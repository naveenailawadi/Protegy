# Curriculum
- rule 1: code every day
- rule 2: don't forget rule 1

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

## Pandas
- understand how to work with data (python's greatest advantage!)
    - [Corey Schafer Pandas Tutorial](https://www.youtube.com/watch?v=ZyhVh-qRZPA&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&ab_channel=CoreySchafer)
- test out your knowledge by printing all the emails in Pandas / emails.csv
    - solution in Pandas/printingemails.py

## Web Scraping with Beautiful Soup
- learn the basics of web scraping and interacting with websites
    - [Free Code Camp Beautiful Soup Tutorial](https://www.youtube.com/watch?v=XVv6mJpFOb0)
- get a professional - grade understanding of practicing and using the library
    - [Corey Schafer Beautiful Soup Tutorial](https://www.youtube.com/watch?v=ng2o98k983k&t=2s)
