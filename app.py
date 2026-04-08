from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)
app.secret_key = 'elena_geo'

# 1. Database Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345678'
app.config['MYSQL_DB'] = 'employee_db'

mysql = MySQL(app)

# 2. READ: The Home Page
@app.route('/')
def Index():
    cur = None
    try:
        cur = mysql.connection.cursor()
        
        # Fetching Employees
        cur.callproc('GetAllEmployees')
        employee_data = cur.fetchall()

        # Clearing buffers for the next procedure call
        while cur.nextset():
            pass
        
        # Fetching Stats
        cur.callproc('GetEmployeeStats')
        stats_data = cur.fetchone()
        
        return render_template("index.html", employees=employee_data, 
                               total=stats_data[0], budget=stats_data[1], 
                               max_s=stats_data[2], top_d=stats_data[3])
    except Exception as e:
        print(f"Error during Read: {e}")
        return render_template("index.html", employees=[], total=0, budget=0, max_s=0, top_d="N/A", error="Database connection failed.")
    finally:
        if cur: cur.close()

# 3. CREATE: Add Employees
@app.route('/insert', methods=['POST'])
def insert():
    cur = None
    if request.method == 'POST':
        try:
            data = (
                request.form['emp_id'],
                request.form['first_name'],
                request.form['last_name'],
                request.form['email'],
                request.form['phone'],
                request.form['department'],
                request.form['salary'],
                request.form['doj']
            )

            cur = mysql.connection.cursor()
            cur.callproc('AddEmployees', data)
            mysql.connection.commit()
            flash("Employee Added Successfully!", "success")
        except Exception as e:
            flash(f"Failed to add employee: {str(e)}", "danger")
        finally:
            if cur: cur.close()
            
        return redirect(url_for('Index'))
    
# 4. UPDATE: Edit Employee
@app.route('/update', methods=['POST'])
def update():
    cur = None
    if request.method == 'POST':
        try:
            data = (
                request.form['id'],
                request.form['emp_id'],
                request.form['first_name'],
                request.form['last_name'],
                request.form['email'],
                request.form['phone'],
                request.form['department'],
                request.form['salary'],
                request.form['doj']
            )
            cur = mysql.connection.cursor()
            cur.callproc('UpdateEmployee', data)
            mysql.connection.commit()
            flash("Employee Updated Successfully", "success")
        except Exception as e:
            flash(f"Failed to update employee: {str(e)}", "danger")
        finally:
            if cur: cur.close()
            
        return redirect(url_for('Index'))

# 5. DELETE: Remove Employee  
@app.route('/delete/<string:id_data>', methods=['GET'])
def delete(id_data):
    cur = None
    try:
        cur = mysql.connection.cursor()
        cur.callproc('DeleteEmployee', [id_data])
        mysql.connection.commit()
        flash("Employee Deleted Successfully", "success")
    except Exception as e:
        flash(f"Error during deletion: {str(e)}", "danger")
    finally:
        if cur: cur.close()
        
    return redirect(url_for('Index'))

if __name__ == "__main__":
    app.run(debug=True)