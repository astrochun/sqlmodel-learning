#!/usr/bin/env python

from sqlmodel_learning.db import SQLModel, engine


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db_and_tables()
