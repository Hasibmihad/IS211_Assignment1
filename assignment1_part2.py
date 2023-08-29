class Book:
    #author = ""
    #title = ""
    def __init__(self,author,title):
        self.author= author
        self.title= title 

    def display(self):  
        str= self.title+", written by "+self.author
        print (str)
        return 

def main():
    book1 = Book("J. K. Rowling", "Harry Potter and the Goblet of Fire")
    book2 = Book("Walter Scott", "Ivanhoe: A Romance")

    # Print the objects using class Books display() function
    print(book1.display())
    print(book2.display())

if __name__ == "__main__":
    main()
