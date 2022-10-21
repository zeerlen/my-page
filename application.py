from flask import Flask, render_template, redirect, request, flash
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

load_dotenv()

application = Flask(__name__)

SECRET_KEY = os.urandom(32)
application.secret_key = SECRET_KEY

mail_settings = {
    "MAIL_SERVER": 'smtp.mailtrap.io',
    "MAIL_PORT": 2525,
    "MAIL_USE_TLS": True,
    "MAIL_USE_SSL": False,
    "MAIL_USERNAME": os.getenv("MAIL"),
    "MAIL_PASSWORD": os.getenv("PASSWORD")
}

application.config.update(mail_settings)
mail = Mail(application)

class Contact:
    def __init__(self, name, email, message):
        self.name = name
        self.email = email
        self.message = message

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        contactForm = Contact(
            request.form["name"],
            request.form["email"],
            request.form["message"]
        )

        msg = Message(
            subject = f'{contactForm.name} lhe enviou uma mensagem no Portifólio!',
            sender = application.config.get("MAIL_USERNAME"),
            recipients= ['alen.iuri@gmail.com', application.config.get("MAIL_USERNAME")],
            body = f'''
            
            {contactForm.name} com e-mail <{contactForm.email}> lhe enviou a seguinte mensagem:
            {contactForm.message}
            '''
        )

        mail.send(msg)
        flash('Mensagem enviada com sucesso!')
    return redirect('/')

if __name__ == '__main__':
    application.run(debug=True)