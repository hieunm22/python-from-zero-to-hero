import home
import account

@app.errorhandler(401)
def page_forbidden(e):
  f = codecs.open('html/401.html', 'r')
  return f.read()

@app.errorhandler(404)
def page_not_found(e):
  f = codecs.open('html/404.html', 'r')
  return f.read()