import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
print("WELCOME TO NATIONAL DIGITAL LIBRARY  ASSOCIATION")

def addNewbook():
    bookid=int(input ("Enter a book id: "))
    title = input ("Enter book title :")
    author = input ("Enter author of the book :")
    publisher = input ("Enter book publisher :")
    edition = input ("Enter edition of book :")
    cost = int (input("Enter cost of the book :" ))
    category = input ("Enter category of book :")
    bdf = pd.read_csv ("book.csv")
    n=bdf["bookid"].count()
    bdf.at[n] = [bookid, title, author, publisher, edition, cost, category]
    bdf.to_csv("book.csv", index = False)
    print("Book added successfully")
    print(bdf)
    showMenu()
    
def searchBook():
    title = input ("Enter a book name :")
    bdf=pd.read_csv ("book.csv")
    df=bdf.loc[bdf["title"]==title]
    if df.empty:
        print("No book found with given code")
    else:
        print("Books details are :")
        print(df)
    showMenu()
        
def deleteBook() :
    bookid = float(input("Enter a book id"))
    bdf=pd.read_csv("book.csv")
    bdf=bdf.drop(bdf[bdf["bookid"] == bookid].index)
    bdf.to_csv("book.csv", index=False)
    print("Book Deleted Successfully")
    print(bdf)
    showMenu()

def showBooks():
    bdf=pd.read_csv ("book.csv")
    print(bdf)
    wait=input()
    showMenu()
    
def addNewMember():
    mid = int(input ("Enter a member id: "))
    mname = input ("Enter member name : ")
    phoneno = int(input ("Enter phone number : "))
    numberofbooksissuied=0
    mdf = pd.read_csv("member.csv")
    n = mdf ["mid"].count()
    mdf.at[n] = [mid, mname, phoneno, numberofbooksissuied]
    mdf.to_csv ("member.csv", index = False)
    print("New Member added successfully")
    print(mdf)
    showMenu()

def searchMember():
    mn = input("Enter a member name :")
    bdf=pd.read_csv("member.csv")
    df =bdf.loc[bdf["m_name"]== mn]
    if df.empty:
        print("No member found with given name")
    else:
        print("Members details are :")
        print (df)
    showMenu()


def deleteMember():
    mid=int(input ("Enter a member id : "))
    bdf=pd.read_csv ("member.csv")
    print(bdf)
    bdf=bdf.drop(bdf[(bdf["mid"]==mid)].index)
    bdf.to_csv("member2.csv", index= False)
    print("Member Deleted Successfully")
    print(bdf)
    showMenu()

def showMembers():
    bdf=pd.read_csv("member.csv")
    print (bdf)
    showMenu()
    
def issueBooks():
    book_name = input ("Enter book name :")
    bdf = pd. read_csv ("book.csv")
    bdf = bdf.loc [bdf["title"] == book_name]
    if bdf.empty:
        print ("No Book Found in the Library")
        return
    m_name = input("Enter member name :")
    mdf = pd. read_csv ("member.csv")
    mdf = mdf.loc[mdf ["m_name"] == m_name]
    if mdf.empty:
        print("No such Member Found")
        return
    dateofissue = input("Enter date of issue : ")
    numberofbookissued=int(input("Enter number of book issued :"))
    bdf = pd.read_csv("issuebooks.csv")
    n=bdf["book_name"].count()
    bdf.at[n] =[book_name, m_name, date.today(), numberofbookissued,""]
    bdf.to_csv ("Wissuebooks.csv", index = False)
    print("Book issued successfully")
    print (bdf)
    showMenu()


def returnBook():
    m_name=input("Enter a member name :")
    book_name = input ("Enter book name :")
    idf = pd.read_csv ("issuebooks.csv")
    idf = idf.loc[idf["book_name"] == book_name]
    if idf. empty:
        print ("The book is not issued in records")
    else:
        idf = idf.loc[idf["m_name"] == m_name]
        if idf. empty:
            print("The book is not issued to the member")
        else:
            print ("Book can be returned")
            ans = input ("Are you sure you want to return the book :")
            if ans.lower() == "yes" :
                idf=pd.read_csv ("issuebooks.csv")
                idf = idf.drop (idf[idf["book_name"] == book_name]. index)
                idf.to_csv ("issuebooks.csv", index=False)
                print("Book Returned Successfully")
            else:
                print("Return operation cancelled")
    showMenu()





def showissuedBooks ():
    idf=pd.read_csv ("issuebooks.csv")
    print (idf)
    showMenu()


    
def deleteissuedBooks ():
    book_name = input ("Enter a book name :")
    bdf=pd.read_csv ("issuebooks.csv")
    bdf=bdf.drop (bdf[bdf["book_name"]==book_name]. index)
    bdf.to_csv ("issuebooks.csv", index= False )
    print("Deleted Issuied Book Successfully")
    print (bdf)
    showMenu()




def showCharts():
    print("Press 1 - Books and their Cost")
    print("Press 2 - Number of Books issued by members ")
    ch = int (input ("Enter your choice : "))
    if ch == 1:
        df = pd.read_csv ("book.csv")
        df1 = df[["title", "cost"]]
        df1.plot("title","cost", kind='bar')
        plt.xlabel('title------->')
        plt.ylabel('cost------->')
        plt.show()

    if ch == 2:
        df = pd. read_csv ("issuebooks.csv")
        df1 = df[["numberofbooks","m_name"]]
        df1.plot(kind='bar', x="m_name",color="red",
                 label="Number of books Issued")
        plt.legend()
        plt.show()
    showMenu()


        

def showMenu():
    print("                                                                                                  ")
    print("    NATIONAL DIGITAL LIBRARY  ASSOCIATION                 ")
    print("                                                                                                  ")
    print("Press 1 Add a New Book")
    print("Press 2 - Search for a Book")
    print ("Press 3 - Delete a Book")
    print("Press 4 - Show All Books")
    print("Press 5 - Add a New Member")
    print("Press 6 - Search for a Member")
    print("Press 7 - Delete a Member")
    print("Press 8 - Show All Members")
    print("Press 9 - Issue a Book")
    print("Press 10 - Return a Book")
    print("Press 11 Show All Issued Books")
    print("Press 12 Delete a Issue a Book")
    print("Press 13 - To view Charts")
    print("Press 14 - To exit")
    ch = int (input ("Enter your choice : "))
    while True:
        
        if ch == 1:
            addNewbook()
            wait=input()
        elif ch == 2:
            searchBook()
            wait=input()
        elif ch == 3:
            deleteBook()
            wait=input()
        elif ch == 4:
            showBooks ()
            wait=input()
        elif ch == 5:
            addNewMember()
        elif ch == 6:
            searchMember()
            wait=input()
        elif ch == 7:
            deleteMember()
            wait=input()
        elif ch == 8:
            showMembers()
            wait=input()
        elif ch == 9:
            issueBooks()
            wait=input()
        elif ch == 10:
            returnBook()
            wait=input()
        elif ch == 11:
            showissuedBooks()
            wait=input()
        elif ch == 12:
            deleteissuedBooks ()
            wait=input()
        elif ch == 13:
            showCharts()
            wait=input()
        elif ch == 14:
            print('''
                     Library Project made by         : Anurag Sharma
                     School Name                 : Delhi Public School, Sec-19, Faridabad
                     Session                     : 2020-21
                     ''')
            break

showMenu()
