from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from encrypt import *
 
# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class ReusableForm(Form):
    message = TextField('Message:', validators=[validators.required()])
    key = TextField('Key:', validators=[validators.required()])

    def reset(self):
        blankData = MultiDict([ ('csrf', self.reset_csrf() ) ])
        self.process(blankData)
 
 
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
 
    print(form.errors)
    if request.method == 'POST':
        message = request.form['message']
        key_input = request.form['key']
        direction = request.form['options']

        key = key_formatter(key_input)

        print(message)
        print(key)
 
        if form.validate():
            if not is_invertible(key):
                flash('Error: {} is not is_invertible.'.format(str(key)))
            elif direction == 'encrypt':
                flash(encryptor(message, key))
            elif direction == 'decrypt':
                flash(decryptor(message, key))
        else:
            flash('Error: All the form fields are required.')
 
    return render_template('form.html', form=form)
 
if __name__ == "__main__":
    app.run()