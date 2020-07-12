class CoffeeMachine:
    current_state = 'choose_action'

    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        self.power = 1

    def __str__(self):
        if CoffeeMachine.current_state == 'choose_action':
            return 'Write action (buy, fill, take, remaining, exit):'
        elif CoffeeMachine.current_state == 'choose_coffee':
            return 'What do you want to buy? 1 - espresso,' \
                   ' 2 - latte, 3 - cappuccino, back - to main menu:'
        elif CoffeeMachine.current_state == 'add_water':
            return 'Write how many ml of water do you want to add:'
        elif CoffeeMachine.current_state == 'add_milk':
            return 'Write how many ml of milk do you want to add:'
        elif CoffeeMachine.current_state == 'add_beans':
            return 'Write how many grams of coffee beans do you want to add:'
        elif CoffeeMachine.current_state == 'add_cups':
            return 'Write how many disposable cups of coffee do you want to add:'

    def behaviour(self, some_input):
        if CoffeeMachine.current_state == 'choose_action':
            if some_input == 'buy':
                CoffeeMachine.current_state = 'choose_coffee'
                print('')
            elif some_input == 'remaining':
                print(f'''
The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.beans} of coffee beans
{self.cups} of disposable cups
{self.money} of money
''')
            elif some_input == 'take':
                taken_money = self.money
                self.money = 0
                print(f'''
I gave you ${taken_money}
''')
            elif some_input == 'fill':
                CoffeeMachine.current_state = 'add_water'
                print('')
            elif some_input == 'exit':
                self.power = -self.power
                return None
        elif CoffeeMachine.current_state == 'choose_coffee':
            if some_input == '1':  # espresso
                if self.water < 250:
                    print('''Sorry, not enough water!
                    ''')
                elif self.beans < 16:
                    print('''Sorry, not enough coffee beans!
                    ''')
                elif self.cups < 1:
                    print('''Sorry, not enough disposable cups!
                    ''')
                else:
                    self.water -= 250
                    self.beans -= 16
                    self.cups -= 1
                    self.money += 4
                    print('''I have enough resources, making you a coffee!
                    ''')
            elif some_input == '2':  # latte
                if self.water < 350:
                    print('''Sorry, not enough water!
                    ''')
                elif self.milk < 75:
                    print('''Sorry, not enough milk!
                    ''')
                elif self.beans < 20:
                    print('''Sorry, not enough coffee beans!
                    ''')
                elif self.cups < 1:
                    print('''Sorry, not enough disposable cups!
                    ''')
                else:
                    self.water -= 350
                    self.milk -= 75
                    self.beans -= 20
                    self.cups -= 1
                    self.money += 7
                    print('''I have enough resources, making you a coffee!
                    ''')
            elif some_input == '3':  # cappuccino
                if self.water < 200:
                    print('''Sorry, not enough water!
                    ''')
                elif self.milk < 100:
                    print('''Sorry, not enough milk!
                    ''')
                elif self.beans < 12:
                    print('''Sorry, not enough coffee beans!
                    ''')
                elif self.cups < 1:
                    print('''Sorry, not enough disposable cups!
                    ''')
                else:
                    self.water -= 200
                    self.milk -= 100
                    self.beans -= 12
                    self.cups -= 1
                    self.money += 6
                    print('''I have enough resources, making you a coffee!
                    ''')
            elif some_input == 'back':
                print('')
            CoffeeMachine.current_state = 'choose_action'
        elif CoffeeMachine.current_state == 'add_water':
            self.water += int(some_input)
            CoffeeMachine.current_state = 'add_milk'
        elif CoffeeMachine.current_state == 'add_milk':
            self.milk += int(some_input)
            CoffeeMachine.current_state = 'add_beans'
        elif CoffeeMachine.current_state == 'add_beans':
            self.beans += int(some_input)
            CoffeeMachine.current_state = 'add_cups'
        elif CoffeeMachine.current_state == 'add_cups':
            self.cups += int(some_input)
            CoffeeMachine.current_state = 'choose_action'
            print('')


capacity = CoffeeMachine(400, 540, 120, 9, 550)

while capacity.power > 0:
    print(capacity)
    action = str(input())
    CoffeeMachine.behaviour(capacity, action)
