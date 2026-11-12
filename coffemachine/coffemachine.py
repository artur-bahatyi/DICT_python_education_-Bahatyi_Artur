class CoffeeMachine:
    STATE_CHOOSING_ACTION = "choosing_action"
    STATE_CHOOSING_BUY_OPTION = "choosing_buy_option"
    STATE_FILLING_WATER = "filling_water"
    STATE_FILLING_MILK = "filling_milk"
    STATE_FILLING_BEANS = "filling_beans"
    STATE_FILLING_CUPS = "filling_cups"

    def __init__(self):
        # Початкові запаси (за умовами етапів 4-6)
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

        # Початковий стан — вибір дії
        self.state = self.STATE_CHOOSING_ACTION
        self.is_active = True

    def print_status(self):
        """Виводить поточний стан кавомашини"""
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")

    def make_coffee_steps(self):
        """Етап 1: Повідомлення про етапи приготування напою"""
        print("Starting to make a coffee")
        print("Grinding coffee beans")
        print("Boiling water")
        print("Mixing boiled water with crushed coffee beans")
        print("Pouring coffee into the cup")
        print("Pouring some milk into the cup")
        print("Coffee is ready!")

    def process_input(self, user_input: str):
        """Головний метод обробки введення залежно від поточного стану"""
        if self.state == self.STATE_CHOOSING_ACTION:
            self._handle_choosing_action(user_input)

        elif self.state == self.STATE_CHOOSING_BUY_OPTION:
            self._handle_buying(user_input)

        elif self.state == self.STATE_FILLING_WATER:
            self.water += int(user_input)
            print("Write how many ml of milk do you want to add:")
            self.state = self.STATE_FILLING_MILK

        elif self.state == self.STATE_FILLING_MILK:
            self.milk += int(user_input)
            print("Write how many grams of coffee beans do you want to add:")
            self.state = self.STATE_FILLING_BEANS

        elif self.state == self.STATE_FILLING_BEANS:
            self.beans += int(user_input)
            print("Write how many disposable cups of coffee do you want to add:")
            self.state = self.STATE_FILLING_CUPS

        elif self.state == self.STATE_FILLING_CUPS:
            self.cups += int(user_input)
            self.state = self.STATE_CHOOSING_ACTION
            self._prompt_action()

    def _prompt_action(self):
        """Виводить запит головної дії"""
        print("\nWrite action (buy, fill, take, remaining, exit):")

    def _handle_choosing_action(self, action: str):
        if action == "buy":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:")
            self.state = self.STATE_CHOOSING_BUY_OPTION
        elif action == "fill":
            print("Write how many ml of water do you want to add:")
            self.state = self.STATE_FILLING_WATER
        elif action == "take":
            print(f"I gave you {self.money}")
            self.money = 0
            self._prompt_action()
        elif action == "remaining":
            print()
            self.print_status()
            self._prompt_action()
        elif action == "exit":
            self.is_active = False

    def _handle_buying(self, choice: str):
        if choice == "back":
            self.state = self.STATE_CHOOSING_ACTION
            self._prompt_action()
            return

        if choice == '1':  # Еспресо
            req_water, req_milk, req_beans, cost = 250, 0, 16, 4
        elif choice == '2':  # Лате
            req_water, req_milk, req_beans, cost = 350, 75, 20, 7
        elif choice == '3':  # Капучино
            req_water, req_milk, req_beans, cost = 200, 100, 12, 6
        else:
            self.state = self.STATE_CHOOSING_ACTION
            self._prompt_action()
            return

        # Перевірка ресурсів
        if self.water < req_water:
            print("Sorry, not enough water!")
        elif self.milk < req_milk:
            print("Sorry, not enough milk!")
        elif self.beans < req_beans:
            print("Sorry, not enough coffee beans!")
        elif self.cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            # Викликаємо кроки приготування з Етапу 1
            self.make_coffee_steps()

            self.water -= req_water
            self.milk -= req_milk
            self.beans -= req_beans
            self.cups -= 1
            self.money += cost

        self.state = self.STATE_CHOOSING_ACTION
        self._prompt_action()

if __name__ == "__main__":
    machine = CoffeeMachine()
    machine._prompt_action()

    while machine.is_active:
        user_input = input("> ")
        machine.process_input(user_input)