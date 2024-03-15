import pandas as pd
import sqlite3

# Establish a connection to the SQLite database in memory
conn = sqlite3.connect(':memory:')

# Read files 
employee_df = pd.read_csv('.\Relations\employee.csv')
department_df = pd.read_csv('.\Relations\department.csv')
female_df = pd.read_csv('./Relations/female.csv')
project_df = pd.read_csv('.\Relations\project.csv')
salary_df = pd.read_csv('.\Relations\salary.csv')
supervise_df = pd.read_csv('.\Relations\supervise.csv')
workson_df = pd.read_csv('.\Relations\workson.csv')
# Load the CSV data into SQL tables
department_df.to_sql('department', conn, if_exists='replace', index=False)
employee_df.to_sql('employee', conn, if_exists='replace', index=False)
female_df.to_sql('female', conn, if_exists='replace', index=False)
project_df.to_sql('project', conn, if_exists='replace', index=False)
salary_df.to_sql('salary', conn, if_exists='replace', index=False)
supervise_df.to_sql('supervise', conn, if_exists='replace', index=False)
workson_df.to_sql('workson', conn, if_exists='replace', index=False)

# Query 1: Females on project "computerization" with 10 hours of effort and supervised by "jennifer"
q1_df = pd.read_sql_query("""
SELECT e.EMPLOYEE_NAME
FROM employee e
JOIN workson w ON e.EMPLOYEE_NAME = w.NAME
JOIN supervise s ON e.EMPLOYEE_NAME = s.SUBORDINATE
JOIN female f ON e.EMPLOYEE_NAME = f.NAME
WHERE w.PROJECT = 'computerization' AND w.EFFORT = 10 AND s.SUPERVISOR = 'jennifer'
""", conn)

# Query 2: Employee who makes over 40000 and works for research department
q2_df = pd.read_sql_query("""
SELECT e.EMPLOYEE_NAME
FROM employee e
JOIN salary sa ON e.EMPLOYEE_NAME = sa.EMPLOYEE_NAME
JOIN department d ON e.EMPLOYEE_NAME = d.EMPLOYEE_NAME
WHERE sa.SALARY > 40000 AND d.DEPARTMENT = 'research'
""", conn)

# Query 3: Supreme chief of the company (President)
q3_df = pd.read_sql_query("""
SELECT e.EMPLOYEE_NAME
FROM employee e
LEFT JOIN supervise s ON e.EMPLOYEE_NAME = s.SUBORDINATE
WHERE s.SUPERVISOR IS NULL
""", conn)

# Query 4: Individuals who work on "productx" with effort of 20 or more hours
q4_df = pd.read_sql_query("""
SELECT w.NAME
FROM workson w
WHERE w.PROJECT = 'productx' AND w.EFFORT >= 20
""", conn)

# Close the connection to the database
conn.close()

# Display the results
print("Q1 Results:")
print(q1_df)
print("\nQ2 Results:")
print(q2_df)
print("\nQ3 Results:")
print(q3_df)
print("\nQ4 Results:")
print(q4_df)
