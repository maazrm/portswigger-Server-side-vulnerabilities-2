# portswigger-Server-side-vulnerabilities-2
Broken Access Control - Lab #2 Unprotected admin functionality with unpredictable URL

Lab 2 of server side vaulnerabilities

TASK:  This lab has an unprotected admin panel. It's located at an unpredictable location, but the location is disclosed somewhere in the application.
Solve the lab by accessing the admin panel, and using it to delete the user carlos. 

ANALYSIS: Here this web page has a unprotected admin panel but the link is unpredictable. The location of the panel is somewhere in the application we have to find it.

In this particular task it is in the source code itself


STEPS TO SOLVE

STEP 1: First check for robots.txt file. It is a file for search engine crawlers. (Not present)

STEP 2: look in the source code for any left over code that might help us
        Js script present that gives us the admin page url.


PYTHON SCRIPT

Now we write a python script that will go into the admin panel and delete carlos automatically

pseudo code
First we go into the home page and extract the cookies 
Second get the admin panel url from the js script
Third go into the admin panel and delete carlos

