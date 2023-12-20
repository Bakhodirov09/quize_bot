from main.models import *
from main.database_set import database
async def add_user(data: dict):
    try:
        query = users.insert().values(
            full_name=data["full_name"],
            language="uz",
            chat_id=data["chat_id"],
            phone_number=data["phone_number"],
            created_at=data["created"],
        )
        new_user = await database.execute(query=query)
        return new_user
    except Exception as exc:
        print(exc)
        return False

async def get_user(chat_id):
    try:
        query = users.select().where(users.c.chat_id==chat_id)
        user = await database.fetch_one(query=query)
        return user
    except Exception as exc:
        print(exc)
        return False

async def add_test(data: dict):
    try:
        query = tests.insert().values(
            title=data["test_nomi"],
            chat_id=data["chat_id"],
            created_at=data["sana"]
        ).returning(tests.c.id)
        new_test_id = await database.execute(query=query)
        return new_test_id
    except Exception as exc:
        return False

async def add_question(data: dict, message):
    try:
        query = questions.insert().values(
            test_id=data["test_id"],
            title=message.text,
            created_at=message.date
        ).returning(questions.c.id)
        new_question_id = await database.execute(query=query)
        return new_question_id
    except Exception as exc:
        return False

async def add_question_option(data: dict):
    try:
        query = question_answers.insert().values(
            question_id=data["question_id"],
            title=data["title"],
            created_at=data["created_at"]
        ).returning(question_answers.c.id)
        new_option_id = await database.execute(query=query)
        return new_option_id
    except Exception as exc:
        print(exc)
        return False
