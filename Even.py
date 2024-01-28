#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#function is_even
def is_even(a):
    
    #Checking for even or odd
    if a%2 == 0:  
        return True #return statements
    else:
        return False
    
    
#Main function   
if __name__ == '__main__':
    
    #inputting
    num = int(input("Enter a number: "))
    
    # function call
    result = is_even(num)
    
    #printing the resut
    print(result)

