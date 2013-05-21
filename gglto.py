from flask import Flask, redirect, request

import re


app = Flask(__name__)
replace_special_chars = re.compile('[-_+]')
domain_to_redirect_url = {
  "ggl.to": "http://www.google.com/search?rls=ig&hl=en&sa=Search&q={}",
  "look.fo": "http://www.google.com/search?rls=ig&hl=en&sa=Search&q={}",
  "str8.to": "http://www.google.com/search?rls=ig&hl=en" +
    "&btnI=I'm+Feeling+Lucky&sourceid=navclient&q={}"
}


@app.route("/")
def index():
  return """<pre>
This is a simpler version of {domain}, see http://str8.to/techcrunch-look-fo.

Migrated hosting a while back; feel free to bother @alexeymk with questions or concerns
    </pre>""".format(domain=request.headers['Host'])


@app.route("/<search_query>")
def redirect_search(search_query):
  base_path = domain_to_redirect_url.get(request.headers['Host'],
    "http://google.com/search?q={}")  # default to simplest possible version
  query_escaped = replace_special_chars.sub('%20', search_query)
  return redirect(base_path.format(query_escaped))


if __name__ == '__main__':
  app.run()
