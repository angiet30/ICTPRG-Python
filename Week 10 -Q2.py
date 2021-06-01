authors = (
    'Charles Dickens: 1870',
    'William Thackeray: 1863',
    'Anthony Trollop: 1882',
    'Gerard Manley Hopkis: 1889',
)
for comp in authors:
    new = comp.split(':')
    print (new[0],'die in',new[1])