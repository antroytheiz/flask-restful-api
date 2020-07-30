from flask import *

app = Flask(__name__)

languages = [
        {'name':'Python'},
        {'name':'Javascript'},
        {'name':'PHP'}
    ]

@app.route('/')
def home():
    return """
    <h1>Welcome</h1>
    <p><a href='/languages'>Languages</a></p>    
    """

@app.route('/language', methods=['get'])
def langAll():
    return jsonify({'message':languages})

# Menampilkan data
@app.route('/language/<string:name>', methods=['get'])
def langOne(name):
    lang = [language for language in languages if language['name'] == name]
    return jsonify({'language':lang})

# Membuat data
@app.route('/language', methods=['post'])
def addOne():
    language = {'name' : request.json['name']}

    languages.append(language)
    return jsonify({'languages': languages})

# Mengubah data
@app.route('/language/<string:name>', methods=['put'])
def updateOne(name):
    language = [language for language in languages if language['name'] == name]
    language[0]['name'] = request.json['name']
    return jsonify({'language':languages[0]})

# Menghapus data
@app.route('/language/<string:name>', methods=['delete'])
def deleteOne(name):
    language = [language for language in languages if language['name'] == name]
    languages.remove(language[0])
    return jsonify({'languages': languages[0]})
    
if __name__ == "__main__":
    app.run(debug=True)