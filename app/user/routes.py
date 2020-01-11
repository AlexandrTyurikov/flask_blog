from flask import url_for, render_template, flash, request
from flask_login import current_user, login_user, login_required
# from app.user.forms import LoginForm
from werkzeug.utils import redirect

from app import db
from app.user import bp
from app.user.forms import RegistrationForm
from app.user.models import User


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
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
        return redirect(url_for('security.login'))
    return render_template('user/register.html', title='Register', form=form)


@bp.route('/detail/<username>')
@login_required
def user_detail(username):
    user = User.query.filter(User.user_name == username).first_or_404()
    # user = User.query.filter_by(user_name=username).first_or_404()
    return render_template('user/user_detail.html', user=user)


# @bp.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         email = request.form['email']
#         first_name = request.form['first_name']
#         last_name = request.form['last_name']
#         phone = request.form['phone']
#         password = request.form['password']
#
#         user = User(
#             user_name=username,
#             email=email,
#             first_name=first_name,
#             last_name=last_name,
#             phone=phone,
#             password=password
#         )
#
#         db.session.add(user)
#         db.session.commit()
#         return redirect(url_for('security.login'))
#
#     form = RegistrationForm()
#     return render_template('user/register.html', title='Register', form=form)


# @bp.route('/login', methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.username.data).first()
#         if user is None or not user.check_password(form.password.data):
#             flash('Invalid username or password')
#             return redirect(url_for('user_u.login'))
#         login_user(user, remember=form.remember_me.data)
#         return redirect(url_for('index'))
#     return render_template('user/login.html', title='Sign In', form=form)
