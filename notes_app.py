
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request

app = Flask(__name__)

notes = []

@app.route('/')
@app.route('/notes', methods=['GET'])
def get_notes():
    message=""
    return render_template("notes.html", message=message)

@app.route('/notes', methods=['POST'])
def post_notes():
    message="Note = '" +request.form.get("note") + "'"
    note = request.form.get("note")
    if note != None and note != "" and not (note in notes):
        notes.append(note)
    return render_template("notes.html", message=message)