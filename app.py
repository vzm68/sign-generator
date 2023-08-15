#############################################
# Mail Sign Generator
# Was created: 11.08.2023
# Beta version: 0.0.1
#############################################
from flask import Flask, render_template
from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import InputRequired
from string import Template

#from os import remove

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'


class InputForm(FlaskForm):                  # Determine the form
    full_name = StringField('Full Name:', validators=[InputRequired()])
    job_title = StringField('Job Title:', validators=[InputRequired()])
    email = EmailField('Email:', validators=[InputRequired()])
    phone = StringField('Phone:', validators=[InputRequired()])
    submit = SubmitField('Generate Sign')


def clean(filename):
    pass
    #remove("templates/results/filename")


@app.route('/', methods=['GET', 'POST'])
def index():Ну
    form = InputForm()
    if form.validate_on_submit():             # Get variable by input form
        full_name = form.full_name.data
        job_title = form.job_title.data
        email = form.email.data
        phone = form.phone.data

        with open('sign.html', 'r') as file:  # Open template, save it after edit by name and open generated file
            temp = Template(file.read())
            with open(f'templates/results/{full_name}.html', "w") as result:
                result.write(
                    temp.substitute(FULL_NAME=full_name, JOB_TITLE=job_title, USER_EMAIL=email, USER_PHONE=phone))
            return render_template(f"results/{full_name}.html")

    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
