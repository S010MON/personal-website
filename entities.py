
class User:

    def __init__(self, user_id, first_name, last_name, birthday, email, phone):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.email = email
        self.phone = phone


class Film:

    def __init__(self, title, genre, year):
        self.title = title
        self.genre = genre
        self.year = year
