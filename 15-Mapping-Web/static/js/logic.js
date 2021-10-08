var url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";//baseURL + timeframe;


$(document).ready(function(){

    $.ajax({
        type: "GET",
        url: url,
        contentType: "application/json",
        dataType: "json",
        success: function(data) {
            console.log(data);

            createMap(data); 

        },
        error: function(data) {
            console.log("YOU BROKE IT!!");
        },
        complete: function(data) {
            console.log("Request finished");
        }
    });



});


function createMap(data){
    


    let features = data.features;

    var markers = L.layerGroup();

    for(let i=0;i<features.length;i++){
        
        var coordinates = features[i].geometry;
        if(coordinates){
            let marker = L.circleMarker([coordinates.coordinates[1],coordinates.coordinates[0]],{
                color:colors(features[i].properties.mag),
                radius:features[i].properties.mag * 5,
                fillOpacity:.75
            });
            marker.bindPopup(`<h3>Location:</h3><p>${features[i].properties.place}</p><h3>Magnitude:</h3><p>${features[i].properties.mag}</p><h3>Time:</h3><p>${new Date(features[i].properties.time)}</p>`);
            markers.addLayer(marker);

        }
    }

    var overlayMaps = {
        "Markers": markers,
    };



    var light_layer = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        id: 'mapbox/light-v10',
        accessToken: API_KEY
    })

    var satellite_layer = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        id: 'mapbox/satellite-v9',
        accessToken: API_KEY
    })

    var baseMaps = {
        "Light":light_layer,
        "Satellite":satellite_layer
    }

    var myMap = L.map("map",{
        center:[34.0522,-118.2437],
        zoom: 5,
        layers:[satellite_layer,markers]
    });


    L.control.layers(baseMaps,overlayMaps).addTo(myMap);



};

function colors(mag){
    if(mag > 5){
        return "#FFEF00";
    }
    else if(mag > 3){
        return "#FF7900";
    }
    else if(mag > 1){
        return "#39ff14";
    }
    else{
        return "#e60026";
    }
    
}
