****alu_regex-data-extraction-bendoujanna****

<br>

#**Project overview**

As software engineers, we have to be able to extract from a thousand of documents the exact data we need. 
This program read through files and extract data types using regular expressions.
For this assignment, I focused on five (5) data types:

-Email adresses

-URLs 

-Phone numbers in three formats

-Credit card numbers in two formats

-Hashtags

It's entirely built in **python** and does not need any external libraries apart from the standard "re" module (already imported in the main python file)

This is part of the Regex Onboarding Hackathon formative assignment at the African Leadership University. 
The task is to choose at least four data types, write regex patterns to match them, and then write a program that would read test files and extract the matching data.

<br>

##**How it works**

The script in the main file (main.py) does the three main things:

-Reads a list of text files 

-Applies five (5) regex based extractor functions, one for each data type

-Prints what it finds, or prints a message in case nothing is found

Each function return a list of matches. In the main loop, the script checks the lists and prints results.


<br>

###**Repository structure**

     /README.md          # the README file

     /main.py            # main script with the regex patterns 

     /test1.txt          # first test file with all types of data 

     /test2.txt          # second test file with one data type missing


<br>

####**Setup**

-Clone the repository

-Open a terminal in the folder 

   *Make sure all the files are in the same directory, then run "python main.py"
      
   *If you're using VS code or pyCharm, you can open the folder directly and run the "main.py" file

The script will read each file lsited in the "files" list.

<br>

   **Adding test files**
   
   You can add more filenames to this list if you create additional test files. 

   This is how the list currently looks:
   
        files = ['test1.txt', 'test2.txt']

   You can add more test files in this list if you create any. 
   
   The program will run automatically on each. Just make sure that they are in the same folder as main.py


<br>

#####**Regex patterns used**

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

5. Hashtags
   
   (?:^|\s)(#[A-Za-z0-9_]+)

Matches:

      #ThisIsAHashtag

      #example


<br>

######**Some output samples**

Below is a screenshot of the output.

<img width="1243" height="874" alt="Screenshot 2025-09-23 182005" src="https://github.com/user-attachments/assets/c172db4b-128d-4798-b042-0b53175abb04" />


 I also copied and pasted it in case the image won't be available. 


     ...Extracting from test1.txt...
     
     Emails found: ['user@example.com', 'firstname.lastname@company.co.uk', 'rfner.fj@earlyaid.com']
     
     URLs found: ['https://www.mefnuin.com', 'https://ingvneori.irnv.org/page']
     
     Phone numbers found: ['(123) 456-7890', '123-456-7890', '123.456.7890']
     
     Credit card numbers found: ['1234 5678 9012 3456', '1234-5678-9012-3456']
     
     Hashtags found: ['#regex_extraction']
     
     
     ...Extracting from test2.txt...
     
     Emails found: ['bendoujnna@gmail.com', 'info@travelagency.org', 'bookings.support@holiday-company.com']
     
     URLs found: ['https://flights.example.com/details', 'https://support.example.org/help/tickets.', 'https://support.client.org/help']
     
     Phone numbers found: ['(321) 654-9870', '321-654-9870', '321.654.9870', '(000) 000-0000']
     
     No Credit card numbers found
     
     Hashtags found: ['#hello', '#World', '#ThisIsATest']
     
     
     Process finished with exit code 0

     

#######**Limitations**

As you have read earlier, there are some formats the regular expressions won't match. Their aim is not to match all formats possible of emails, URLs, phone numbers, credit card numbers and hashtags.

They match only the formats I indicated above.

Please note that this is intentional and part of the assignment. 



<br>
<br>
<br>
<br>

**Regex Onboarding Hackathon assignment**

*Bendou Janna Vitalina Soeur*











