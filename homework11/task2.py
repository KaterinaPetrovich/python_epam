class Order:
    def __init__(self, price, discount_func):
        self.price = price
        self.discount_func = discount_func

    def final_price(self):
        return self.discount_func(self)


def morning_discount(order):
    return order.price - order.price * 0.25


def elder_discount(order):
    return order.price - order.price * 0.9
