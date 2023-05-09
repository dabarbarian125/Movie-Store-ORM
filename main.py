#/usr/bin/python3
import os
from orm_utils import initialize, Actor, Film_Actor, Film, Film_Category, Category, Language
from sqlalchemy.sql import func



def heavenly_gun():
  return [x[0] for x in session.query(Actor.first_name + ' ' + Actor.last_name).filter(Film.film_id == Film_Actor.film_id, Actor.actor_id == Film_Actor.actor_id, Film.title == 'HEAVENLY GUN').all()]

def movie_count():
  return session.query(Actor.first_name + ' ' + Actor.last_name, func.count(Film_Actor.film_id)).filter(Actor.actor_id == Film_Actor.actor_id).group_by(Actor.actor_id).order_by(func.count(Film_Actor.film_id).desc()).all()

def anime_world():
  # print(session.query(Language.language_id, Language.name).all())
  test_2 = session.query(Category.category_id, Category.name, Film).filter(Category.category_id == Film_Category.category_id, Film_Category.film_id == Film.film_id).all()
  for id, category, film in test_2:
    if category == 'Animation':
      film.language_id = 3
  session.commit()
  print(session.query(Category.category_id, Category.name, Film.title, Language.name).filter(Category.category_id == Film_Category.category_id, Film_Category.film_id == Film.film_id, Film.language_id == Language.language_id, Film.language_id == 3).all())


# Initializer code
# if __name__ == '__main__':


def respawn():
  session,conn,metadata = initialize()
  


def reset_database():
  os.system('rm sqlite-sakila.db')
  os.system('cp backup/sqlite-sakila.db sqlite-sakila.db')
  os.system('chmod 774 /home/runner/Movie-Store-ORM/sqlite-sakila.db')
  # respawn()

reset_database()
session, conn, metadata = initialize()
print(f"Actors of Heavenly Gun: \n{heavenly_gun()}\n\n")
print(f"Total Amount of Movies for Each Actor: \n{movie_count()}\n\n")

