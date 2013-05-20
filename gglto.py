from flask import Flask, redirect
app = Flask(__name__)

@app.route("/")
def index():
  return "this is a simpler version of ggl.to"


@app.route("/<search_query>")
def redirect_search(search_query):
  return redirect("http://google.com/search?q={}".format(search_query))

if __name__ == '__main__':
  app.run()
