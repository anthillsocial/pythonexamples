#!/usr/bin/python
# Works with both python2 and pyhton3
# Make sure jinja and cherrypy are installed for pyhton2 OR python3
# depending on which version of pyhton you use
import cherrypy, os, threading
from jinja2 import Environment, FileSystemLoader
ENV = Environment(loader=FileSystemLoader('templates'))

# Setup the server
class CherryPyServer:

    # Initialise the server
    def __init__(self, port):
        # Initial configeration
        cherrypy.config.update({
            'server.socket_host': '0.0.0.0',
            'server.socket_port': port,
            'server.max_request_body_size':416000000
        })
        # Enable the following paths
        self.paths = self.paths()
        self.root = Root()
        # And startup the web application
        threading.Thread(target=self.startserver).start()
    
    # Specify how specific URLS shoudl be handled
    def paths(self):
        return {
            '/': {
                'tools.staticdir.root': os.path.abspath(os.getcwd())
            },
            '/public': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': './public'
            }        
        }

    # start the webserver in its own thread
    def startserver(self):
        cherrypy.quickstart(self.root, '/', self.paths)

    # Pass some variables to the display
    def update(self, newvars):
        self.root.update(newvars)       

# Manage the display when you visit 'http://0.0.0.0:8787'
class Root(object):
    
    # Initialise the root object
    def __init__(self):
        self.newvars = {}
    
    def update(self, newvars):
        self.newvars = newvars
        print(newvars)

    @cherrypy.expose
    def index(self, **kwargs):
        template = ENV.get_template('index.html')
        passvars = {'title':'index', 'getvars':kwargs, 'postvars':cherrypy.request.body_params, 'extvars':self.newvars}
        return template.render(pagevars=passvars)
    
    @cherrypy.expose
    def page2(self, *args, **kwargs):
        template = ENV.get_template('index.html')
        passvars = {'title':'Page 2', 'args':args, 'kwargs':kwargs, 'extvars':self.newvars}
        return template.render(pagevars=passvars)

# Example usage
if __name__ == '__main__':
    import time, datetime
    # Start a web serve run its own thread
    server = CherryPyServer(port=8787)
    # Now continue with other code and send variables as and when they are ready
    while True:
        current_time = datetime.datetime.now().time()
        server.update({'time':current_time})
        time.sleep(1)

