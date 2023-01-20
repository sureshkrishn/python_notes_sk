from flask import Flask,render_template
import cx_Oracle

app = Flask(__name__)

@app.route('/data')
def get_data():
    try:
        
        # Connect to the Oracle database
        con = cx_Oracle.connect('stcskills/root123@localhost:1521')
        cur = con.cursor()

        # Execute a query to fetch data
        query = 'SELECT empno , ename ,job FROM emp'
        cur.execute(query)
        data = cur.fetchall()

        # Close the cursor and connection
        cur.close()
        con.close()

        # Return the data as a JSON object
        return render_template('data.html', data=data)
    except cx_Oracle.DatabaseError as e:
        # Return an error message if there's a problem connecting to the database
        return str(e)

if __name__ == '__main__':
    app.run(debug = True)



