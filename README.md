# First-code
```python
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

This is the first code that I wrote when I was learning python from Solo Learn.

![png](https://github.com/Rizwans-github/First-code/assets/141806496/28cfca9a-5b3b-4eb5-b259-87a1b232a1a9)
![png](https://github.com/Rizwans-github/First-code/assets/141806496/f2bb9e6d-5474-4118-a515-c4d6ff4df1f3)
