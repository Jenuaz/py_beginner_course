from flask import Flask #we need to import Flask from the Flask module in order to create our own Flask web API 
app = Flask(__name__) #we creatinga new Flask app by creating  an instance of Flask giving it the name of the app. 

@app.route("/") #now we can start creating a route for our web API
def hello(): #to define a functionality of this route we define a function immediately below the rout declaration
    return "Hellow World!"

@app.route("/user/<username>")  #So we can make a parameterized URL and use <variable> as parameter
def show_user(username):
    return "User: %s" % username
