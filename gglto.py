from flask import Flask, redirect

import re


app = Flask(__name__)
replace_special_chars = re.compile('[-_+]')


@app.route("/")
def index():
  return "This is a simpler version of ggl.to, see " + \
    "http://str8.to/techcrunch-look-fo.  Migrated hosting a while back." + \
    "Feel free to bother @alexeymk with questions or concerns"


@app.route("/<search_query>")
def redirect_search(search_query):
  query_escaped = replace_special_chars.sub('%20', search_query)
  return redirect("http://google.com/search?q={}".format(query_escaped))


if __name__ == '__main__':
  app.run()
