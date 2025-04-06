from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        conn = psycopg2.connect(
            host=os.environ['DB_HOST'],
            dbname=os.environ['DB_NAME'],
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASSWORD']
        )
        cur = conn.cursor()
        cur.execute('SELECT version();')
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return f"Connected to PostgreSQL!<br>Version: {db_version[0]}"
    except Exception as e:
        return f"Database connection failed: {e}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
