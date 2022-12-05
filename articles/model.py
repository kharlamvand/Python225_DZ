import pickle
import os.path


class Article:
    def __init__(self, title, ganr, producer, year, duration, studio, actors):
        self.title = title
        self.ganr = ganr
        self.producer = producer
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f"{self.title} - жанр ({self.ganr}) - режиссер ({self.producer})"


class ArticleModel:
    def __init__(self):
        self.db_name = 'move_catalog.txt'
        self.articles = self.load_data()  # {}

    def add_article(self, dict_article):
        article = Article(*dict_article.values())
        self.articles[article.title] = article

    def get_all_articles(self):
        return self.articles.values()

    def get_singe_article(self, user_title):
        article = self.articles[user_title]
        dict_article = {
            "название": article.title,
            "жанр": article.ganr,
            "режиссер": article.producer,
            "год выпуска": article.year,
            "длительность": article.duration,
            "студия": article.studio,
            "актеры": article.actors
        }
        return dict_article

    def remove_article(self, user_title):
        return self.articles.pop(user_title)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, 'rb') as f:
                return pickle.load(f)
        else:
            return dict()

    def save_data(self):
        with open(self.db_name, 'wb') as f:
            pickle.dump(self.articles, f)
