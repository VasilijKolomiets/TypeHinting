from typing import Protocol

from datetime import datetime
from pathlib import Path

import sqlite3


class SimpleLogger(Protocol):
    """Interface for any storage logging text"""

    def __init__(self, file: Path) -> None:
        raise NotImplementedError

    def save(self, text: str) -> None:
        """Log the date and text."""
        raise NotImplementedError


class LoggerInitOnly:
    """For common __init__ sharing by inherit."""

    def __init__(self, file: Path):
        self._file = file
        self._now = datetime.now()
        self._text = ""


class PlainFileLogger(LoggerInitOnly):
    """Logging text in tab-delimitered text file."""

    def save(self, text) -> None:
        """Save to the _file."""
        self._text = text[:2048]
        with open(self._file, "a", encoding="UTF-8") as f:
            f.write(f"{self._now}\t{self._text}\n")  #  look at `\t` !!!


class SQLiteFileLogger(LoggerInitOnly):
    """Logging text in SQLite file."""

    def __init__(self, file: Path):
        super().__init__(file)
        self._create_table_if_not_exists()

    def _create_table_if_not_exists(self) -> None:
        """Create the table if it does not exist."""
        with sqlite3.connect(self._file) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS text_logging (
                    datetime TEXT NOT NULL,
                    text TEXT NOT NULL CHECK(length(text) <= 2048)
                )
            """)
            conn.commit()

    def save(self, text: str) -> None:
        """Save to the SQLite file."""
        self._text = text[:2048]
        with sqlite3.connect(self._file) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO text_logging (datetime, text)
                VALUES (?, ?)
            """,
                (self._now.isoformat(), self._text),
            )
            conn.commit()


def log_it(text: str, logger: SimpleLogger) -> None:
    """Log text into the storage"""
    logger.save(text)
