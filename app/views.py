from app import application
from flask import render_template
from .forms import EncipherForm
from widgets.cipher import encipher

@application.route('/', methods=['GET','POST'])
@application.route('/index', methods=['GET', 'POST'])
def index():
    form = EncipherForm()
    enciphered_text = None
    if form.validate_on_submit():
        enciphered_text = encipher(str(form.input_text.data), int(form.numRotations.data))
    return render_template('index.html',
                           form=form,
                           enciphered_text=enciphered_text)
