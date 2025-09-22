
#regular expressions
import re

def extract_emails(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)

def extract_URLs(text):
    pattern = r'https:\/\/(?:[\w-]+\.)+[\w-]+(?:\/[^\s]*)?'

    return re.findall(pattern, text)

def extract_phoneNumbers(text):
    pattern = r'(\(\d{3}\)\s\d{3}-\d{4}|\d{3}[-.]\d{3}[-.]\d{4})'
    return re.findall(pattern, text)

def extract_creditCard_numbers(text):
    pattern = r'\d{4}(?:[ -])\d{4}(?:[ -])\d{4}(?:[ -])\d{4}'

    return re.findall(pattern, text)

files = ["test1.txt","test2.txt"]
for filename in files:
    print(f"\n...Extracting from {filename}...")
    with open(filename, "r") as f:
        data = f.read()

    emails = extract_emails(data)
    URLs = extract_URLs(data)
    phoneNumbers = extract_phoneNumbers(data)
    creditCardNumbers = extract_creditCard_numbers(data)

    print("Emails found:", emails)
    print("URLs found:", URLs)
    print("PhoneNumbers found:", phoneNumbers)
    print("CreditCards found:", creditCardNumbers)