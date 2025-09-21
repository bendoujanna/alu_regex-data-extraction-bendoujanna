

import re

def validate_email(text):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, text))

def validate_URL(text):
    pattern = r'^(https?:\/\/[\w\-]+(\.[\w\-]+)+[^\s]*?)(?=\s|$)'
    return bool(re.match(pattern, text))

def validate_phoneNumber(text):
    pattern = r'^(\(\d{3}\)|\d{3})[ .-]?\d{3}[ .-]?\d{4}$'
    return bool(re.match(pattern, text))

def validate_creditCard_number(text):
    pattern = r'^\d{4}([ -]?)\d{4}\1\d{4}\1\d{4}$'
    return bool(re.match(pattern, text))
