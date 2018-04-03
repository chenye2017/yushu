from flask import Flask,make_response,jsonify
from helper import is_isbn_or_keyword
from yushu_book import YuShuBook

app = Flask(__name__)

@app.route('/hello')
def hello():
    headers = {
        'content-type':'text/plain',
        'location': 'http://www.baidu.com'
    }

    response = make_response('<html>hello, chenye</html>',302)
    response.headers = headers

    return response
# @app.route('/book/search/<q>/<page>')
# def search(q, page):
#     return jsonify('ll')
#     #先判断传进来的是isbn还是关键字
#     isbn_or_keyword = is_isbn_or_keyword(q)
#     if isbn_or_keyword == 'isbn':
#         result = YuShuBook.search_by_isbn(q)
#         return jsonify(result)
#     if isbn_or_keyword == 'key':
#         result = YuShuBook.search_by_key(q)
#         return jsonify(result)

#app.add_url_rule('/hello', view_func=hello)

app.run(host='0.0.0.0', debug=True)