# Default function to implement conditions to check leap year  
def CheckLeap(Year):  
  # Checking if the given year is leap year  
  if((Year % 400 == 0) or  # sorgu yapıldı
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
    print("Given Year is a leap Year Cooper");  

  # Else it is not a leap year  
  else:  
    print ("Given Year is not a leap Year Cooper")  
# Taking an input year from user  
Year = int(input("Enter the number: "))  
# Printing result  

CheckLeap(Year)  
# this commit also added via using linux-terminal

