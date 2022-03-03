from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys

sad_words = ['sad', 'depressed', 'unhappy',
             'miserable', 'angry', 'depressing', 'annoyed']

starter_encouragements = ["Cheer Up!",
                          'Hang in there.', "You are a great person / bot!"]

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bot.db'

db = SQLAlchemy(app)


class PromptGroupModel(db.Model):
    __tablename__ = 'prompt_groups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False, unique=True)

    # link responses
    prompts = db.relationship(
        'PromptModel', backref='prompt_group', lazy='dynamic')


class PromptModel(db.Model):
    __tablename__ = 'prompts'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(140), nullable=False)

    # link group id
    prompt_group_id = db.Column(db.Integer, db.ForeignKey(
        'prompt_groups.id'), nullable=False)


class ResponseGroupModel(db.Model):
    __tablename__ = 'response_groups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False, unique=True)

    # link responses
    responses = db.relationship(
        'ResponseModel', backref='response_group', lazy='dynamic')


class ResponseModel(db.Model):
    __tablename__ = 'responses'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(140), nullable=False)

    # link group id
    response_group_id = db.Column(db.Integer, db.ForeignKey(
        'response_groups.id'), nullable=False)


class ConfigModel(db.Model):
    __tablename__ = 'configs'
    id = db.Column(db.Integer, primary_key=True)

    key = db.Column(db.String(20), nullable=False)
    value = db.Column(db.Boolean, default=False)


def setup():
    # create all tables
    db.create_all()

    # create a responding key
    new_key = ConfigModel(key='responding')
    db.session.add(new_key)

    # create prompt group
    prompt_group = PromptGroupModel(name='sad')
    db.session.add(prompt_group)
    db.session.commit()

    # add prompts
    for word in sad_words:
        new_prompt = PromptModel(text=word, prompt_group_id=prompt_group.id)
        db.session.add(new_prompt)

    # create response group
    response_group = ResponseGroupModel(name='encouragements')
    db.session.add(response_group)
    db.session.commit()

    # add responses
    for encouragement in starter_encouragements:
        new_encouragement = ResponseModel(
            text=encouragement, response_group_id=response_group.id)
        db.session.add(new_encouragement)

    # commit the whole new database (nobody else is going to be using it)
    db.session.commit()


# set tup the model when running
if __name__ == '__main__':
    if sys.argv[1] == 'reset':
        db.drop_all()
        setup()
