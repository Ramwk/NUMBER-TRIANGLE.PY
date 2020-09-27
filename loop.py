def greet():
    welcome='WELCOME TO THE NUMBER TRIANGLE PROGRAM !!'      
    return welcome.center(50)

print(greet())

#for simplicity lets take CPL(characters per line) as 70 in this program. 
#For every increase in two columns, an additional row of numbers can be fit. So the maximum number of rows possible will be 35.

rows = 40
while rows > 35:
    rows_string= input('How many rows would you like to have in your triangle? ')
    rows=float(rows_string)

rows=round(rows)

print('\n')
print("The number of rows in your triangle will be : %s" %rows)
print('\n')

while True:
    character=input('What integer would you like to fill your triangle with (BETWEEN 1 AND 10)? ')
    num=float(character)
    if num <= 10:
        break
    else:
        continue

num_round=round(num)

print('\n')
print('Your triangle will be filled with the character : %s' %num_round)
print('\n')

numb=str(num_round)

i=75 #i is the arguement of the method- center
x=0 #x is the variable for iteration until it becomes equal to the number of rows
n=1 #for concatenating the input string from user

#we have two inputs from user- rows and numb

while x < rows:
    concat=numb*n
    print(concat.rjust(i))
    x=x+1
    n=n+2
    i=i+1



   

       











