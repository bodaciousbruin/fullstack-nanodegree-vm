from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from database_setup import Base, Restaurant, MenuItem
import sys
import datetime

engine = create_engine( 'sqlite:///restaurantmenu.db')

# binds engine to Base class
Base.metadata.bind = engine

# connect engine to code executions
DBSession = sessionmaker(bind = engine)

# establish a session with a session object
session = DBSession()

class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
            try:
                if self.path.endswith("/restaurants"):
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    
                    # get list of restaurants
                    allRestaurants = session.query(Restaurant.name).order_by(Restaurant.name.asc()).all()
                    
                    restaurantOutputString = "<br>"
                    # format restaurants for display
                    for item in allRestaurants:
                        restaurantOutputString += item[0] + "<br>"
                        restaurantOutputString += "<a href = 'restaurant/id/edit' >Edit</a><br>"
                        restaurantOutputString += "<a href = 'restaurant/id/delete' >Delete</a><br>"
                        restaurantOutputString += "<br>"
                    
                    output = ""
                    output += "<html><body>"
                    output += "<h1>List of Restaurants</h1>"
                    output += restaurantOutputString
                    # output += "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2>\
                    #   <input name='message' type='text' ><input type='submit' value='Submit'></form>"
                    output += "</body></html>"
                    self.wfile.write(output)
                    print output
                    return
                
                if self.path.endswith("/restaurants/new"):
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    
                    output = ""
                    output += "<html><body>"
                    output += "<h1>Enter name of new restaurant</h1> <a href = '/restaurants' >Back to restaurant List</a>"
                    output += "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2>\
                      <input name='message' type='text' ><input type='submit' value='Submit'></form>"
                    output += "</body></html>"
                    self.wfile.write(output)
                    print output
                    return
                
            except IOError:
                self.send_error(404, "File Not Found %s" % self.path)
                
    def do_POST(self):
        try:
            self.send_response(301)
            self.end_headers()
            
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                fields=cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('message')
                
            output = ""
            output += "<html><body>"
            output += " <h2> Okay, how about this: </h2>"
            output += "<h1> %s </h1>" % messagecontent[0]
            
            output += "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2>\
                      <input name='message' type='text' ><input type='submit' value='Submit'></form>"
            output += "</html></body>"
            self.wfile.write(output)
            print output
            
            
        except:
            pass

def main():
    try:
        port = 8080
        server = HTTPServer(('',port), webserverHandler)
        print "Web server running on port %s" % port
        server.serve_forever()
        
    except KeyboardInterrupt:
        print "^C received.  Stopping webserver..."
        server.socket.close()
        
if __name__ == '__main__':
    main()