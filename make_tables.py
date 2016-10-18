from astropy.io import ascii

for oneTable in ['bd_table','observing_table']:
    dat = ascii.read(oneTable+'.csv')
    dat.write(oneTable+'.tex')
    