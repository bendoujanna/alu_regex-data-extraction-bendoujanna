"""
That program is built to extract five data types among a thousand of data
    -emails
    -phone numbers
    -credit card numbers
    -URLs
    -Hashtags
"""
import re # Import the python 're' module to use regular expressions

# The functions below extracts the five data types chosen

def extract_emails(text):
    """
    Extract all emails found in a text and return a list of email addresses.
    Formats:
        -user@example.com
        -firstname.lastname@company.co.uk
    """
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)  # Return everything that matches the pattern

def extract_URLs(text):
    """
    Extracts all the HTTPS URLs found from a text
    Then returns a list of the URLs
    Formats:
        -https://www.example.com
        -https://subdomain.example.org/page
    """
    pattern = r'https:\/\/(?:[\w-]+\.)+[\w-]+(?:\/[^\s]*)?'
    return re.findall(pattern, text)

def extract_phoneNumbers(text):
    """
    Extracts all the phone numbers found in a text in the formats:
    (123) 456-7890
    123-456-7890
    123.456.7890
    Then returns a list of the phone numbers
    """
    pattern = r'(\(\d{3}\)\s\d{3}-\d{4}|\d{3}[-.]\d{3}[-.]\d{4})'
    return re.findall(pattern, text)

def extract_creditCard_numbers(text):
    """
    Extracts all the credit card numbers found in a text in the formats:
    1234 5678 9012 3456
    1234-5678-9012-3456
    Then returns a list of the credit card numbers

    """
    pattern = r'\d{4}(?:[ -])\d{4}(?:[ -])\d{4}(?:[ -])\d{4}'

    return re.findall(pattern, text)

def extract_hashtags(text):
    """
    Extracts all the hashtags found in a text in the formats:
    #ThisIsAHashtag
    #example
    Then returns a list of the hashtags
    """
    pattern = r'(?:^|\s)(#[A-Za-z0-9_]+)'
    return re.findall(pattern, text)


"""
The part below read the text files and extract the data types
"""

files = ["test1.txt","test2.txt"]  # List of text files to analyze
for filename in files:  # Loop through each file
    print(f"\n...Extracting from {filename}...\n")
    with open(filename, "r") as f:  # Open and read the file content
        datatype = f.read()

    # Apply the extraction functions to the file content
    emails = extract_emails(datatype)
    URLs = extract_URLs(datatype)
    phoneNumbers = extract_phoneNumbers(datatype)
    creditCardNumbers = extract_creditCard_numbers(datatype)
    hashtags = extract_hashtags(datatype)

    # For each data type, display the results or a message in case nothing is found
    if emails:
        print(f"Emails found: {emails}\n")
    else:
        print("No emails found\n")
    if URLs:
        print(f"URLs found: {URLs}\n")
    else:
        print("No URLs found\n")
    if phoneNumbers:
        print(f"Phone numbers found: {phoneNumbers}\n")
    else:
        print("No Phone numbers found\n")
    if creditCardNumbers:
        print(f"Credit card numbers found: {creditCardNumbers}\n")
    else:
        print("No Credit card numbers found\n")
    if hashtags:
        print(f"Hashtags found: {hashtags}\n")
    else:
        print("No Hashtags found\n")