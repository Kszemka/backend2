# app.py
from flask import Flask, jsonify
import psycopg2
from psycopg2 import sql
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Database configuration
db_config = {
    'host': 'database',
    'port': '5432',
    'database': 'task_db',
    'user': 'postgres',
    'password': 'postgres'
}

# Function to get task categories from the database
def get_task_categories():
    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()

    try:
        query = sql.SQL('SELECT * FROM task_category;')
        cur.execute(query)
        categories = cur.fetchall()
        return categories
    except Exception as e:
        print(f"Error: {e}")
        return []
    finally:
        cur.close()
        conn.close()

# Define a route to get task categories in JSON format
@app.route('/task-categories', methods=['GET'])
def list_task_categories():
    categories = get_task_categories()
    category_list = [{'id': category[0], 'category_name': category[1]} for category in categories]
    return jsonify(category_list)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
