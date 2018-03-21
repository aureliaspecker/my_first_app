from flask import Flask, render_template, request

app = Flask("MyApp")

@app.route("/") #this is a decorator. It is very powerful. You're saying "Before you call this method, use x code. And after you call teh method, use y code." It needs to be put before every function.
def hello():
    return "Hello World!"

@app.route("/idontexist")
def idontexist():
    return "I do exist now!"

@app.route("/aurelia")
def desert():
    return "I'm not sure what my favourite desert is..."

@app.route("/<name>") #this says "whatever anybody enters in the URL, it will take that entry and store it as a variable called name and then pass that variable into the hello function and render the HTML template"
def hello_someone(name):
    return render_template("hello.html", name=name.title()) #.title() makes the name become upper case (turns it into a title)

@app.route("/signup", methods=["POST"]) #POST vs GET (you can see this appear in Terminal). GET is when you're asking the server to give you the webpage you're asking for. POST means you give the server some information to do something with. You always need a POST for form submissions with HTML.
def sign_up():
    form_data = request.form #request.form requests the form from html (this is why it's important that the id matches this)
    print form_data["email"] #this prints in the terminal (referring back to the id of 'email' in the html)
    return "All OK"

app.run(debug=True) #to tell the application to run
