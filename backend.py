from flask import Flask, request, jsonify, send_from_directory
import sqlite3
import os

app = Flask(__name__)

# 确保数据库文件存在
if not os.path.exists('paste.db'):
    with sqlite3.connect('paste.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                text TEXT NOT NULL,
                timestamp TEXT NOT NULL
            )
        ''')
        conn.commit()

def get_db_connection():
    conn = sqlite3.connect('paste.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/dates', methods=['GET'])
def get_dates():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT date FROM records')
    dates = [row['date'] for row in cursor.fetchall()]
    conn.close()
    return jsonify(dates)

@app.route('/api/records', methods=['GET'])
def get_records():
    date = request.args.get('date')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT text, timestamp FROM records WHERE date = ? ORDER BY timestamp DESC', (date,))
    records = [{'text': row['text'], 'timestamp': row['timestamp']} for row in cursor.fetchall()]
    conn.close()
    return jsonify(records)

@app.route('/api/save', methods=['POST'])
def save_record():
    data = request.json
    date = data['date']
    record = data['record']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO records (date, text, timestamp) VALUES (?, ?, ?)', 
                   (date, record['text'], record['timestamp']))
    conn.commit()
    conn.close()
    return jsonify({'status': 'success'})

@app.route('/api/delete', methods=['POST'])
def delete_record():
    data = request.json
    date = data['date']
    record = data['record']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM records WHERE date = ? AND text = ? AND timestamp = ?', 
                   (date, record['text'], record['timestamp']))
    conn.commit()
    conn.close()
    return jsonify({'status': 'success'})

@app.route('/api/update', methods=['POST'])
def update_record():
    data = request.json
    date = data['date']
    record = data['record']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE records SET text = ?, timestamp = ? WHERE date = ? AND text = ?', 
                   (record['text'], record['timestamp'], date, record['text']))
    conn.commit()
    conn.close()
    return jsonify({'status': 'success'})

@app.route('/', methods=['GET'])
def serve_page():
    with open('paste.html', 'r', encoding='utf-8') as file:
        content = file.read()
    return content

@app.route('/webfonts/<filename>', methods=['GET'])
def serve_webfont(filename):
    return send_from_directory('webfonts', filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
