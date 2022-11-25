import db


def get_appeals(user_id: int) -> str:
    """Return all user appeals"""
    cursor = db.get_cursor()
    cursor.execute(f"SELECT *"
                   f"FROM appeal WHERE customer={user_id}")
    result = cursor.fetchone()
    if not result[0]:
        return ("У вас ещё не было заявлений\n"
                "Отправить заявления: /create_appel\n")
    return result
