from flask import Flask, render_template, request, jsonify, redirect, url_for
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
def auth(username, password):
    print("результат")
    cursor.execute("SELECT username, password FROM Users WHERE username ='%s';" % (username))
    row = cursor.fetchone()
    if row:
        if row[1] == password:
            user = User(username, "user")
            return "authorization completed"
        else:
            return "authorization failed: incorrect password"
    else:
        return "the user does not exist"
text = "Loren ipsum"
def insert_to_db():
    
    cursor.execute("INSERT INTO Posts(name, text, author) VALUES(%s, %s, %s);", ("Пост1", text, "admin"))
    cursor.execute("SELECT * FROM Posts;")
    rows = cursor.fetchall()
    
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
            return jsonify({"error": "Missing username or password"}), 400
            
        auth_result = auth(username, password)
        
        if auth_result == "admin":
            return redirect(url_for('admin'))
        elif auth_result == "authorization completed":
            return render_template("index.html")
        else:
            return "Нету пользователя"
    return render_template('login.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')
@app.route('/calendar')
def calendar():
    return render_template('calendar.html')
@app.route('/articles')
def articles():
    name = "post 1"
    cursor.execute("SELECT name, text, author FROM Posts WHERE name ='%s';" % (name))
    row = cursor.fetchone()
    return render_template('articles.html', text = row[1], header = row[0])

# http://127.0.0.1:5000/home

if __name__ == '__main__':  
    insert_to_db()
    app.run(debug=True)
    
# CREATE TABLE Users(id SERIAL PRIMARY KEY, username VARCHAR(30), password VARCHAR(20), name VARCHAR(40)); таблица пользователей
    
# CREATE TABLE Posts(id SERIAL PRIMARY KEY, name VARCHAR(30), text VARCHAR(2000), author VARCHAR(30));- таблица постов
