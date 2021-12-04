import sys
import json
borrowlist={}
global Author
books = { 1000: [10,'A time to Kill','Grisham'], 
          1001: [3,'The Pelican Brief','Grisham'],
          1002: [12,'The Litigator','Grisham'],
          1100: [2,'Bloodline','Sheldon'], 
          1101 :[12,'If tommorow Comes','Sheldon'],
          1103 :[10,'Master of the Game','Sheldon'],
          1110 :[11,'Come Easy Go Easy','Chase'], 
          1111 :[8,'Believed Violent','Chase'],
          1112 :[12,'Mission to Venice','Chase']            
          } # Key is ISBN and Values are Copies/Titile/Author
            
def bookmenu():
    while (True) :
        status=input("Enter your Status as User/Admin\n")
        if status=="User" :
            print('Please select one of the following options for book inventory menu As User\n')
            print('Option 1:  View All books')
            print('Option 2:  Borrow a book')
            print('Option 3:  Return a book')
            print('option 4: Search by Author ')
            print('option 5: Search by Title ')
            print('option 9:  Quit the Application')
            break
        elif status=="Admin" :
            lowstock(books)
            print('Please select one of the following options for book inventory menu As Admin\n')
            print('Option 6:  Add more Books')
            print('Option 7:  Remove a book')
            print('Option 8:   Sort the book')
            print('option 9:  Quit the Application')
            break
        else :
            print ("You are not authorised to use the Application\n, Enter 7 to quit the application")
            break

# function to display the content of the Dictionary on and after manipulations
def printbooklist():
    print()
    print('ISBN No','' ,'Quantity ','... ','Title','         ','Author')
    for keys,values in books.items():
        #print("{}".format(i),values)
        print(f'{keys :<7}, {values[0]:<7},{values[1] :<22},{values[2]:<7} ')
    print()
# function to borrow a book for Option 2
def borrowbook(key,title,books):
     
    isbnkey=books.keys()
    if key in isbnkey:
        books[key][0]=books[key][0] -1
    else :
        print(" We do not have the book in stock\n")

        
# function to return a book for option 3
def returnbook(key,title,books):
    isbnkey=books.keys()
    if key in isbnkey:
        books[key][0]=books[key][0] +1
        borrowlist.pop(key,title)
        bl=json.dumps(borrowlist)
        print(bl)
        print (borrowlist)
    else :
        print(" We do not have the book in stock\n")      
# fuction to search by Author from the dictionary : for option 4
def searchbookAuthor(books,search_Author):
    do_exist = False
    for key, val in books.items():
        #print(val[2])
        if val[2] == search_Author:
            do_exist=True
            #print (do_exist) 

            print(val[1],val[2])
# fuction to search by Title from the dictionary : for option 5
def searchbooktitle(books,title):
    do_exist = False
    #print(search_Author)
    for key, val in books.items():
        #print(val[2])
        if val[1] == title:
            do_exist=True
            #print (do_exist) 

            print(val[0],val[1])    
    

# function to add new book to the list : for Option 6
def addbook(key,copy,books):
    
    current_key=books.keys()
    if key in current_key :
        books[key][0]+=copy[0] # increase the qty by 1
    else :
        books[key]=copy

# function to remove book from the  list : for Option 7
def removebook(key,copy,books):
    
    current_key=books.keys()
    if key in current_key :
        books[key][0]-=copy[0] # reduce the qty by 1
    else :
        books[key]=copy

# function to sort book : for Option 8
def sortbook(books) :
     for key,values in sorted(books.items()):
        print(key , " :: " , values)
# function to print the item low on stock
def lowstock(books) :
    print('Find below the list of items low in stock!!!')
    print('Qty ''.','Title')
    for key, val in books.items():
        #print(val[2])
        if val[0] <= 5:
            print(val[0]," ",val[1])   
      

# function to perform selected menu task
while(True):
    # Print items low on stock
    bookmenu()
    menu_choice=int(input("Enter the menu choice : \n"))
    if menu_choice==1 :
        printbooklist()
    elif menu_choice==2:
         #borrowlist={}
         title=input("Enter the title of the books to be borrowed\n")
         ISBN=int(input('Please enter the ISBN Number\n'))
         Author=input('Please Enter the Author of the book\n')
         Copy = int(input('Please enter number of copies to borrow:\n '))
         borrowbook(ISBN,[title,Author],books)
         Blist={ISBN:[title,Author]}
         borrowlist.update(Blist)
         print("the content of the borrowed book.....\n")
         bl1=json.dumps(borrowlist)
         print(bl1)
         print (borrowlist)
         printbooklist()
    elif menu_choice==3:
         title=input("Enter the title of the books to be returned\n")
         ISBN=int(input('Please enter the ISBN Number\n'))
         Author=input('Please Enter the Author of the book\n')
         returnbook(ISBN,[title,Author],books)
         Blist={ISBN:[title,Author]}
         printbooklist()
    elif menu_choice==4:
         search_Author = input("Provide the Author to display his books.....\n")  
         searchbookAuthor(books,search_Author)
    elif menu_choice==5:
         title = input("Provide the title of the book to search for.....")  
         searchbooktitle(books,title)
    elif menu_choice==6 :
        #addbook()
        ISBN=int(input('Please enter the ISBN Number\n'))
        Copy = int(input('Please enter number of copies to add:\n '))
        title = input('Please enter the Title of the book: \n')
        Author = input('Please enter the Author of the book: \n')
        addbook(ISBN, [Copy, title, Author], books)
        printbooklist()
    elif menu_choice==7 :
        #addbook()
        ISBN=int(input('Please enter the ISBN Number\n'))
        Copy = int(input('Please enter number of copies to add:\n'))
        title = input('Please enter the Title of the book: \n')
        Author = input('Please enter the Author of the book: \n')
        removebook(ISBN, [Copy, title, Author], books)
        printbooklist()
    elif menu_choice==8 :
        sortbook(books)
    else :
        print('thanks,You can Contact us at\nEmail:ayobamisomisore@gmail.com\nPhone number:97477293391')
        print()
        break