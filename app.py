from flask import Flask,request,redirect,render_template,session,Response,url_for,flash

app=Flask(__name__)
app.secret_key='superkey'
@app.route("/")
def Home():
    return render_template('home.html')


@app.route("/login",methods=['GET','POST'])
def login():
    
    if request.method=='POST':
        username=request.form['name']
        password=request.form['password']
        
        
        if username=='admin' and password=="123":
            session['user']=username
            return redirect(url_for("welcome")) 
        
        else:
            return Response("wrong credentials",mimetype="text/plain")
        
    return render_template("login.html")


@app.route("/welcome")
def welcome ():
    if "user" in session:
        return f'''
    <h2>welcome {session['user']}</h2>
    <a href="{ url_for('logout') }">Logout</a>'''
    return redirect(url_for('login'))



@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect(url_for('login'))




if __name__=="__main__":
    app.run(debug=True)