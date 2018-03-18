from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'ReadyPlayerOne'

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/dojo_survey', methods=['POST'])
def dojo_survey():
  name = request.form['name']
  location = request.form['location']
  language = request.form['language']
  comment = request.form['comment']
  if len(name) < 1:
    flash("Whoa! Name cannot be empty!")
    return redirect('/')
  if len(comment) < 1:
    flash("Whoa! Comment cannot be empty!")
    return redirect('/')
  elif len(comment) > 120:
    flash("Take it easy. No more than 120 characters please.")
    return redirect('/')

  return render_template("result.html", name2=name, location2=location, language2=language, comment2=comment)

app.run(debug=True) 