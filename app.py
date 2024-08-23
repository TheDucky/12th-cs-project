from flask import Flask, render_template, request, redirect, url_for
from lib import ctrl_db as cd

# creating instance of Flask class
app = Flask(__name__) 

# @ = decorator: it associates the function under it to the specified rout. in this case the root URL '/'
@app.route('/', methods=('POST', 'GET'))
def index():

    if request.method == 'POST':
        title = request.form.get('title')
        note = request.form.get('note')
        cd.add_note(title, note)
        return redirect(url_for('index')) # used to clean the data already present in the form

    notes = cd.get_notes()
    return render_template('index.html', notes=notes)

@app.route('/<int:sno>/delete', methods=('POST', 'GET')) # sno passed into rout to determine which post to be deleted
def delete(sno):
    
    cd.delete_note(sno)
    return redirect(url_for('index'))

@app.route('/<int:sno>/vedit', methods=('POST', 'GET'))
def edit(sno):

    if request.method == 'POST':
        newnote = request.form.get('newnote')
        cd.edit_note(sno, newnote)
        return redirect(url_for('index'))
    
    return render_template('edit.html', note=cd.get_one_note(sno))

# name class instance is used my flask to get resources, templates etc
if __name__ == '__main__': 
    app.run(debug=True, host="0.0.0.0")