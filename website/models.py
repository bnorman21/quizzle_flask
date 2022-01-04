from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    #one to many relationship
    #when linking the foreign key, remeber it is lower case
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quiz_name = db.Column(db.String(150))
    quiz_category = db.Column(db.String(150))
    #many quizzes to one relationship
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #one quiz to many relationship
    questions = db.relationship('Question')
    question_scores = db.relationship('QuestionScore')
    quiz_scores = db.relationship('QuizScore')

class QuizScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    result = db.Column(db.Float)
    #many quiz socres to one relationship
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prompt = db.Column(db.String(150))
    #starting with hardcoding four option then will work on implementing an array
    option1 = db.Column(db.String(150))
    option2 = db.Column(db.String(150))
    option3 = db.Column(db.String(150))
    option4 = db.Column(db.String(150))
    correct_option = db.Column(db.String(150))
    #many questions to one relationship
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #one question to many relationship
    question_scores = db.relationship('QuestionScore')

class QuestionScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    correct = db.Column(db.Boolean)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    



class User(db.Model, UserMixin):
    #need primary key
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    #when you are creating the relationship, you state the name of the class
    notes = db.relationship('Note')
    quizzes = db.relationship('Quiz')
    quiz_scores = db.relationship('QuizScore')
    questions = db.relationship('Question')
    question_scores = db.relationship('QuestionScore')