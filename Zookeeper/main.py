import animals

animals = [animals.camel, animals.lion, animals.deer, animals.goose, animals.bat, animals.rabbit]
habitat = int(input('Which habitat # do you need? > '))
while habitat != 'exit':
    print(animals[habitat])
    habitat = input('Which habitat # do you need? > ')
print('See you!')
