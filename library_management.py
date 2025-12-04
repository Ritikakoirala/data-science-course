try:
    def addbook():
        bookname=input("enter your name:")
        authorname=input("enter your authorname:")
        bookprice=int(input("enter your bookprice:"))
        book = {"bookname": bookname, "authorname": authorname, "bookprice": bookprice}
        with open("library.txt", "a") as f:
            f.write(str(book) + "\n")
            print("book added")

    def removebook():
        bookname = input("enter your bookname:")
        with open("library.txt", "r") as f:
            lines = f.readlines()
        with open("library.txt", "w") as f:
            for line in lines:
                if bookname not in line:   
                    f.write(line)
        print("book removed")


    def updatebook():
        bookname = input("enter your bookname:")
        newprice = int(input("enter your new bookprice:"))
        with open("library.txt", "r") as f:
            data = f.read()
        newdata = ""
        updated = False
        for line in data.split("\n"):
            if bookname in line and line.strip() != "":
                record = eval(line)     
                record.pop("bookprice")       
                record["bookprice"] = newprice   
                newdata += str(record) + "\n"
                updated = True
            else:
                newdata += line + "\n"

        with open("library.txt", "w") as f:
            f.write(newdata)

        if updated:
            print("book updated")
        else:
            print("book not found")


    while True:
        choice = int(input("enter your choice addbook for 1, removebook for 2, updatebook for 3, exit for 4:"))
        if choice == 1:
            addbook()
        elif choice == 2:
            removebook()
        elif choice == 3:
            updatebook()
        elif choice == 4:
            break
        else:
            print("invalid choice")
except Exception as e:
    print(e)