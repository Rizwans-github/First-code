#Type your number, it should be smaller than 500.
Your_Number = int(input())
#Here if the chosen number is less than 500 then this code is run.
if Your_Number <= 500:
    print("Numbers after your chosen number are:")
    '''Since, I want to start the count after the given number,
    I made the range start from the entered input'''
    for i in range(Your_Number,500):
        '''I chose to keep this i +=1 here as to make sure that the code prints
        after increasing by 1''' 
        i +=1
        print(i)
    
else:
    print("Chosen number is too large!!!")
