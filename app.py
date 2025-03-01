from flask import Flask, render_template
import psycopg2

connection =psycopg2.connect(
    dbname = "projectdb",
    user = "postgres",
    password="32081ABc",
    host="localhost",
    port = "5432"
)
class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

cursor = connection.cursor()
app = Flask(__name__)
def insert_to_db():
    text = "Lorem ipsum"
    cursor.execute("INSERT INTO Posts(name, text, author) VALUES(%s, %s, %s);", ("Пост1", text, "admin"))
    cursor.execute("SELECT * FROM Posts;")
    rows = cursor.fetchall()
    for row in rows:
        for i in row:
            print(i);
@app.route('/home')
def home():
    return render_template('index.html')
@app.route('/chat')
def chat():
    return render_template('chat.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/admin')
def admin():
    return render_template('admin.html')
@app.route('/calendar')
def calendar():
    return render_template('calendar.html')
@app.route('/articles')
def articles():
    return render_template('articles.html', text = text, header = "Заголовок")
# http://127.0.0.1:5000/home

if __name__ == '__main__':  
    insert_to_db()
    app.run(debug=True)
    
# CREATE TABLE Users(id SERIAL PRIMARY KEY, username VARCHAR(30), password VARCHAR(20), name VARCHAR(40)); таблица пользователей
    
# CREATE TABLE Posts(id SERIAL PRIMARY KEY, name VARCHAR(30), text VARCHAR(2000), author VARCHAR(30));- таблица постов
