class CoffeeMachine:

    def __init__(self):
        self.ingredients = [400, 540, 120, 9, 550]
        self.espresso = [250, 0, 16, 1, 4]
        self.latte = [350, 75, 20, 1, 7]
        self.cappuccino = [200, 100, 12, 1, 6]
        self.dic = {'1': self.espresso, '2': self.latte, '3': self.cappuccino}
        self.inp = None

    def action(self):
        print('\nWrite action (buy, fill, take):')
        inp = str(input())
        if inp == "buy":
            self.buy()
        elif inp == "fill":
            self.fill()
        elif inp == "take":
            self.take()
        elif inp == 'exit':
            self.end()
        elif inp == 'remaining':
            self.inventory()
        else:
            self.action()

    def buy(self):
        print('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
        inp = str(input())
        if inp == 'back':
            self.action()
        self.inp = self.dic[inp]
        self.coffee()

    def coffee(self):
        if min([i - j for i, j in zip(self.ingredients, self.inp)]) < 0:
            print('Sorry, not enough water!')
            self.action()
        print('I have enough resources, making you a coffee!')
        self.ingredients = [i - j for i, j in zip(self.ingredients, self.inp)]
        self.ingredients[4] += self.inp[4] * 2
        self.action()

    def fill(self):
        print('Write how many ml of water do you want to add:')
        self.ingredients[0] += int(input())
        print('Write how many ml of milk do you want to add:')
        self.ingredients[1] += int(input())
        print('Write how many grams of coffee beans do you want to add:')
        self.ingredients[2] += int(input())
        print('Write how many disposable cups of coffee do you want to add:')
        self.ingredients[3] += int(input())
        self.action()

    def take(self):
        print(f'I gave you {self.ingredients[4]}')
        self.ingredients[4] = 0
        self.action()

    def inventory(self):
        print(f'\nThe coffee machine has:\n{self.ingredients[0]} of water\n{self.ingredients[1]} of milk')
        print(f'{self.ingredients[2]} of coffee beans\n{self.ingredients[3]} of disposable cups')
        print(f'{self.ingredients[4]} of money')
        self.action()

    def end(self):
        self.inp = None
        exit()


gogogo = CoffeeMachine()
gogogo.action()
