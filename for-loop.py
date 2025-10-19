print('\nInvert Pyramit\n')
for i in range(5):
    x = '^ '
    x = x*(5-i)
    print(f'{x: ^10}')

print('\nInvert Pyramit\n')
for i in range(5):
    x = 'L '
    x = x*i
    print(f'{x: <10}')
print('\nInvert Pyramit\n')
for i in range(5):
    x = 'R '
    x = x*i
    print(f'{x: >10}')

print('\nInvert Pyramit\n')
for i in range(5):
    x = 'A '
    x = x*i
    print(f'{x: ^10}')

for i in range(5):
    x = 'A '
    x = x*(5-i)
    print(f'{x: ^10}')    