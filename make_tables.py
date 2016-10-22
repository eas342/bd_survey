from astropy.io import ascii
import subprocess
import pdb

for oneTable in ['bd_table','observing_table']:
    ## Cleanup CSV file for what MS Excel does
    subprocess.call(['mac2unix',oneTable+'.csv'])
    dat = ascii.read(oneTable+'.csv')
    ascii.write(dat,oneTable+'.tex',
                Writer=ascii.Latex,latexdict={'tabletype':'table*'})
    #dat.write(oneTable+'.tex',latexdict={'tabletype':'table*'},Writer=ascii.latex)
    
    with open(oneTable+'.tex') as TableTex:
        allLines = TableTex.readlines()
        ## Add a horizontal line under headings
        #pdb.set_trace()