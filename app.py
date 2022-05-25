#!/usr/bin/env python

from sqlmodel import Session
from sqlmodel_learning.db import SQLModel, engine
from sqlmodel_learning.models.hero import Hero


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_heroes():
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

    session = Session(engine)

    session.add(hero_1)
    session.add(hero_2)
    session.add(hero_3)

    session.commit()

    session.close()


def main():
    create_db_and_tables()
    create_heroes()


if __name__ == "__main__":
    main()
