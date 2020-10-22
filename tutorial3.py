import cherrypy
import random, string
class App(object):
    @cherrypy.expose
    def index(self):
        return "<h1>Hello World!!!</h1>"

    @cherrypy.expose
    def generate(self, l = 8):
        return "<h1>{}</h1>".format("".join(random.sample(string.hexdigits, int(l))))

if __name__ == "__main__":
    cherrypy.quickstart(App())
