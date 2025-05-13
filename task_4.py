# Класс User
class User:
    def __init__(self, username: str, email: str, age: int):
        self.username = username
        self.email = email
        self.age = age

    def __str__(self):
        return f"User(username='{self.username}', email='{self.email}', age={self.age})"

# Класс UserManager
class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, user: User):
        if user.username in self.users:
            raise UserAlreadyExistsError(user.username)
        self.users[user.username] = user

    def remove_user(self, username: str):
        if username not in self.users:
            raise UserNotFoundError(username)
        del self.users[username]

    def find_user(self, username: str) -> User:
        if username not in self.users:
            raise UserNotFoundError(username)
        return self.users[username]

# Пользовательские исключения
class UserAlreadyExistsError(Exception):
    """Исключение, если пользователь уже существует."""
    def __init__(self, username):
        self.username = username
        super().__init__(f"Пользователь '{username}' уже существует.")

class UserNotFoundError(Exception):
    """Исключение, если пользователь не найден."""
    def __init__(self, username):
        self.username = username
        super().__init__(f"Пользователь '{username}' не найден.")


if __name__ == "__main__":
    manager = UserManager()

    users_to_add = [
        User("Алиса", "alice@example.com", 30),
        User("Миша", "mike@example.com", 25),
        User("Алиса", "alisa@example.com", 28),  # Дубликат имени
    ]

    # Попытка добавления пользователей
    for user in users_to_add:
        try:
            manager.add_user(user)
            print(f"Пользователь добавлен: {user}")
        except UserAlreadyExistsError as e:
            print(f"Ошибка добавления: {e}")

    # Попытка удаления пользователей
    usernames_to_remove = ["Миша", "Костя"]  # Костя не существует
    for username in usernames_to_remove:
        try:
            manager.remove_user(username)
            print(f"Пользователь '{username}' удален.")
        except UserNotFoundError as e:
            print(f"Ошибка удаления: {e}")

    # Попытка найти пользователей
    usernames_to_find = ["Алиса", "Дима"]  # Дима не существует
    for username in usernames_to_find:
        try:
            user = manager.find_user(username)
            print(f"Найден пользователь: {user}")
        except UserNotFoundError as e:
            print(f"Ошибка поиска: {e}")
