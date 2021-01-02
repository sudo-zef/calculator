print('''
           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|  
''')

print('Select operation.')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')
print('5. Floor Division')
print('6. Exponentation')

while True:
    choice = input('Enter choice(1/2/3/4/5/6): ')


    if choice in ('1', '2', '3', '4', '5', '6'):
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))

        if choice == '1':
            print(num1 + num2)

        elif choice == '2':
            print(num1 - num2)

        elif choice == '3':
            print(num1 * num2)

        elif choice == '4':
            print(num1 / num2)
        elif choice == '5':
            print(num1 // num2)
        elif choice == '6':
            print(num1 ** num2)
        break
    else:
        print('Invalid Input')