## different urls lead to different functions
import cherrypy
import random, string
class App(object):
    @cherrypy.expose
    def index(self):
        return "<h1>Home Page!!</h1>"

    @cherrypy.expose
    def generate(self):
        s="".join(random.sample(string.hexdigits, 4))
        return "<h1>{}</h1>".format(s)

if __name__ == "__main__":
    cherrypy.quickstart(App(), "/")