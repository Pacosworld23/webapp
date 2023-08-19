from flask import Blueprint, render_template

# Create a blueprint named 'views'
views = Blueprint('views', __name__)

# Define a route for the root URL '/'
@views.route('/')
def home():
    return render_template("home.html")
