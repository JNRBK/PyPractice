class Tshirt:
    """
    Tshirt class about information about shirt
    Args:
    shirt_color
    shirt_style
    shirt_size
    shirt_price
    """
    def __init__(self, shirt_color, shirt_style, shirt_size, shirt_price):
        self.color = shirt_color
        self.style = shirt_style
        self.size = shirt_size
        self.price = shirt_price

    # function that accepts new price and replace the price
    def change_price(self, new_price):
        self.price = new_price

    # function to take amount of discount and apply it to the price
    def make_discount(self, discount):
        return self.price * (1-discount)

details = Tshirt('blue', 'short sleeve', 'M', 30)

print(details.color)
print(details.style, details.price)

details.change_price(40)
print(details.price)

print(details.make_discount(.5))

list_of_shirts = []
shirt1 = Tshirt('grey', 'sleeve-less', 'XL', 45)
shirt2 = Tshirt('green', 'long sleeve', 'L', 35)

list_of_shirts.append(shirt1)
list_of_shirts.append(shirt2)

#looping in all items inside the list
for item in list_of_shirts:
    print("color-> {}, style-> {}, size-> {}, price-> {}"\
        .format(item.color, item.style, item.size, item.price))

#looping on one of the specs
for detail in range(len(list_of_shirts)):
    print(list_of_shirts[detail].color)