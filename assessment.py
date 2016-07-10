# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5%


def item_cost(state, price):
    """Calculates the cost of an item by adding tax.
    Returns the total cost, including tax depending on which state is entered.
    The default tax is 5%. If the state passed to the function
    is "CA", then tax is raised to 7%.
    """

    tax = .05
    if state == "CA":
        tax = .07
    total_item_cost = (price * tax) + price
    return "$%.2f" % total_item_cost


#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.

def is_berry(fruit):
    """Takes the name of a fruit as a string and returns a boolean.
    If strawberry, cherry or blackberry are passed in, will return True.
    """

    if fruit == "strawberry" or fruit == "blackberry" or fruit == "cherry":
        return True
    else:
        return False


def shipping_cost(fruit):
    """Calculates shipping cost using the is_berry function
    Takes the fruit name as a string, calls the is_berry function and returns
    0 if the fruit is True in is_berry, and 5 if False.
    """

    if is_berry(fruit) is True:
        return 0
    if is_berry(fruit) is False:
        return 5


def is_hometown(town_name):
    """Takes a town name as a string, and returns True if that town is Boulder
    and False if not.
    """

    if town_name == "Boulder" or town_name == "boulder":
        return True
    else:
        return False


def full_name(first_name, last_name):
    """Takes a first and last name as strings and concatenates them."""

    return first_name + " " + last_name


def hometown_greeting(town_name, first_name, last_name):
    """Returns a greeting depending on the results from is_hometown and full_name functions.
    Takes a town name, a first and a last name as strings as arguments, calls
    is_hometown and full_name functions, and returns a greeting depending on the
    output of those two functions.
    """

    if is_hometown(town_name) is False:
        return "Hi " + full_name(first_name, last_name) + ", where are you from?"
    if is_hometown(town_name) is True:
        return "Hi " + full_name(first_name, last_name) + ", we're from the same place!"


#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addone with y = 5. Call again with y = 20. 

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

def increment(x):
    def add(y):
        x = 1
        return x + y
    return add(1)
    
print increment(2)

# The above function is what I started for PART THREE #1 and #2, but then I got 
# super confused on this one and decided to save it for another time. 
# PART THREE #3 below...


def num_list_append(number, num_list):
    num_list.append(number)
    return num_list



#####################################################################