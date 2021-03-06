from sqlmodel import SQLModel, create_engine  # noqa: F401

from .models import hero  # noqa: F401

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)
