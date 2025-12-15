import random

def luhn_check(card):
    digits = [int(x) for x in card]
    for i in range(len(digits)-2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    return sum(digits) % 10 == 0


def generate_card(bin_):
    card = bin_
    while len(card) < 15:
        card += str(random.randint(0,9))

    for i in range(10):
        test = card + str(i)
        if luhn_check(test):
            return test
    return None