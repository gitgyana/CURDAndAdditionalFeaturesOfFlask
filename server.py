from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route('/login')
def admin():
    return render_template('index.html')

# Accessing Form Data with flask.request.form (also check the index.html)
@app.route('/admin', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # process login here
    if username == 'kali':
        if password == 'kali':
            return {"message": "Good"}
        else:
            return {"message": "Invalid Password"}
    else:
        return {"message": "Invalid Username"}


@app.errorhandler(405)
def api_not_found(error):
    return {"message": "admin request without credentials is prohibited"}, 405

# Redirecting to a URL with flask.redirect
@app.route('/')
def redirecting():
    return redirect('/login')

# Generating Dynamic URLs with flask.url_for
@app.route('/signin')
def signin():
    return redirect(url_for('signin_page'))


@app.route('/signin_page')
def signin_page():
    return render_template('index.html')
