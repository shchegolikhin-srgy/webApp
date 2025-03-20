from flask import Flask, render_template, request, jsonify, redirect, url_for
import psycopg2

connection =psycopg2.connect(
    dbname = "projectdb",
    user = "postgres",
    password="postgres",
    host="localhost",
    port = "5432"
)

class User:
    def __init__(self):
        self.username = None
    def setUsername(self, username):
        self.username = username
    def getUsername(self):
        return self.username
cursor = connection.cursor()
user = User()
app = Flask(__name__)
def auth(username, password):
    print("результат")
    cursor.execute("SELECT username, password FROM Users WHERE username ='%s';" % (username))
    row = cursor.fetchone()
    if row:
        if row[1] == password:
            
            return "authorization completed"
        else:
            return "authorization failed: incorrect password"
    else:
        return "the user does not exist"

    
    
@app.route('/home')
def home():
    return render_template('index.html')
@app.route('/chat')
def chat():
    return render_template('chat.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:
            return render_template("login.html")
            
        auth_result = auth(username, password)
        
        if auth_result == "admin":
            user.setUsername("admin")
            return render_template("admin.html")
        elif auth_result == "authorization completed":
            user.setUsername(username)
            return render_template("index.html")
        else:
            return render_template("login.html")
    return render_template('login.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        header = request.form.get('title')
        text = request.form.get('content')
        cursor.execute("INSERT INTO Posts(name, text, author) VALUES(%s, %s, %s);", (header, text, "admin"))
    else:
        if user.getUsername() == "admin":
            return render_template("admin.html")
        else:
            return "Вы не админ"

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')
@app.route('/articles')
def articles():
    name = "post 1"
    cursor.execute("SELECT name, text, author FROM Posts WHERE text LIKE '%s%';")
    row = cursor.fetchone()
    
    return render_template('articles.html', text = row[1], header = row[0])

# http://127.0.0.1:5000/home

if __name__ == '__main__':  
    app.run(debug=True,  host = '0.0.0.0')
    
# CREATE TABLE Users(id SERIAL PRIMARY KEY, username VARCHAR(30), password VARCHAR(20), name VARCHAR(40)); таблица пользователей
    
# CREATE TABLE Posts(id SERIAL PRIMARY KEY, name VARCHAR(30), text VARCHAR(2000), author VARCHAR(30));- таблица постов

