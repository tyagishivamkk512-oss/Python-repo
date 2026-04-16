# dictionary{} ot consists of {key:value}  changable, ordered and no duplicates 

capitals = {'india':'delhi',
            'japan':'tokyo',
            'germany':'berlin',
            'russia':'moscow',}

print(capitals.get('japan'))

capitals.update({'China':'beijing'}) #to update or change 

capitals.update({'india':'m.z.n'})

#capitals.pop('russia') it will delete russia and capital
#capitals.popitem() will delete latest added item
#clear function also there

capitals.keys() # will return all the keys only
capitals.values() # will return all the values only 

capitals.items() # will return a 2d tuple 


for key,value in capitals.items():
    print(f"{key} : {value}")