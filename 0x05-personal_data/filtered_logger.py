#!/usr/bin/env python3
""" Personal data.
"""
import logging
import mysql.connector
import re
import os
from typing import List

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Function to hide personal data.
        Args:
            fields: a list of strings.
            redaction: a string representing by what the
                       field will be obfuscated.
            message: a string representing the log line.
            separator: a string representing by which character
                       is separating all fields in the log line.
        Return:
            The log message obfuscated.
    """
    for i in fields:
        message = re.sub(r"{}=(.*?){}".format(i, separator),
                         f'{i}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Initializer.
            Arg:
                fields: a list of strings.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Format method.
            Arg:
                record: records of filter_datum function.
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def get_logger() -> logging.Logger:
    """ Function that stock log(logger), logger information gathering(handler)
        and formatted forwarding(formatter).
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Function that connect to secure database.
        Return:
            A connector to the database.
    """
    return mysql.connector.connect(
        host=os.getenv('PERSONAL_DATA_DB_HOST'),
        database=os.getenv('PERSONAL_DATA_DB_NAME'),
        user=os.getenv('PERSONAL_DATA_DB_USERNAME'),
        password=os.getenv('PERSONAL_DATA_DB_PASSWORD')
    )


def main():
    """ Function that database connection using get_db and
        retrieve all rows in the users table.
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")


if __name__ == "__main__":
    main()
