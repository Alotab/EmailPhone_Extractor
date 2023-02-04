import pyperclip, re


#Use thic clipboard text for testing our code
message = '''
Skip to main content

Enable accessibility for visually impaired

Open the accessibility menu
Accessibility Widget
This website uses cookies to improve your experience. Learn More
Got It
Skip to main content
Home
Search
Enter your keywords 
Catalog
Merchandise
Blog
Early Access
Write for Us
About Us
Contact Us
Topics
Art & Design
General Computing
Hacking & Computer Security
Hardware / DIY
Kids
LEGO®
Linux & BSD
Manga
Programming
Python
Science & Math
Scratch
System Administration
Early Access
FREE ebook edition with every print book purchased from nostarch.com!
+

EARLY ACCESS lets you read full chapters months before a title's release date!
Shopping cart
0 Items	Total: $0.00
User login
Log in
Create account
Contact Us
Reach Us by Email - email is the best way to reach us
Help with your order: support@nostarch.com
Academic requests: academic@nostarch.com (Further information)
Bulk and special sales questions: sales@nostarch.com
Conference and event inquiries: conferences@nostarch.com
Errata - please send any errata reports to: errata@nostarch.com
General inquiries: info@nostarch.com
Media requests: media@nostarch.com
Proposals or editorial inquiries: editors@nostarch.com
Rights inquiries: rights@nostarch.com
Reach Us by Mail
Our Mailing Address

No Starch Press
329 Primrose Road,  #42
Burlingame, CA 94010-4093
USA

Our Physical Address

No Starch Press, Inc.
245 8th Street
San Francisco, CA 94103
USA

NOTE: Below are our business phone numbers but we are a completely remote company. Please email support@nostarch.com with your questions and we will do our best to promptly resolve any issues that you may have.

Phone: 800.420.7240 or +1 415.863.9900
Fax: +1 415.863.9950

Reach Us on Social Media
Twitter Facebook Instagram Linkedin Pinterest

Navigation
My account
Want sweet deals?
Sign up for our newsletter.

About Us  |  Jobs!  |  Sales and Distribution  |  Rights  |  Media  |  Academic Requests  |  Conferences  |  FAQ  |  Contact Us  |  Write for Us  |  Privacy
Copyright 2023. No Starch Press, Inc

'''


#This module copy text from the clipboard 
pyperclip.copy(message)


#reges for the phone Numbers
phoneRegex = re.compile(r'''( 
    (\d{3}|\(\d{3}\))?                  # area code
    (\s|-|\.)?                          # separator
    (\d{3})                             # first 3 digits
    (\s|-|\.)?                          # separator
    (\d{4})                             # last 4 digits
    (\s*(ext|txt|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)


#regex for Email Address
emailRegex = re.compile(r'''( 
    [a-zA-Z0-9._%-]+            # username
    @                           # @ symbol
    [a-zA-Z0-9._%-]+            # domain name
    (\.[a-zA-Z]{2,4})           # dot-somethin
    )''', re.VERBOSE)


#find all matches in the clipboard text
text = str(pyperclip.paste())


matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)



for groups in emailRegex.findall(text):
    matches.append(groups[0])


#copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))

else:
    print('No phone numbers or email addresses found')