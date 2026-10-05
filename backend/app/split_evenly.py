# Function: Calculate the split of a bill evenly among a set number of people

# Parameters:
# - total_amount (float): Full amount of the bill (tax / tip included)
# - num_people (int): number of people we splitting the bill by

# Returns:
# - split_amounts (list): Amount each person needs to pay

# List instead of float because of case where cents are infinitely repeating
# Ex: $100 split 3 ways is $33.333~, one person needs to pay $33.34 to
# add up to the total amount

# Edge Cases:
# - num_people <= 0 (not splitting by anyone or negative people is illegal)
# - total_amount <= 0 (less than $0 is illegal)

# test case: split_evenly(100, 3)
# takes total_amount = 100, num_people = 3
# checks the edge cases mentioned if valid
# calculates the split amounts for each person and adds up to the total amount
# stores the values in a list called split_amounts and returns
from decimal import Decimal, ROUND_HALF_UP


def split_evenly(total_amount, num_people):
    # check edge cases
    if not isinstance(num_people, int) or num_people <= 0:
        raise ValueError(
            "Number of people must be greater than 0 and an integer")
    if total_amount <= 0:
        raise ValueError("Total must be greater than 0")
    # calculate the split
    total_decimal = Decimal(str(total_amount))
    total_cents = int(
        (total_decimal * 100).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    )
    cents_per_person, extra_cents = divmod(total_cents, num_people)

    split_amounts = [
        (Decimal(cents_per_person + (1 if index < extra_cents else 0)) / 100)
        for index in range(num_people)
    ]
    # check if sum of split values = total_amount
    expected_total = Decimal(total_cents) / 100
    if sum(split_amounts) != expected_total:
        raise ArithmeticError("Split amounts do not add up to the total")

    return split_amounts
