from flask import Flask,request,flash,render_template
from flask_mail import Mail,Message

app =Flask(__name__)
app.secret_key="123"

@app.route("/")
def home():
   return render_template('index.html')

@app.route("/about")
def about():
   return render_template('about.html')

@app.route("/resume")
def resume():
   return render_template('resume.html')

@app.route("/contact",methods=["POST","GET"])
def contact():
   if request.method=="POST":
      fmail=request.form.get('fmail')
      tmail = request.form.get('tmail')
      fpwd = request.form.get('fpwd')
      message = request.form.get('message')
      body = request.form.get('body')

      app.config['MAIL_SERVER']='smtp.gmail.com'
      app.config['MAIL_PORT']=465
      app.config['MAIL_USERNAME']=fmail
      app.config['MAIL_PASSWORD']=fpwd
      app.config['MAIL_USE_TLS']=False
      app.config['MAIL_USE_SSL']=True

      mail = Mail(app)

      msg=Message(message,sender=fmail,recipients=[tmail])
      msg.body=body
      mail.send(msg)
      flash("Mail Sented Successfully", 'success')
   return render_template('contact.html')

if __name__ == '__main__':
   app.run(debug = True)
