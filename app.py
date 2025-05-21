from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flashing success messages

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")


mail = Mail(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        msg = Message("New Contact Form Submission",
                      sender=email,
                      recipients=["runnelsdb@gmail.com"])  # Your Gmail again

        msg.body = f"From: {name}\nEmail: {email}\n\n{message}"
        mail.send(msg)

        flash("Message sent successfully!")
        return redirect(url_for("contact"))

    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

@app.route("/shop")
def shop():
    return render_template("shop.html")

if __name__ == "__main__":
    app.run(debug=True)


