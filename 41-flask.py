# Theory about this code:

# This code demonstrates how to create a simple Flask web application using Python.
# Flask(__name__) creates the web application, and @app.route() defines different URL routes.
# The / route displays a basic welcome message.
# The /first_page and /second_page routes display separate page messages.
# Finally, app.run(debug=True) starts the Flask development server with debug mode enabled.





from flask import Flask




app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

@app.route('/first_page')
def first():
    return 'Hello, this is my first page'

@app.route('/second_page')
def secnond():
    return 'Hello, this is my sencond page'

if __name__ == '__main__':
    app.run(debug=True)





