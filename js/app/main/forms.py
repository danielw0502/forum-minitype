from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


## post form
class PostForm(FlaskForm):
    title = StringField('标题',validators=[DataRequired()])
    body = StringField('内容',validators=[DataRequired()])
    submit = SubmitField('提交')


## comment form
class CommentForm(FlaskForm):
    body = StringField('输入评论',validators=[DataRequired()])
    submit = SubmitField('提交')