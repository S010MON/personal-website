from entities import User, Film


class Database:

    def __init__(self):
        self.users = []
        self.users.append(User(1, 'John', 'Doe', '01-01-1990', 'johndoe@gmail.com', '012345678'))
        self.users.append(User(2, 'Jane', 'Doe', '02-02-1991', 'janedoe@gmail.com', '012345678'))
        self.users.append(User(3, 'Barbara', 'Streisand', '03-03-1992', 'barbrastreisand@gmail.com', '012345678'))
        self.users.append(User(4, 'Ronald', 'McDonald', '04-04-1993', 'thehamburgerler@gmail.com', '012345678'))
        self.users.append(User(5, 'Barry', 'White', '05-05-1994', 'barryweight@gmail.com', '012345678'))

        self.films = []
        self.films.append(Film('Saving Ryan\'s Privates', 'action', 1998))
        self.films.append(Film('Fast 10: your seatbelts', 'action', 2021))
        self.films.append(Film('Raiders of the lost Arse', 'action', 1995))
        self.films.append(Film('The Porn Identity', 'comedy', 2011))
        self.films.append(Film('Good Will Humping', 'thriller', 1997))


def get_all_films(self):
    return self.films


def get_film_by_title(self, title):
    for film in self.films:
        if film.title == title:
            return film
    return None


def get_film_by_genre(self, genre):
    for film in self.films:
        if film.genre == genre:
            return film
    return None


def get_film_by_year(self, year):
    for film in self.films:
        if film.year == year:
            return film
    return None


def get_user_by_email(self, email):
    for user in self.users:
        if user.email == email:
            return user
    return None


def get_user_by_id(self, user_id):
    return self.users[user_id-1]


def add_user(self, first_name, last_name, birthday, email, phone):
    id = len(self.users)
    self.users.append(User(id, first_name, last_name, birthday, email, phone))