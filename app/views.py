from app import app

@app.route('/')
@app.route('/index')
@app.route('/index.html')
@app.route('/home')
def index():
    return "Hello, World"
