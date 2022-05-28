from sqlalchemy.exc import NoResultFound
from sqlmodel import Session, SQLModel, select

from .db import engine
from .models.hero import Hero


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_heroes():
    heroes = [
        Hero(name="Deadpond", secret_name="Dive Wilson"),
        Hero(name="Spider-Boy", secret_name="Pedro Parqueador"),
        Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48),
        Hero(name="Tarantula", secret_name="Natalia Roman-on", age=32),
        Hero(name="Black Lion", secret_name="Trevor Challa", age=35),
        Hero(name="Dr. Weird", secret_name="Steve Weird", age=36),
        Hero(
            name="Captain North America",
            secret_name="Esteban Rogelios",
            age=93,
        ),
    ]

    with Session(engine) as session:
        for h in heroes:
            try:
                record = select_hero(h.name)
                print(f"Record exists: {record}!")
            except NoResultFound:
                print(f"Adding: {h}")
                session.add(h)

        """
        print("After adding to the session")
        print("Hero 1:", hero_1)
        print("Hero 2:", hero_2)
        print("Hero 3:", hero_3)
        """

        session.commit()

        """
        print("After committing the session")
        print("Hero 1:", hero_1)
        print("Hero 2:", hero_2)
        print("Hero 3:", hero_3)

        print("After committing the session, show IDs")
        print("Hero 1 ID:", hero_1.id)
        print("Hero 2 ID:", hero_2.id)
        print("Hero 3 ID:", hero_3.id)

        print("After committing the session, show names")
        print("Hero 1 name:", hero_1.name)
        print("Hero 2 name:", hero_2.name)
        print("Hero 3 name:", hero_3.name)

        session.refresh(hero_1)
        session.refresh(hero_2)
        session.refresh(hero_3)

        print("After refreshing the heroes")
        print("Hero 1:", hero_1)
        print("Hero 2:", hero_2)
        print("Hero 3:", hero_3)
        """

    """
    print("After the session closes")
    print("Hero 1:", hero_1)
    print("Hero 2:", hero_2)
    print("Hero 3:", hero_3)
    """


def select_hero(name: str) -> Hero | None:
    with Session(engine) as session:
        hero = session.exec(select(Hero).where(Hero.name == name))
        if hero:
            return hero.one()


def main():
    create_db_and_tables()
    create_heroes()
