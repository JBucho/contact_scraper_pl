# Simple App to scrap phone numbers and email addresses from copied text.

import re
import pyperclip


def extract_phones(text):
    """
    Extracts phone numbers matching regex pattern from text.

    :param text: string -> text to extract from
    :return: list -> all phone numbers extracted from string
    """
    # Regex pattern for phone numbers (PL numbers)
    phone_regex = re.compile(
        r"""
    # +48 555 000 000, 555-000-000, (+48) 555-000-000, (+48) 555 000 000, 048 555-000-000, 048555000555,
    # +48555000555, 555000555
    (
    ( \+\d{2} | \(\+\d{2}\) )?      # directional (optional)
    ((\s|-)?\d{3}){3}               # 9 digits with separators
    )
    """,
        re.VERBOSE,
    )

    # Extract phone numbers from given text
    extracted_phone = phone_regex.findall(text)

    all_phone_numbers = []
    for number in extracted_phone:
        all_phone_numbers.append(number[0])

    return all_phone_numbers


def extract_emails(text):
    """
    Extracts email addresses matching regex pattern from text.
    :param text: string -> text to extract from
    :return: list -> email addresses
    """
    # Regex pattern for email addresses
    email_regex = re.compile(
        r"""
    # some.+_thing@some.+_thing.com
    
    [a-zA-Z0-9_.+]+         # name part
    @                       # @ symbol
    [a-zA-Z0-9_.+]+         # domain name part
    """,
        re.VERBOSE,
    )

    # Extract email addresses from given text
    extracted_emails = email_regex.findall(text)

    return extracted_emails


def to_string(phones, emails):
    """
    Converts lists of phone numbers and email addresses to multi-line string.
    :param phones: list -> phone numbers
    :param emails: list -> email addresses
    :return: string -> all phone numbers and email addresses
    """
    results = "\n".join(phones) + "\n" + "\n".join(emails)

    return results


if __name__ == "__main__":

    # Get the text off the clipboard
    source = pyperclip.paste()

    # Extract phone numbers
    phone_numbers = extract_phones(source)

    # Extract emails
    email_addresses = extract_emails(source)

    # Copy results to clipboard
    pyperclip.copy(to_string(phone_numbers, email_addresses))
