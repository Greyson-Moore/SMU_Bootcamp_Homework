-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


drop table if exists "dept_emp";

drop table if exists "dept_manager";

drop table if exists "Department";

drop table if exists "Salaries";

drop table if exists "Employees";

drop table if exists "Titles";


CREATE TABLE "dept_emp" (
    "id" serial   NOT NULL,
	"emp_no" int   NOT NULL,
    "dept_no" varchar(30)   NOT NULL,
    "last_updated" timestamp   NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT "pk_dept_emp" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "dept_manager" (
    "id" serial   NOT NULL,
    "dept_no" varchar(10)   NOT NULL,
    "emp_no" int   NOT NULL,
    "last_updated" timestamp   NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT "pk_dept_manager" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "Department" (
    "dept_no" varchar(10)   NOT NULL,
    "dept_name" varchar(30)   NOT NULL,
    "last_updated" timestamp   NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT "pk_Department" PRIMARY KEY (
        "dept_no"
     )
);

CREATE TABLE "Salaries" (
    "id" serial   NOT NULL,
    "emp_no" int   NOT NULL,
    "salary" int   NOT NULL,
    "last_updated" timestamp   NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT "pk_Salaries" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "Titles" (
    "title_id" varchar(15)   NOT NULL,
    "title" varchar(30)   NOT NULL,
    "last_updated" timestamp   NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT "pk_Titles" PRIMARY KEY (
        "title_id"
     )
);

CREATE TABLE "Employees" (
    "emp_no" int   NOT NULL,
    "emp_title" varchar(15)   NOT NULL,
    "birth_date" timestamp   NOT NULL,
    "first_name" varchar(50)   NOT NULL,
    "last_name" varchar(50)   NOT NULL,
    "sex" varchar(10)   NOT NULL,
    "hire_date" timestamp   NOT NULL,
    "last_updated" timestamp   NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT "pk_Employees" PRIMARY KEY (
        "emp_no"
     )
);

ALTER TABLE "dept_emp" ADD CONSTRAINT "fk_dept_emp_dept_no" FOREIGN KEY("dept_no")
REFERENCES "Department" ("dept_no");

ALTER TABLE "dept_emp" ADD CONSTRAINT "fk_dept_emp_emp_no" FOREIGN KEY("emp_no")
REFERENCES "Employees" ("emp_no");

ALTER TABLE "dept_manager" ADD CONSTRAINT "fk_dept_manager_dept_no" FOREIGN KEY("dept_no")
REFERENCES "Department" ("dept_no");

ALTER TABLE "dept_manager" ADD CONSTRAINT "fk_dept_manager_emp_no" FOREIGN KEY("emp_no")
REFERENCES "Employees" ("emp_no");

ALTER TABLE "Salaries" ADD CONSTRAINT "fk_Salaries_emp_no" FOREIGN KEY("emp_no")
REFERENCES "Employees" ("emp_no");

ALTER TABLE "Employees" ADD CONSTRAINT "fk_Employees_emp_title" FOREIGN KEY("emp_title")
REFERENCES "Titles" ("title_id");


