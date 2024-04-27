#Ask user to input the password, and then call the fuction check_password_strength to check the pwd. 
import re
      
def check_password_strength():
      x=str(input("Enter the password: "))
      i=' '
      if x.__len__() >= 8:
         if x.isupper() == True: #check if input password has uppercase only
             print("Input pwd has all uppercase letters only")  
             return False
         else:
             if x.islower() ==  True: #check if input password has lowercase only
                print("Input pwd has all lowercase letters only")
                return False
             else: 
                z = re.compile('[@_!#$%^&*()<>?/\|}{~:]') #check if input password has special characters
                if(z.search(x) == None):  
                       print("Input password has no special characters")       
                       return False                                                                                         
                else:
                     n = re.compile('\d')  
                     if(n.search(x) == None):
                       print("Input password has no number")
                       return False
                     else:  
                        if x.__len__() >= 8 and x.__len__() <= 12:
                          print("Feedback: Weak Password")
                          return True
                        elif x.__len__() > 12:
                          print("Strong Password")
                          return True
      else:
        print("The Password should be 8 characters long, Try again")
        return False

print(check_password_strength())