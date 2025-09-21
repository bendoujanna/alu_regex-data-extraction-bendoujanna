
#regular expressions
import re

def extract_emails(text):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.findall(pattern, text)

def extract_URLs(text):
    pattern = r'^https:\/\/([\w-]+\.)+[\w-]+(\/[^\s]*)?$'
    return re.findall(pattern, text)

def extract_phoneNumbers(text):
    pattern = r'^(\(\d{3}\)\s\d{3}-\d{4}|\d{3}[-.]\d{3}[-.]\d{4})$'
    return re.findall(pattern, text)

def extract_creditCard_numbers(text):
    pattern = r'^\d{4}([ -])\d{4}\1\d{4}\1\d{4}$'
    return re.findall(pattern, text)

