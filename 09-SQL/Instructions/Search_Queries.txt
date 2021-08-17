--Displays employee number, last name, first name and salary
select 
	e.emp_no,
	e.last_name,
	e.first_name,
	s.salary
from
	"Employees" e
join
	"Salaries" s on
	e.emp_no = s.emp_no;

	
--Displays the first name, last name and hire date for employees hired in 1986
select
	e.first_name,
	e.last_name,
	e.hire_date
from
	"Employees" e
where e.hire_date between '1986-01-01 00:00:00' AND '1986-12-31 23:59:59.000';


--Displays the manager of each department with the department number, deparment name, manager's employee number, last name and first name
select
	dm.dept_no,
	d.dept_name,
	dm.emp_no,
	e.last_name,
	e.first_name
from
	dept_manager dm
join
	"Department" d on
		dm.dept_no = d.dept_no
join	
	"Employees" e on
		dm.emp_no = e.emp_no;


--Displays the employee's number, first name, last name and department name
select
	e.emp_no,
	e.first_name,
	e.last_name,
	d.dept_name
from
	"Employees" e
join
	dept_emp de on
		e.emp_no = de.emp_no
join
	"Department" d on
		de.dept_no = d.dept_no


--Displays the first name, last name and sex for employees with the first name "Hercules" and last names begin with "B"
select
	e.first_name,
	e.last_name,
	e.sex
from
	"Employees" e
where
	e.first_name = 'Hercules' and e.last_name like 'B%';


--Displays all employees' number, last name, first name and department name in the sales department
select
	e.emp_no,
	e.last_name,
	e.first_name,
	d.dept_name
from 
	"Employees" e
join
	dept_emp de on
		e.emp_no = de.emp_no
join
	"Department" d on
		de.dept_no = d.dept_no
where
	d.dept_name = 'Sales';


--Displays all employees' number, last name, first name and department name in the sales and development departments
select
	e.emp_no,
	e.last_name,
	e.first_name,
	d.dept_name
from 
	"Employees" e
join
	dept_emp de on
		e.emp_no = de.emp_no
join
	"Department" d on
		de.dept_no = d.dept_no
where
	d.dept_name = 'Sales' or d.dept_name = 'Development';


--Displays the frequency count of employee last names in descending order
select
	e.last_name,
	count(e.last_name)
from
	"Employees" e
group by 
	e.last_name
order by
	count(e.last_name) desc;

