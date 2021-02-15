from flask import Flask, render_template, request
import requests
import smtplib

posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()
EMAIL = "ben@gmail.com"
PASSWORD = "Be1111bd4"
app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        data = request.form
        print(data['name'])
        print(data['email'])
        print(data['phone'])
        print(data['message'])
        return "<h1>Successfully sent your message</h1>"
    return render_template("contact.html", msg_false=False)

def send_mail(name, email, phone, message):
    email_message = f"Subject: New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(EMAIL, EMAIL, email_message)

if __name__ == "__main__":
    app.run(debug=True)
