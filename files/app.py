from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    try:
        conn = mysql.connector.connect(
            host="db",
            user="root",
            password="rootpass",
            database="testdb"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT message FROM greetings LIMIT 1;")
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return f"<h1>Welcome!</h1><p>{result[0]}</p>"
    except Exception as e:
        return f"<h1>Backend Error</h1><p>{e}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


