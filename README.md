# Curriculum
- rule 1: type every line of code in a tutorial
    - it's all about practice
- rule 2: code every day
- rule 3: don't forget rule 2

## Python Basics
- get the basics down before you do anything
    - [Free Code Camp Intro Tutorial](https://www.youtube.com/watch?v=rfscVS0vtbw&ab_channel=freeCodeCamp.org)
- reference for basic python concepts: [Corey Schafer Python Beginner Concepts Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7)
    - note: you can do all of these for an in-depth understanding of them
    - much of this information will be picked up along your programming career, so I would not expect everyone to focus on learning it early on as it is quite dry
- work with dictionaries and return the juice type from a function
    - review functions: [Corey Schafer Functions Tutorial](https://www.youtube.com/watch?v=9Os0o3wzS_I)
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
    - any basic understanding of data requires an undestanding of lists
        - [Corey Schafer Lists Tutorial](https://www.youtube.com/watch?v=W8KRzm-HUcc&ab_channel=CoreySchafer)
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
- learn how to webscrape and automate using more complex automation tools
    - [Frank Andrade Selenium Tutorial](https://www.youtube.com/watch?v=UOsRrxMKJYk&ab_channel=FrankAndrade)
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
    - solution in Selenium/spotify_script.py

## Learn about Classes
- learn about classes
    - [Corey Schafer Classes Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc)
- object orient your Spotify Bot
    - data members (in init)
        - in init, make self.driver
    - make a bot class with the following functions
        - login
            - takes a self, username, and password argument
        - play playlist
            - takes a self, playlist url argument
        - close
            - takes a self argument
    - use the class to do the same task (play a playlist)
- integrate pandas with your Spotify Bot (review the pandas tutorials if necessary)
    - play 10 playlists from a csv

## Multithreading & Multiprocessing - Using the Full Machine
- understand a new code format
    - [Corey Schafer if __name__ == '__main__' Tutorial](https://www.youtube.com/watch?v=sugvnHA7ElY)
- threading allows you to run tasks while other tasks are waiting
    - [Corey Schafer Threading Tutorial](https://www.youtube.com/watch?v=IEEhzQoKtQU)
- multiprocessing allows multiple functions to run in parallel, allowing you to use the full resources of your computer
    - [Corey Schafer Multiprocessing Tutorial](https://www.youtube.com/watch?v=fKl2JW_qrso&t=313s)
- make a New York Times Scraper!
    - Note: I do not advocate doing this outside of educational purposes. Please purchase a subscription if you wish to read the newspaper regularly.
    - make a class to house your methods
        - make a function that gets all the headlines from the homepages
        - make a function that stores the text (all the p tags) from each article in its own text file
            - you can see how to make files in Multiprocessing/make_file.py (note: you can also append to files with the 'a' mode)
    - solution in Multiprocessing/NYTScraper.py


## Web Development
- learn web development from the ground up (understand html, css, backend, and frontend)
    - [Corey Schafer Tutorial](https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)
- OPTIONAL: understand server-side infrastructure, get a better handle on sql
    - [Sentdex Flask Tutorial](https://www.youtube.com/playlist?list=PLQVvvaa0QuDc_owjTbIY4rbgXOFkUYOUB)
    - note: this is much more advanced, you will have serious web development skills by the end of this tutorial
    - I recommend learning the apache setup at the beginning for gaining increased understanding of working with servers
- make backend api development easier with flask restful
    - [Melvin L Flask Restful Tutorial](https://www.youtube.com/watch?v=s_ht4AKnWZg&ab_channel=MelvinL)
- learn javascript: [Learn Code Academy Tutorial](https://www.youtube.com/watch?v=G-POtu9J-m4&list=PLoYCgNOIyGABdI2V8I_SWo22tFpgh2s6_&index=2)

## Desktop UIs
- learn how to use your web development skills to build interactive platforms with eel
    - [Sourav Johar Eel Tutorial](https://www.youtube.com/watch?v=iy2aKf9AAvc)

## Continued Learning
- there are always new projects and applications for programming, so keep reading  about new programming skills!
- a few skills I have found useful and/or interesting
    - [logging](https://realpython.com/python-logging/)
    - [creating a telegram bot](https://betterprogramming.pub/how-to-get-data-from-telegram-82af55268a4b)
    - [GIS with geopandas](https://www.analyticsvidhya.com/blog/2021/09/how-to-visualise-data-in-maps-using-geopandas/)
    - [working with financial data with the yahoo finance api](https://towardsdatascience.com/free-stock-data-for-python-using-yahoo-finance-api-9dafd96cad2e)
- if you really like programming, reach out to me at admin@entredeveloperslab.com to collaborate on some upcoming projects!
