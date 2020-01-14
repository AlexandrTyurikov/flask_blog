from flask import url_for, render_template, flash, request, redirect
from flask_login import current_user, login_user, login_required
from werkzeug.urls import url_parse
# from werkzeug.utils import redirect

from app import db
from app.user import bp
from app.user.forms import RegistrationForm, LoginForm, EditProfileForm
from app.user.models import User


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('posts.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(user_name=form.username.data,
                    email=form.email.data,
                    first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    phone=form.phone.data,
                    password=form.password.data
                    )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('user_u.login'))
    return render_template('user/register.html', title='Register', form=form)


@bp.route('/detail/<username>')
@login_required
def user_detail(username):
    user = User.query.filter(User.user_name == username).first_or_404()
    return render_template('user/user_detail.html', user=user)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('posts.index'))
    form = LoginForm()
    if form.validate_on_submit():
        # user = User.query.filter_by(username=form.username.data).first()
        user = User.query.filter_by(email=form.email.data).first_or_404()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('posts.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('posts.index')
        return redirect(next_page)
    return render_template('user/login.html', title='Sign In', form=form)


@bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.user_name)
    if form.validate_on_submit():
        current_user.user_name = form.username.data
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.phone = form.phone.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('user_u.edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.user_name
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.phone.data = current_user.phone
    return render_template('user/edit_profile.html', title='Edit Profile',
                           form=form)
