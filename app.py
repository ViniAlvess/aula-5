from flask import Flask

app =Flask(__name__)

@app.route("/")
def index():
    return"<h1> Senac Digi </h1>" 

@app.route('/quemsomos')
def quemsomos():
    return "<h2> Quem somos </h2>"

@app.route ('/produtos/<numero_produto>')
def produtos(numero_produto):
    return "<h2> produtos </h2>"

@app.route('/login')
def login():
    return "<h2> Login </h2>"
    
if __name__ == '__main__':
    app.run(debug=True)