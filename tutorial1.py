import cherrypy


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "<p><h1>Hello world!</h1></p>"

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_port': 8000})
    cherrypy.quickstart(HelloWorld(), "/")
