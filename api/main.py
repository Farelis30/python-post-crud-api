from flask import Flask

app = Flask(__name__)

@app.get('/')
def index():
    return 'Hello world!!!'

@app.get('/about')
def about():
    return 'About Page'

@app.errorhandler(404)
def error_handler_page(error):
    return "Halaman ini tidak tersedia", 404