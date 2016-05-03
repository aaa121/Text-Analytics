# This writes a new file or overwrite the previous if existing prior writing
with open('nz_regions.txt','w') as regions:
    regions.write('Auckland\n')
    regions.write('Canterbury\n')
    regions.write('Wellington\n')

# This add to the list of existing file
with open('nz_regions.txt', 'a') as regions:
    regions.write('Waikato\n')
    regions.write('Bay of Plenty\n')
    regions.write('Manawatu-Wanganui\n')



import read_write_file_algorithm as rd
rd.read_write_file('nz_regions.txt','Otago\nNorthland\nSouthland\nHawke\'s Bay\n'
                                    'Taranaki\nNelson\nTasman\nGisborne\nMalborough\nWest Coast')
'''
# This read the outputs
with open('nz_regions.txt', 'r') as regions:
    print(regions.read())
'''