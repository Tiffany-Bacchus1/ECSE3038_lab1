def hello ():
    print ("Engineering Internet of Things Systems - ECSE3038")
    
def validatePassword(password):
    numCount = 0;
    
    if len(password) >= 8 and password.isalnum(): 
        for value in password:
            if element.isdigit():
                numCount += 1 
        
        if numCount >= 2:
            return True
        else:
            return False
            

def sumUpToN(num):
    sum = 0
    num += 1
    
    if num < 1:
        return -1
        
    
    else:
        for index in range (num):
            sum += index 
        return sum 
        
 # Part 1
 hello ()
 print ("/n")
 
 # Part 2
 print(validatePassword  qua3mgi4e"))       
 print ("/n")
 
 # Part 3
 sum = sumUptoN(6)
 print (sum)
