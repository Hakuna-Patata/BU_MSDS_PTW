# Program: Cash Register
# Purpose: Program to add items to cart and generate total items and cost.
# Developer: Patrick Weatherford
# Week 2 - Assignment 10.2
# DSC 510 T301 - Intro to Programming
# Bellevue University - Professor Michael Eller


import locale
locale.setlocale(locale.LC_ALL, '')


class CashRegister:

    item_count = 0
    total_price = 0

    def __init__(self):
        self.price = None

    def add_item(self, price):
        self.price = price
        CashRegister.item_count += 1
        CashRegister.total_price += price
        return price

    @property
    def cart_total(self):
        return CashRegister.total_price

    @property
    def cart_item_count(self):
        return CashRegister.item_count


def cart_calc(cart):
    item_counter = 0
    enter_price = ''

    while enter_price.lower() != 'x':
        enter_price = input(f"Enter price for item {item_counter+1}: ")
        if enter_price.lower() == 'x':
            break
        else:
            try:
                float(enter_price)
            except:
                while True:
                    enter_price = input(f"Invalid price entry! Enter numeric price for item {item_counter+1}: ")
                    try:
                        float(enter_price)
                    except:
                        if enter_price.lower() == 'x':
                            break
                        else:
                            continue
                    else:
                        cart.add_item(float(enter_price))
                        item_counter += 1
                        break
            else:
                cart.add_item(float(enter_price))
                item_counter += 1


def program_print(cart):
    nl = '\n'
    tab = '\t'
    dash = '-'
    program_title = "Welcome to the Cash Register Program!"
    exit_msg = "Enter 'x' at any time to complete/exit the program."
    print(f"{dash*50}{nl}{program_title : ^50}{nl}{dash*50}{nl}{exit_msg}{nl}")  # welcome message header
    cart_calc(cart)
    crt_total = locale.currency(cart.cart_total)
    crt_itm_cnt = cart.cart_item_count
    print(f"{nl}Item Count:{crt_itm_cnt}{2*tab}Total:{crt_total}")


def main():
    cart = CashRegister()
    program_print(cart)


if __name__ == '__main__':
    main()
