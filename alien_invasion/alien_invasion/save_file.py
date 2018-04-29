filename = 'high_score.txt'

with open(filename, 'w') as obj:
    obj.write('10000')
    
with open(filename) as obj:
    high_score = int(obj.read())
    print(high_score)
            
