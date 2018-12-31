from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class RegisterForm(FlaskForm):
    name = StringField('昵称', validators=[DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,'用户名只能包含字母数字下划线')])
    email = StringField('邮箱', validators=[DataRequired(),Length(1, 64), Email()])
    password = PasswordField('密码',validators=[DataRequired(), EqualTo('password2', message='密码必须一致')])
    password2 = PasswordField('确认密码',validators=[DataRequired()])
    submit = SubmitField('注册')
    
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(message='邮箱已注册')
    
    def validate_name(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(message='昵称已被用')

class LoginForm(FlaskForm):
    email = StringField('登录邮箱', validators=[DataRequired()])
    password = StringField('登录密码',validators=[DataRequired()])
    remember_me = BooleanField('保持登录')
    submit = SubmitField('登录')