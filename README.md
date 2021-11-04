# Curriculum
- rule 1: type every line of code in a tutorial
    - it's all about practice
- rule 2: code every day
- rule 3: don't forget rule 2

## Python Basics
- get the basics down before you do anything
    - [Free Code Camp Intro Tutorial](https://www.youtube.com/watch?v=rfscVS0vtbw&ab_channel=freeCodeCamp.org)
- work with dictionaries and return the juice type from a function
    - dictionaries:
    ```py
    orange = {'name': 'orange', 'juice_type': 'orange juice'}
    apple = {'name': 'macintosh', 'juice_type': 'apple juice'}
    grape = {'name': 'grape', 'juice_type': 'grape juice'}
    rock = {'name': 'rock', 'juice_type': 'no juice'}
    ```
    - solution in Functions/functions1.py
- try to compute all the y values for x 1 to 100 using the following formula: y = 5 * x + 3
    - solution in Functions/function2.py
- make a Student class with the following characteristics
    - attributes: str: name, str: major, float: gpa, bool: is_on_probation
    -  fail_class method that decrements gpa by 1 (until a minimum gpa of 1) and puts the student on probation if his / her GPA falls below 2
    - pass_class method that increments gpa by 1 (until a maximum gpa of 2) and takes a student off of probation if his / her GPA is greater than 2
    - add a string property to the class with the following method:
    ```py

    def __repr__(self):
        string_value = f"{self.name} (Major: {self.major}; GPA: {self.gpa}; On Probation: {self.is_on_probation})"

        return string_value
    ```
    - solution in Classes/classesobjects.py

## Pandas - Fundamentals of Working with Data
- understand how to work with data (python's greatest advantage!)
    - [Corey Schafer Pandas Tutorial](https://www.youtube.com/watch?v=ZyhVh-qRZPA&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&ab_channel=CoreySchafer)
- test out your knowledge by printing all the emails in Pandas/emails.csv
    - solution in Pandas/printingemails.py

## Beautiful Soup - Intro to Web Scraping
- learn the basics of web scraping and interacting with websites
    - [Free Code Camp Beautiful Soup Tutorial](https://www.youtube.com/watch?v=XVv6mJpFOb0)
- get a professional grade understanding of practicing and using the library
    - [Corey Schafer Beautiful Soup Tutorial](https://www.youtube.com/watch?v=ng2o98k983k&t=2s)
- connect your scraping experience with pandas
    - convert BeautifulSoup/scrapeCoreysCSV.py to use pandas instead of the csv library (this may require some googling)
        - solution in BeautifulSoup/scrapeCoreyPandas.py
- understand modularity
    - build a function that takes a website as an argument and returns the title (in the `<title>` tag)
        - solution in BeautifulSoup/getTitle.py

## Selenium - Web Scraping and Automation
- learn how to webscrape using more complex automation tools
    - [Free Code Camp Selenium Tutorial](https://www.youtube.com/watch?v=j7VZsCCnptM&ab_channel=freeCodeCamp.org)
- interact with my website!
    - use a bot to do the following:
        - go to my website: https://entredeveloperslab.com
        - click the contact page (top right button)
        - send me a message with the form
    - solution in Selenium/browser_interactions.py
- make a Spotify Bot!
    - Bot Actions:
        - Open Spotify
        - Log In to Spotify (make username, password inputs for the user)
        - Click a Playlist (on the left)
        - Click Play
        - Sleep for 5 minutes with time.sleep(300) (leave the music playing on your computer)
        - Close the Bot

## Multithreading & Multiprocessing - Using the Full Machine
- understand a new code format
    - [Corey Schafer if __name__ == '__main__' Tutorial](https://www.youtube.com/watch?v=sugvnHA7ElY)
- threading allows you to run tasks while other tasks are waiting
    - [Corey Schafer Threading Tutorial](https://www.youtube.com/watch?v=IEEhzQoKtQU)
- multiprocessing allows multiple functions to run in parallel, allowing you to use the full resources of your computer
    - [Corey Schafer Multiprocessing Tutorial](https://www.youtube.com/watch?v=fKl2JW_qrso&t=313s)
