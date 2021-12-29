from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class RegisterForm(FlaskForm):
    name = StringField('Enter your Name', validators=[DataRequired()])
    email = StringField('Enter your Email', validators=[DataRequired()] )
    password = StringField('Enter your Password', validators=[DataRequired()])
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):

    email = StringField('Enter your Email', validators=[DataRequired()] )
    password = PasswordField('Enter your Password', validators=[DataRequired()])
    submit = SubmitField("Log in")

class CommentsForm(FlaskForm):
    comment_text = CKEditorField("comment", validators=[DataRequired()])
    submit = SubmitField("Comment")
