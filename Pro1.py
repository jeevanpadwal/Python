class BockStore:
    NoOfBooks = 0
    def __init__(self,BName,BAuthor):
        self.Name = BName
        self.Author = BAuthor
        BockStore.NoOfBooks = BockStore.NoOfBooks + 1

    def Display(self):
        print("Name :",self.Name)
        print("Author:",self.Author)
        print("Number of books :",BockStore.NoOfBooks)

        print("_____________________________________")

        print(self.Name,"by",self.Author,".",BockStore.NoOfBooks)
    
        


def main():

    obj1 = BockStore("Linux System Programing","Robert Love")
    obj1.Display()

    obj2 = BockStore("C Programming ","Danish Ritchie")
    obj2.Display()


if __name__ == "__main__":
    main()