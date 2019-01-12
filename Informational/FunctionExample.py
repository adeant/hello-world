""""set a parameter default value to make it optional"""
"""*args and **kwargs are the conventional names
*args uses value inputs
**kwargs uses key-value inputs
"""


def build_profile(first='john', last='doe', **user_info):
    """build a dictionary w info about user"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user = build_profile(
    'albert', 'einstein',
    location='princeton',
    field='physics'
    )
print(user)


def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(
        "\nMaking a " + str(size) + "-inch pizza with the following toppings:"
        )
    for topping in toppings:
            print("- " + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
