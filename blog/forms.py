from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import BooleanField, PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired("Required field!")]
    )
    password = PasswordField(
        "Password", validators=[DataRequired("Required field!")]
    )
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")


class PostForm(FlaskForm):
    title = StringField(
        "Title",
        validators=[
            DataRequired("Required field!"),
            Length(
                min=3,
                max=120,
                message="Make sure the title is between 3 and 120 characters.",
            ),
        ],
    )
    description = TextAreaField(
        "Description",
        validators=[
            Length(
                max=240,
                message="Make sure the description field is no longer than 240 characters.",
            )
        ],
    )
    body = TextAreaField("Content", validators=[DataRequired("Required field!")])
    image = FileField(
        "Cover Article", validators=[FileAllowed(["jpg", "jpeg", "png"])]
    )
    submit = SubmitField("Publish Post")
