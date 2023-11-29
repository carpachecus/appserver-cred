''' This module contains a Flask app that displays
a welcome message , date and the current time'''

# 1. Import libraries
from flask import Flask
from datetime import datetime

# 2. Create a Flask app
app = Flask(__name__)


# 3. Define a route and a view function
@app.route('/')
def index():
    '''This function returns a welcome message and the current time.'''
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%Y-%m-%d")
<<<<<<< HEAD
    return f"<h1>Welcome to my Credibanco web app!</h1><h1>Today's  date is {current_date} and the current time is {current_time}.</h1>"
=======
    return f'<h1>Welcome to my Credibanco web app!</h1><h1>Todays date is {current_date} and the current time is {current_time}.</h1>'
    
>>>>>>> 4278be450aa29b3267b9c27cbf279e3406cc460d

# 4. Run the app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"))
