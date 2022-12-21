# A simple Triangle Asterisk pattern in python
# Example : for height=4, the pattern is:

#    * 
#   * * 
#  * * * 
# * * * * 

height = int(input('Enter height : '))

for row in range(height):
    for _ in range(height - row -1):
        print(' ', end='')
    for _ in range(row+1):
        print('*', end=' ')
    print()