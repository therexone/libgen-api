from flask import Flask, jsonify, request
from scrapper import Scrapper
from downloadFetcher import DownloadFetcher

app = Flask(__name__)


@app.route('/<query>')
def books(query):
    data = Scrapper(query).parse_data()
    return jsonify({'books': data}), 200


@app.route('/<query>/<book_name>')
def book_download(query, book_name):
    data = Scrapper(query).parse_data()
    # gets the book_name from the data and gets the direct download link for the book
    try:
        book = list(
            filter(lambda book: book['Book']['title'] == book_name, data))[0]
        direct_dl = DownloadFetcher(book).get_direct_download()
        return jsonify({'book': book, 'download': direct_dl}), 200

    except Exception as e:
        print(e)
        print(book_name)
        return f"Error specified book name not found for query = {query}", 404


if __name__ == '__main__':
    app.run(debug=True)
