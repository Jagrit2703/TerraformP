import webapp2
class Mainpage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')
app=webapp2.WSGIApplication([('/',Mainpage),],debug=True)