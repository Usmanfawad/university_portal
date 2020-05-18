from portal import app
from flask import render_template,url_for,flash,redirect,request,abort,jsonify,send_from_directory
from flask_login import login_user,current_user,logout_user,login_required
from portal.forms import *
from functools import wraps
from flask import send_file

from portal import app,db,bcrypt,login_manager

from portal.models import *


def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            if ((current_user.role != role) and (role != "ANY")):
                print("HERE AGAIN")
                return redirect(url_for('unauthorized'))
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

@app.route('/unauthorized',methods=['GET','POST'])
def unauthorized():
    if current_user.role == 'ADMIN':
        page = 'admin_dashboard'
    elif current_user.role == 'USER':
        page = 'userManager'
    elif current_user.role == 'USER_DEPART_USER':
        page = 'userUser'
    elif current_user.role == 'TECH_DEPART_MANAGER':
        page = 'techManager'
    elif current_user.role == 'TECH_DEPART_TECH':
        page = 'techTech'
    return render_template('unauthorized.html',page=page)

@app.route('/',methods=['GET','POST'])
@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        if current_user.role == 'ADMIN':
            return redirect(url_for('admin_dashboard'))
        elif current_user.role == 'USER_DEPART_MANAGER':
            return redirect(url_for('userManager'))
        elif current_user.role == 'USER_DEPART_USER':
            return redirect(url_for('userUser'))
        elif current_user.role == 'TECH_DEPART_MANAGER':
            return redirect(url_for('techManager'))
        elif current_user.role == 'TECH_DEPART_TECH':
            return redirect(url_for('techTech'))
    form = LoginForm()
    if form.validate_on_submit():
        print("came here")
        user = Users.query.filter_by(email=form.email.data).first()

        # if bcrypt.check_password_hash(user.password,form.password.data):
        if user.password==form.password.data:
            login_user(user,remember=form.remember.data)
            if user.role == 'ADMIN':
                return redirect(url_for('admin_dashboard'))
            elif user.role == 'USER_DEPART_MANAGER':
                return redirect(url_for('userManager'))
            elif user.role == 'USER_DEPART_USER':
                return redirect(url_for('userUser'))
            elif user.role == 'TECH_DEPART_MANAGER':
                return redirect(url_for('techManager'))
            elif user.role == 'TECH_DEPART_TECH':
                return redirect(url_for('techTech'))

        else:
            flash('Incorrect Credentials. Please try again!','danger')

    return render_template('login.html',title="Login",form=form)


@app.route('/admin/dashboard',methods=['GET','POST'])
@login_required(role="ADMIN")
def admin_dashboard():
    title="Admin dasboard"
    return render_template("admin_dashboard.html" ,title=title)

