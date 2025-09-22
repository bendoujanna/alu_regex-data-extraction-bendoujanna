**alu_regex-data-extraction-bendoujanna**



**Project overview**

As software engineers, we have to be able to extract from a thousand of documents the exact data that we need. 
This program read through files and extract data types using regular expressions.
For this assignment, I focused on four data types:
-Email adresses
-URLs 
-Phone numbers in three formats
-Credit card numbers in two formats

It's entirely built in **python** and does not need any external libraries apart from the standard "re" module (already imported in the main python file)

This is part of the Regex Onboarding Hackathon formative assignment at ALU, the African Leadership University. 
The task is to choose at least four data types, write regex patterns to match them, and then write a program that would read test files and extract the matching data.



**How it works**

The script in the main file (main.py) does the three main things:

-Reads a list of text files 

-Applies four regex based extractor functions, one for each data type

-Prints what it finds, or prints a message in case nothing is found

Each function return a list of matches. In the main loop, the script checks the lists and prints results neatly.



**Repository structure**

/README.md          # the README. file

/main.py            # main script with the regex patterns 

/test1.txt          # first test file with all types of data 

/test2.txt          # second test file with one data type missing



**Setup**

-Clone the repository

-Open a terminal in the folder 

      *Make sure all the files are in the same directory, then run "python main.py"
      
      *If you're using VS code or pyCharm, you can open the folder directly and run the "main.py" file

The script will read each file lsited in the "files" list.
You can add more filenames to this list if you create additional test files. 
The program will run automatically on each. Just make sure that they are in the same folder as main.py



**Regex patterns used**

1. Email adresses
   
  [a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}

Matches:

-user@example.com

-firstname.lastname@company.co.uk

It does not match invalid email adresses

2. URLs
   
   https:\/\/(?:[\w-]+\.)+[\w-]+(?:\/[^\s]*)?
   
Matches:

-https://www.example.com

-https://subdomain.example.org/page

It does not match http or any other type of url.

3. Phone numbers
   
   \(\d{3}\)\s\d{3}-\d{4}|\d{3}[-.]\d{3}[-.]\d{4}
   
Matches:

 (123) 456-7890
 
 123-456-7890
 
 123.456.7890
 
It does not match any other format.

4. Credit card numbers
   
   \d{4}(?:[ -])\d{4}(?:[ -])\d{4}(?:[ -])\d{4}
   
Matches:

 1234 5678 9012 3456
 
 1234-5678-9012-3456
 
It does not match any other format.



**Some output samples**

Below is a screenshot of the output. I also copied and pasted it in case the image won't be available. 

<img width="1469" height="811" alt="Screenshot 2025-09-22 232904" src="https://github.com/user-attachments/assets/5cbdf402-a48f-4dd6-a269-1e3acc5e58da" />

C:\Users\Admin\anaconda3\python.exe C:\Users\Admin\PycharmProjects\alu_regex-data-extraction-bendoujanna\main.py 

...Extracting from test1.txt...

Emails found: ['user@example.com', 'firstname.lastname@company.co.uk', 'rfner.fj@earlyaid.com']

URLs found: ['https://www.mefnuin.com', 'https://ingvneori.irnv.org/page']

Phone numbers found: ['(123) 456-7890', '123-456-7890', '123.456.7890']

Credit card numbers found: ['1234 5678 9012 3456', '1234-5678-9012-3456']


...Extracting from test2.txt...

Emails found: ['bendoujnna@gmail.com', 'info@travelagency.org', 'bookings.support@holiday-company.com']

URLs found: ['https://flights.example.com/details', 'https://support.example.org/help/tickets.', 'https://support.client.org/help']

Phone numbers found: ['(321) 654-9870', '321-654-9870', '321.654.9870', '(000) 000-0000']

No Credit card numbers found


Process finished with exit code 0








