from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_menu():
    conn = sqlite3.connect('mess.db')
    cursor = conn.cursor()
    cursor.execute("SELECT day, breakfast, lunch, dinner FROM menu")
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/')
def index():
    menu = get_menu()
    return render_template('index.html', menu=menu)

if __name__ == '__main__':
    app.run(debug=True)
