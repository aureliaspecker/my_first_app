from flask import Flask, render_template

app = Flask("MyApp")

@app.route("/") #this is a decorator. It is very powerful. You're saying "Before you call this method, use x code. And after you call teh method, use y code." It needs to be put before every function.
def hello():
    return "Hello Mirela!"

@app.route("/idontexist") #this is a decorator. It is very powerful. You're saying "Before you call this method, use x code. And after you call teh method, use y code." It needs to be put before every function.
def idontexist():
    return "I do exist now!"

@app.route("/aurelia")
def desert():
    return "I'm not sure what my favourite desert is..."

app.run(debug=True) #to tell the application to run
