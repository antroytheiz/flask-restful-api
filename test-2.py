from flask import *
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'theis'
app.config['MYSQL_PASSWORD'] = 'salupa'
app.config['MYSQL_DB'] = 'flask-api'

mysql = MySQL(app)

@app.route('/', methods=['GET'])
def index():
    conn = mysql.connection.cursor()
    conn.execute('SELECT * FROM rest_flask')
    data = []
    for id,language,framework in conn.fetchall():
        data.append({'id':id, 'language':language, 'framework':framework})    

    return jsonify({'result': data})

if __name__ == "__main__":
    app.run(debug=True)


# conn.execute('''CREATE TABLE rest_flask (id INTEGER, language VARCHAR(30), framework VARCHAR(30))''')
# conn.execute(''' INSERT INTO rest_flask VALUES 
#             (1, "Python", "Flask"),
#             (2,"Python", "Django"),
#             (3,"PHP", "Laravel"),
#             (4, "JavaScript", "Node JS")                 
#             ''')
# mysql.connection.commit()