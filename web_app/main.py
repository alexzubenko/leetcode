# https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/
# Line 1: Here we are importing the Flask
# module and creating a Flask web server from the Flask module.
from flask import Flask, render_template


# Line 3: __name__ means this current file. In this case,
# it will be main.py. This current file will represent my web application.
app = Flask(__name__)

# Line 5: It represents the default page.
# For example, if I go to a website such as “google.com/”
# with nothing after the slash. Then this will be the default page of Google.
@app.route("/")

# Line 6–7: When the user goes to my website and they go to the
# default page (nothing after the slash), then the function below will get activated
def home():
    return render_template("home.html")
    # your_name = input("Say your name please: ")
    # return "Say hello to Flask! {}".format(your_name)

@app.route("/salvador")
def salvador():
    return "Hello Salvador"

@app.route("/about")
def about():
    return render_template("about.html")
# Line 9: When you run your Python script, Python assigns the name “__main__” to the script when executed.
#
# If we import another script, the if statement will prevent other scripts from running.
# When we run main.py,
# it will change its name to __main__ and only then will that if statement activate.
if __name__ == "__main__":
    # Line 10: This will run the application. Having debug=True allows possible
    # Python errors to appear on the web page.
    # This will help us trace the errors.

    # In your Terminal or Command Prompt go to the folder that contains your main.py.
    # Then do py main.py or python main.py.
    app.run(debug=True)

