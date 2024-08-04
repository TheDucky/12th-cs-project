from flask import Flask, render_template
from lib import ctrl_db as cd

# creating instance of Flask class
app = Flask(__name__) 

# @ = decorator: it associates the function under it to the specified rout. in this case the root URL '/'
@app.route('/')
def index():
    notes = cd.get_notes()
    return render_template('index.html', notes=notes)

# name class instance is used my flask to get resources, templates etc
if __name__ == '__main__': 
    app.run(debug=True)