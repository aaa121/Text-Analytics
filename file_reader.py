file=open('file_example.txt','r')
contents=file.read()
print(contents)
file.close()

with open('file_example.txt','r') as filex:
    text_filex=filex.read()
    print(text_filex)

with open('file_example.txt', 'r') as filex2:
    line_filex=filex2.readlines()
    print('------------# This print each line into a list form-------------')
    print(line_filex) # This print each line into a list form
    for line in line_filex:
         print('------------# This print each element in the list-------------')
         print(line) # This print each element in the list
         print(len(line))

         print('------------# This print each element in the list but removes, '
               'the string\'s leading and trailing whitespace removed---------')
         linestrip=line.strip()
         print(linestrip)
         print(len(linestrip)) # Among all, this gives the precise length per line of the string by removing the last \n

         print('-------# This print each word-(on a single line or list form)-in each of the element in the list-----------')
         linesplit=line.split()
         print(linesplit)
         print(len(linesplit))

         for i in range(len(linesplit)):
             print('-------# This print each word-(on new line for each word)-in each of the element in the list-----------')
             print(linesplit[i])
             print(len(linesplit[i]))
         '''
         for word in line:
             print(word)
             print(len(word))
        '''
#For line in File technique
with open('file_example.txt', 'r') as filex3:
    for file3 in filex3:
        print(file3)

#For line in File technique II
with open('file_example.txt', 'r') as filex3:
    for file3 in filex3:
        print(file3)
        print(len(file3)) # Return number of character including the trailing, middle and ending whitespace
        print(len(file3.strip())) # Return number of character after removing trailing and ending whitespace at the end
        file3split=file3.split()
        print(len(file3.split())) # Return number of words per line excluding the trailing, middle and ending whitespace
        print(file3split.count('text'))