import sqlalchemy
from sqlalchemy import DateTime
from main.database_set import metadata

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("full_name", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("language", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("chat_id", sqlalchemy.BigInteger),
    sqlalchemy.Column("phone_number", sqlalchemy.String),
    sqlalchemy.Column('created_at', DateTime(timezone=True), nullable=True)
)

tests = sqlalchemy.Table(
    "tests1",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String),
    sqlalchemy.Column("chat_id", sqlalchemy.BigInteger),
    sqlalchemy.Column('created_at', DateTime(timezone=True), nullable=True)
)

questions = sqlalchemy.Table(
    "questions",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String),
    sqlalchemy.Column("test_id", sqlalchemy.BigInteger),
    sqlalchemy.Column('created_at', DateTime(timezone=True), nullable=True)
)

question_answers = sqlalchemy.Table(
    "question_answers1",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("question_id", sqlalchemy.Integer),
    sqlalchemy.Column("title", sqlalchemy.String),
    sqlalchemy.Column("is_true", sqlalchemy.Boolean),
    sqlalchemy.Column('created_at', DateTime(timezone=True), nullable=True)
)
