# membership operators = in , not in

names = {'adolph':'E',
         'hitler':'D',
         'trump':'C',
         'modi':'S'}
name = input('Enter a name: ')

if name in names:
    print(f'{name} got {names[name]} grade')
if name not in names:
    print(f'{name} is not in the names')
