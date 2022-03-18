#Creating a function to check for a valid input 
def check():
    while True:
        try:
            A=input("Enter an integer: ")
            if int(A)<0 or int(A)>255:
                print("Please enter value between 0 and 255.")
            else:
                break
        except:
            print("Please enter a whole integer value.")
            pass
    return int(A)












        

        


    

    
