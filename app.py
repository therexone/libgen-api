from flask import Flask, jsonify, request 
from scapper import Scapper

app = Flask(__name__)

@app.route('/<query>')
def books(query):
    data = Scapper(query).parse_data()
    return jsonify({'books': data}), 200

@app.route('/<query>/<book_name>')
def book_download(query, book_name):
    data = Scapper(query).parse_data()
    #gets the book_name from the data
    try:
        book = list(filter(lambda book : book['Book']['title'] == book_name, data))[0]
        return jsonify({'book' : book}), 200
    except Exception as e:
        print(e)
        print(book_name)
        return f"Error specified book name not found for query = {query}",404


if __name__ == '__main__':
    app.run(debug=True)
    
    
