class Book:
    author = ""
    title = ""
    def __init__(self,author,title):
        Book.author= author
        Book.title= title 

    def display(self):  
        str= Book.author+", written by "+Book.author
        print (str)

        