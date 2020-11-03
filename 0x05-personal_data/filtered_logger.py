#!/usr/bin/env python3
"""
    Personal data
"""
import re
from typing import List


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
