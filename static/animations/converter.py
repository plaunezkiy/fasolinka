import gzip
import json

name = input()
tgs = open(name+'.tgs', 'rb')
tgs_data = gzip.decompress(tgs.read())
tgs.close()

lottie = open(name+'.json', 'w')
lottie.write(tgs_data.decode('utf-8'))
lottie.close()
