#Ex_1
class Card_Deck:
    def __init__(self):
        self.length = 52
        self.index = 0
        self.__SUITS = ['Пик', 'Бубей', 'Червей', 'Крестей']
        self.__RANKS = [*range(2,11), 'J', 'Q', 'K', 'A']

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.length:
            raise StopIteration()
        else:
            suit = self.__SUITS[self.index // len(self.__RANKS)]
            rank = self.__RANKS[self.index % len(self.__RANKS)]
            self.index += 1
            return f'{rank} {suit}'

card_deck = Card_Deck()
for card in card_deck:
    print(f"Карта:{card}")

#Ex_2
def fibo(n):
    num_1, num_2 = 0, 1
    for i in range(n):
        num_1, num_2 = num_2, num_1 + num_2
        yield num_1

for i in fibo(10):
    print(i, end=" ")