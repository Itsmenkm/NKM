###-----------------Variables and String tests
##var="Dhoni"
##Var="sachin"
##
###-----------------function checking
####print(type (var))
##
###print(type (Var))
##
###------------------ Length checking
##print (len (var))
##print (len (Var))
##print (Var)
##print (var)

#--------------------- testing 2 strings in same variable
##var="Dhoni"
##Var="Kohli"
##
##print(var)
##print(Var)

#----------------------------testing name variable
##var=input("type your name")
##
##print (var)

#var=input("type your number")

#print (type (var))
#print (var+var1)

###----------------------------- Blank testing 1
##print ("NKM")
##
##var="Dhoni"
##Var="The Captain cool"
##
##print (var+" " +Var)

##var="Dhoni"
##Var1="10"
##
##print (len (var))
##print (type (var))
##print (type (Var1))
##print (var + Var1)
##
##var=int(input("Enter your Number"))
##var1=10
##print=(var+var1)
##
##try:-----------------------------Error checking
##    var=10/0
##    print(var)
##
##except:
##    print("Sorry")
##
##try:
##    var=("a"+10)
##    print(var)
##except:
##    print("Sorry")

##try:-------------------------------try and except checks
##    var=("a"+10)
##    print(var)
##except ZeroDivisionError:
##    print("Sorry")
##except:
##    print("No")

##try:
##    print("a"+20)
##    print(var)
##except ZeroDivisionError:
##    print("Sorry")
##except TypeError as a:
##    print (a)
##except:
##    print("Sorry")

##
##try:
##    print("q"+10)
##except (ZeroDivisionError,TypeError,SyntaxError) as a:
##    print(a)
##
##try:
##    print("a"+"10")
##except (ZeroDivisionError,TypeError,SyntaxError) as a:
##    print (a)
##else:
##    print("This is not Correct")
##finally:
##    print("This is correct")

##class myError(Exception):---------------------exception adding
##    var="OwnError"
##    
##    
##try:
##    var=10
##    if var>5:
##      raise myError  
##except myError as a:
##    print(a.var)

##Name="india is india"-------------------- count variable function
##print(Name.count("i",4,13))
##
##var="Dhoni"------------------------------- Concatenating str and int
##var1=100
##print("Captain Scored against Pakistan")
##print("Captain",var,"Scored",var1,"against Pakistan")

##Var="india is history"------------------ find fucntion
##print(Var.find("n"))
##
##Var="india is history"------------------- find and index function diff
##print(Var.find("z"))
##print(Var.index("z"))

##Var="India is"--------------------string slicing
##print(Var[1:])
##print(Var[0:3])
##print(Var[-4:])

##Var="Dhoni is"
##print(Var[-2:3])
##print(Var[2:6])
##print(Var[2:7])
##print(Var[2:-2])
##print(Var[::2])
##print(Var[::3])
##print(Var[::4])
##print(Var[::-4])
##
##Var="Dhoni is my Captain"------------------Str to list
##Var1=list(Var)
##print(Var1)

##Var="Dhoni is my Captain"-------------------str functions
##Var1=Var.split()
##print(Var1)

##Var="Dhoni is my Captain"
##Var1=Var.partition("i")
##print(Var1)

##Var="icsicsicsics"
##Var1=Var.split('i',4)
##print(Var1)

##var=" dhoni is "
##print(len(var))
##var1= var.strip()
##print(len(var1))
##
##var="!Dhoni is!"
##var1=var.strip("!")
##print(var1)

##Var=["Dhoni", "Kohli", "Sachin"]-------------------List functions
##Var[0]="India"
##print(Var)
##
##var=["Dhoni", "Sachin", "Kohli"]
##var[2]="I"
##print(var)

##var=["Dhoni", "Sachin", "Kohli"]
##var[2]="Y.S"
##print(var)

##var=["Dhoni", "Sachin", "Kohli"]
##var.insert(0,'india')
##print(var)

##var=["Dhoni", "Sachin", "Kohli"]
##var.append(["india", "My country"])
##print(var)

##var=["Dhoni", "Sachin", "Kohli"]
##var.extend(["India", "is", "My country", "Unity in Diversity", "07", "0,1", "123456789", "10000", "Love you 3000", "I am Iron Man", "Whatever it takes...we're Avengers", "Hey Hulk!, SMASH", "a+b+c=30"])
##print(var)

##var="Dhoni"--------------------------------------For loop functions
##for x in var:
##    print(var)

##var="Dhoni"
##for x in var:
##    print(x)

##var="India is my country"
##for x in var:
##    if x =="i":
##        print("success")
##    elif x=="n":--------------------------------- Muitple char check on same string
##        print("Sucess")
##    else:
##        print("Block")

##var="India is my country"
##for x in var:
##    if x =="i":
##        print("success")
##        break---------------------------------------- To stop print at 1st session

##var="India is my country"
##for x in enumerate(var):
##    if x=="n":
##        print("Success")
##    else:
##        print("Success")


##Var="India is my country"------------------------To check range and even numbers out
##for x,y in enumerate(Var):
##    if y=="i":
##        print("Success")
##for x in range(10):
##    if x%8==0:
##        print(x)

####import time---------------------------------------tkinter module sample
####import tkinter
####from tkinter import Tk
####from tkinter import messagebox
####from tkinter import filedialog
####root=tkinter.Tk()
####root.withdraw()
####root.attributes('-topmost', True)
####time.sleep(10)
####
####dir=filedialog.askdirectory()
####print(dir)
####messagebox.showinfo("dir selected", dir)
##messafbox.showinfo("dirselected", dir)

##for x in range(10):-----------------------------to range in horizontal
##    print(x,end=" ")

##import re----------------------------------------regular expression
##var="india is my country"
##var1=re.search('country',var,re.I)
##print(var1.group())

##import re
##var="<html><head><head><html>"
##var1=re.match('<.*?>', var)
##print(var1)

##import re
##var="Dhoni Scored 183 against Srilanka in 49 Overs at Galle in 2010 with 5 extra"""
##var1=re.findall('\D{1,3}', var)------------------------------------------ \d - decimal, \D - String
##print(var1)

##import re
##var=re.compile('\w[A-E]*')
##var1=var.match("India Is A Good Country")
##print(var1)

##import re
##var="India is"
##var1=re.sub('i','y',var)-------------------------replace single with another string
##print(var1)
