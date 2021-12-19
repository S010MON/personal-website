
class User:

    def __init__(self, user_id, first_name, last_name, date_of_birth, email, phone):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone = phone

    def to_dict(self):
        return {'user_id': self.user_id,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'date_of_birth': self.date_of_birth,
                'email': self.email,
                'phone': self.phone}


class Film:

    def __init__(self, title, genre, year):
        self.title = title
        self.genre = genre
        self.year = year

    def to_dict(self):
        return {'title': self.title,
                'genre': self.genre,
                'year': self.year}
