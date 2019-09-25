from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, RadioField
from wtforms.validators import Required
class PitchForm(FlaskForm):
   title = StringField('Pitch title',validators=[Required()])
   description = TextAreaField('Pitch Description', validators=[Required()]) 
   category = RadioField('Label', choices=[ ('Cute','Cute'), ('Funny','Funny'),('Inspirational','Inspirational'),('Love','Love')],validators=[Required()])
   submit = SubmitField('Submit')
class UpdateProfile(FlaskForm):
   bio = TextAreaField('Tell us about you.',validators = [Required()])
   submit = SubmitField('Submit')

class CommentForm(FlaskForm):
	description = TextAreaField('',validators=[Required()])
	submit = SubmitField()

class UpvoteForm(FlaskForm):
	submit = SubmitField()

class Downvote(FlaskForm):
	submit = SubmitField()

