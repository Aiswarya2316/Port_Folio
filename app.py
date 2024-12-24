from Flask import flask, render_templates
import sqlite3

@app.route('/')
def home()
    render_templates('home.html')

