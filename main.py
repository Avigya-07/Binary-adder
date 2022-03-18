import conversion
import greetings
import validInput
#Importing other functions from its module

greetings.welcome()#Calling initial() function from the greetings module.

while True:
    m=validInput.check()
    n=validInput.check()
    #Calling check function of inputValidation module and storing the input in m and n respectively
    
    num1=""
    num1=conversion.changeToBinary(m)#Calling changeToBinary() function of conversion module.
    num2=""
    num2=conversion.changeToBinary(n)#Calling changeToBinary() function of conversion module.
    
    
    summ=""
    i=0
    carry=0
    for i in range(7,-1,-1):
        p=int(num1[i])
        q=int(num2[i])
        
        summ=str(p^q^carry)+summ
        #Calculating sum of individual bits
        
        carry=(carry&(p^q))|(p&q)
        #Calculating carry in(/out) bit
        
    print("Binary Addition: "+summ) #Displaying binary sum of the entered numbers.
                              
    retry=input("Do you want to re-run the program?(y/n)")
    if retry=="y":
        pass
    elif retry=="n":
            break
    else:
        print("invalid input.")
        break
    #Asking user whether to re-run the program or close  it
    
greetings.thanks() #Calling thanks() function of greetings module

    
        
        

        
        
    
    
