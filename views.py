from flask import Flask,render_template,redirect,url_for,request,session,abort
from .session_interface import MySessionInterface
app = Flask(__name__)
app.secret_key = b"?051kjajshdsd__"  #verileri imzaladıktan sonra şifrelemek için kullandık
app.session_interface = MySessionInterface() #kendi interfaceimizi belirttik
#kütüphaneleri import ettik ve
def get_current_username():
      Email = ""
      login_auth = False
      if 'Email' in session:
            Email = session['Email']  #email sessiona dahil etme gördüyse eğer true olur(doğru giriş)
            login_auth = True
      return Email, login_auth

@app.route("/")
def Index():
      Email, login_auth = get_current_username()  #kullanıcının giriş yaptığını bütün sayfalara bildirdik
      return render_template("index.html", Email=Email, login_auth=login_auth)

@app.route("/avantajlar")
def avantajlar():
      Email, login_auth = get_current_username()
      return render_template("features.html", Email=Email, login_auth=login_auth)


@app.route("/haberler")
def haberler():
      Email, login_auth = get_current_username()
      return render_template("news.html",Email=Email, login_auth=login_auth)

@app.route("/dahafazla")
def dahafazla():
      Email, login_auth = get_current_username()
      return render_template("post.html",Email=Email, login_auth=login_auth)

@app.route("/iletisim")
def iletisim():
      Email, login_auth = get_current_username()
      return render_template("contact.html",Email=Email, login_auth=login_auth)

#post ve get metodu ile formdan veri çekme ve gönderme işlemi 
@app.route("/giris", methods=['GET','POST'])
def giris():
      if request.method == 'POST':
            if request.form:
                  if 'Email' in request.form and 'password' == request.form:
                        Email = request.form['Email']
                        password = request.form['password']
                        if Email == 'kullanıcı' and password == 'sifre':
                              session['Email']=Email
                              return redirect(url_for('Index'))
                        else:
                              return redirect(url_for('giris'))
            abort(400)
#eğer kullanıcı giriş yaparsa ne olacak yapamazsa ne olacak diye belirledik.
      Email, login_auth = get_current_username()
      return render_template("login.html", Email = Email, login_auth=login_auth)
