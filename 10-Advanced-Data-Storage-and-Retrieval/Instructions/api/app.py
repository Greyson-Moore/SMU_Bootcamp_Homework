from flask import Flask, jsonify
import pandas as pd
from sqlalchemy import create_engine, func
import json

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

app = Flask(__name__)

@app.route("/")
def home():
        return(
        f"API routes: <br/>" 
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
        f"/api/v1.0/'start' <br/>"
        f"/api/v1.0/'start'/'end' <br/>"
        )

@app.route("/api/v1.0/precipitation")
def precipitation():
        conn = engine.connect()

        query = """
        select
                date, 
                avg(prcp) as Average_Precipitation
        from
                measurement
        group by
                date
        order by 
                date
        """
       
        precip_df = pd.read_sql(query, con=conn)
        
        conn.close()

        precip_data = precip_df.to_json(orient="records")
        precip_data = json.loads(precip_data)

        return jsonify({"ok": True, "data": precip_data})

@app.route("/api/v1.0/stations")
def stations():
        conn = engine.connect()

        query = """
        select
                *
        from
                station
      
        """
       
        station_df = pd.read_sql(query, con=conn)
        
        conn.close()

        station_data = station_df.to_json(orient="records")
        station_data = json.loads(station_data)

        return jsonify({"ok": True, "data": station_data})

@app.route("/api/v1.0/tobs")
def temp():
        conn = engine.connect()

        query = """
        select
                date,
                tobs
        from
                measurement
        where
                station = "USC00519281" AND date between '2016-08-23'AND '2017-08-23'
      
        """
       
        temp_df = pd.read_sql(query, con=conn)
        
        conn.close()

        temp_data = temp_df.to_json(orient="records")
        temp_data = json.loads(temp_data)

        return jsonify({"ok": True, "data": temp_data})


@app.route("/api/v1.0/<start>")
def start(start):
        conn = engine.connect()

        query = f"""
        select
                min(tobs) as minimum,
                max(tobs) as maximum,
                avg(tobs) as average
        from
                measurement
        where
                date >= '{start}'
      
        """
       
        start_df = pd.read_sql(query, con=conn)
        
        conn.close()

        start_data = start_df.to_json(orient="records")
        start_data = json.loads(start_data)

        return jsonify({"ok": True, "data": start_data})


@app.route("/api/v1.0/<start>/<end>")
def end(start,end):
        conn = engine.connect()

        query = f"""
        select
                min(tobs) as minimum,
                max(tobs) as maximum,
                avg(tobs) as average
        from
                measurement
        where
                date between '{start}' AND '{end}'
      
        """
       
        end_df = pd.read_sql(query, con=conn)
        
        conn.close()

        end_data = end_df.to_json(orient="records")
        end_data = json.loads(end_data)

        return jsonify({"ok": True, "data": end_data})



if __name__ == '__main__':
    app.run(debug=True)
