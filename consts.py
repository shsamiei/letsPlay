from asyncore import read
import json 
f = open("config.json" , 'r')
data = json.loads(f.read())
f.close

block_cells = data['block_cells']
