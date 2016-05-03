with open('donald-trump-brussels-attack.txt','r') as file:
    dtb100=file.read(100) # Read the first 100 characters
    dtb200=file.read(200) # Read another 200 characters
    dtb=file.read() # Read the rest file or put any negative value "file.read(-1)"
print(dtb100)
print("---------------------------------------------------------------------------------")
print(dtb200)
print("---------------------------------------------------------------------------------")
print(dtb)
print("---------------------------------------------------------------------------------")
'''
When reading a file and starting with the word "with", there is no need to
write a corresponding closing command "file.close()". Otherwise, the following
commands returns.
file.close()
trump=file.read()
print(trump)
----------------------------------------------------------------------------------------------------------------
Traceback (most recent call last):
  File "C:/Users/Funmwan/Desktop/Python/Training 101/file_examples/reader_DT_brussel.py", line 13, in <module>
    trump=file.read()
ValueError: I/O operation on closed file.
----------------------------------------------------------------------------------------------------------------
'''
'''
file.close()
trump=file.read()
print(trump)
'''

'''
---------------------------------------------------------------------------------------
'''

with open('donald-trump-brussels-attack.txt', 'r') as docfile:
    dtrump=docfile.read()
    print(dtrump.split())

print(dtrump.split().count("Donald"))
import word_occurence_counter_program as wc

trumpcount=wc.word_counter(dtrump,'','Trump')
print(trumpcount)

trumpcount2=wc.word_counter(dtrump,'','Trump:')
print(trumpcount2)



with open('donald-trump-brussels-attack.txt', 'r') as docfilex:
    docline=docfilex.readlines()
    for line in docline:
        linestrip=line.strip()
        print(len(linestrip))

with open('donald-trump-brussels-attack.txt', 'r') as dtfilex:
    for dtdoc in dtfilex:
        dtstrip=dtdoc.strip()
        dtsplit=dtdoc.split()
        print(len(dtstrip))
        print(len(dtsplit))
