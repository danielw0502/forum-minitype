from flask import render_template, flash, redirect, url_for
from flask import Blueprint
from . import auth
from .forms import RegisterForm,LoginForm
from ..models import db,User,Post,Comment
from flask_login import login_user, logout_user, login_required
from flask import request


@auth.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()

    """
    if User.query.filter_by(username=form.name.data).first():
        flash('昵称已被用','warning')
    if User.query.filter_by(email=form.email.data).first():
        flash('邮箱已注册','warning')
    if form.password.data != form.password2.data:
        flash('密码输入不一致，请重新输入','warning')
    """

    if form.validate_on_submit():
        user = User(username=form.name.data,password=form.password.data,email=form.email.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.login'))
    return render_template('register.html',form=form)

@auth.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid email or password.','warning')
    return render_template('login.html',form=form)

@auth.route('/logout',methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))





