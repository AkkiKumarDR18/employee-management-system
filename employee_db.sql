CREATE DATABASE IF NOT EXISTS Employee_db;
USE Employee_db;

DROP TABLE IF EXISTS employee;

CREATE TABLE IF NOT EXISTS employees (
	id INT AUTO_INCREMENT PRIMARY KEY,
    emp_id VARCHAR(20) UNIQUE NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(10) UNIQUE NOT NULL,
    department VARCHAR(50) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL CHECK (salary BETWEEN 15000 AND 500000),
    join_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DESC employees;

DELIMITER //
CREATE PROCEDURE IF NOT EXISTS GetAllEmployees()
BEGIN
	SELECT * FROM employees ORDER BY created_at DESC;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE IF NOT EXISTS AddEmployees(
	IN p_emp_id VARCHAR(20),
    IN p_first_name VARCHAR(50),
    IN p_last_name VARCHAR(50),
    IN p_email VARCHAR(100),
    IN p_phone VARCHAR(10),
    IN p_dept VARCHAR(50),
    IN p_salary DECIMAL(10, 2),
    IN p_doj DATE
)
BEGIN
	INSERT INTO employees (emp_id, first_name, last_name, email, phone, department, salary, join_date)
    VALUES (p_emp_id, p_first_name, p_last_name, p_email, p_phone, p_dept, p_salary, p_doj);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE IF NOT EXISTS UpdateEmployee(
	IN p_id INT,
    IN p_emp_id VARCHAR(20),
    IN p_first_name VARCHAR(50),
    IN p_last_name VARCHAR(50),
    IN p_email VARCHAR(100),
    IN p_phone VARCHAR(10),
    IN p_dept VARCHAR(50),
    IN p_salary DECIMAL(10,2),
    IN p_doj DATE
)
BEGIN
	UPDATE employees
    SET emp_id = p_emp_id, first_name = p_first_name, last_name = p_last_name,
		email = p_email, phone = p_phone, department = p_dept,
        salary = p_salary, join_date = p_doj
	WHERE id = p_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE IF NOT EXISTS DeleteEmployee(IN p_id INT)
BEGIN
	DELETE FROM employees WHERE id = p_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE IF NOT EXISTS GetEmployeeStats()
BEGIN
	SELECT
		COUNT(*) AS total_count,
        IFNULL(SUM(salary), 0) AS total_budget,
        IFNULL(MAX(salary), 0) AS max_salary,
        (SELECT department FROM employees GROUP BY department ORDER BY COUNT(*) DESC LIMIT 1) AS top_dept
	FROM employees;
END //

SELECT * FROM employees;
	
