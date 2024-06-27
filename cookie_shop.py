"""
Functions necessary for running a virtual cookie shop.
See README.md for instructions.
Do not run this file directly.  Rather, run main.py instead.
"""

from pathlib import Path

def bake_cookies(filepath):
    """
    Opens up the CSV data file from the path specified as an argument.
    - Each line in the file, except the first, is assumed to contain comma-separated information about one cookie.
    - Creates a dictionary with the data from each line.
    - Adds each dictionary to a list of all cookies that is returned.

    :param filepath: The path to the data file.
    :returns: A list of all cookie data, where each cookie is represented as a dictionary.
    """
    # write your code for this function below here.
    cookies = {}

    f = open(filepath, 'r')
    cookie_file = f.readlines()
    f.close()

    cookie_inventory = []

    for line in cookie_file[1:]:
        cookie = line.strip().split(',')
        cookie_id = int(cookie[0])
        cookie_title = cookie[1]
        cookie_description = cookie[2]
        cookie_price = float(cookie[3].replace('$', ''))

        cookie_entry = {'id': cookie_id, 'title': cookie_title, 'description': cookie_description, 'price': cookie_price}
        cookie_inventory.append(cookie_entry)

    return cookie_inventory



def welcome():
    """
    Prints a welcome message to the customer in the format:

      Welcome to the Python Cookie Shop!
      We feed each according to their need.

    """
    # write your code for this function below this line

    print('Welcome to the Python Cookie Shop!\nWe feed each according to their need.')


def display_cookies(cookies):
    """
    Prints a list of all cookies in the shop to the user.
    - Sample output - we show only two cookies here, but imagine the output continues for all cookiese:
        Here are the cookies we have in the shop for you:

          #1 - Basboosa Semolina Cake
          This is a This is a traditional Middle Eastern dessert made with semolina and yogurt then soaked in a rose water syrup.
          Price: $3.99

          #2 - Vanilla Chai Cookie
          Crisp with a smooth inside. Rich vanilla pairs perfectly with its Chai partner a combination of cinnamon ands ginger and cloves. Can you think of a better way to have your coffee AND your Vanilla Chai in the morning?
          Price: $5.50

    - If doing the extra credit version, ask the user for their dietary restrictions first, and only print those cookies that are suitable for the customer.

    :param cookies: a list of all cookies in the shop, where each cookie is represented as a dictionary.
    """
    # write your code for this function below this line

    print('Here are the cookies we have in the shop for you:')
    
    for i in range(len(cookies)):
        cookie = cookies[i]

        print(f"#{cookie['id']} - {cookie['title']}")
        print(f"{cookie['description']}")
        cookie_price = format(cookie['price'],'.2f')
        print(f"Price: ${cookie_price}\n")



def get_cookie_from_dict(id, cookies):
    """
    Finds the cookie that matches the given id from the full list of cookies.

    :param id: the id of the cookie to look for
    :param cookies: a list of all cookies in the shop, where each cookie is represented as a dictionary.
    :returns: the matching cookie, as a dictionary
    """
    # write your code for this function below this line

    for i in cookies:
        if i['id'] == id:
            return i



def solicit_quantity(id, cookies):
    """
    Asks the user how many of the given cookie they would like to order.
    - Validates the response.
    - Uses the get_cookie_from_dict function to get the full information about the cookie whose id is passed as an argument, including its title and price.
    - Displays the subtotal for the given quantity of this cookie, formatted to two decimal places.
    - Follows the format (with sample responses from the user):

        My favorite! How many Animal Cupcakes would you like? 5
        Your subtotal for 5 Animal Cupcake is $4.95.

    :param id: the id of the cookie to ask about
    :param cookies: a list of all cookies in the shop, where each cookie is represented as a dictionary.
    :returns: The quantity the user entered, as an integer.
    """
    # write your code for this function below this line

    given_cookie = get_cookie_from_dict(id, cookies)
    cookie = True

    while cookie:
        order_quantity = input(f"My favorite! How many {given_cookie['title']}s would you like? ")

        if order_quantity.isnumeric():
            order_quantity = int(order_quantity)
            cookie = False

            if order_quantity >= 0:
                order_subtotal = float(given_cookie['price']) * order_quantity
                order_subtotal = format(order_subtotal,'.2f')
                print(f"Your subtotal for {order_quantity} {given_cookie['title']} is ${order_subtotal}.")
    
    return order_quantity


def solicit_order(cookies):
    """
    Takes the complete order from the customer.
    - Asks over-and-over again for the user to enter the id of a cookie they want to order until they enter 'finished', 'done', 'quit', or 'exit'.
    - Validates the id the user enters.
    - For every id the user enters, determines the quantity they want by calling the solicit_quantity function.
    - Places the id and quantity of each cookie the user wants into a dictionary with the format
        {'id': 5, 'quantity': 10}
    - Returns a list of all sub-orders, in the format:
        [
          {'id': 5, 'quantity': 10},
          {'id': 1, 'quantity': 3}
        ]

    :returns: A list of the ids and quantities of each cookies the user wants to order.
    """
    # write your code for this function below this line

    customer_order = []
    while True:
        order_id = input('Please enter the id of the cookie you would like to order: ')
        if order_id in ['finished', 'done', 'quit', 'exit']:
            break
        if order_id.isnumeric():
            order_id = int(order_id)
            if order_id > 0:
                complete_order = {'id': order_id}
                order_quantity = solicit_quantity(order_id, cookies)
                if order_quantity > 0:
                    complete_order['quantity'] = order_quantity
                    customer_order.append(complete_order)
    return customer_order



def display_order_total(order, cookies):
    """
    Prints a summary of the user's complete order.
    - Includes a breakdown of the title and quantity of each cookie the user ordereed.
    - Includes the total cost of the complete order, formatted to two decimal places.
    - Follows the format:

        Thank you for your order. You have ordered:

        -8 Animal Cupcake
        -1 Basboosa Semolina Cake

        Your total is $11.91.
        Please pay with Bitcoin before picking-up.

        Thank you!
        -The Python Cookie Shop Robot.

    """
    # write your code for this function below this line

    order_total = 0
    for i in order:
        cookie_price = format(get_cookie_from_dict(i['id'],cookies)['price'],'.2f')
        order_total += int(i['quantity']) * float(cookie_price)

    print('Thank you for your order. You have ordered:\n')

    for i in order:
        print(f"-{i['quantity']} {get_cookie_from_dict(i['id'],cookies)['title']}\n")
    
    print(f"Your total is ${format(order_total,'.2f')}.")
    print('Please pay with Bitcoin before picking-up.\n')

    print('Thank you!\n-The Python Cookie Shop Robot.')



def run_shop(cookies):
    """
    Executes the cookie shop program, following requirements in the README.md file.
    - This function definition is given to you.
    - Do not modify it!

    :param cookies: A list of all cookies in the shop, where each cookie is represented as a dictionary.
    """
    # write your code for this function below here.
    welcome()
    display_cookies(cookies)
    order = solicit_order(cookies)
    display_order_total(order, cookies)
