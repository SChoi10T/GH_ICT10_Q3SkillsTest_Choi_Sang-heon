# Account Creation
from pyscript import display, document # pyright: ignore[reportMissingImports]

def account_creation(e):
    document.getElementById("output").innerHTML = "" # Clear Output

    # Get values from the inputs
    username = document.getElementById("input1").value
    password = document.getElementById("input2").value
    username_length = len(username)
    password_length = len(password)

    # Username and Password Restrictions
    if username_length < 7 and password_length < 10: # if the information typed out isn't valid/long enough
        display(f'Invalid output.', target='output')
    elif username_length < 7: # if the username is too short
        display(f'Your username is too short. Try again.', target='output')
    elif password_length < 7: # if the password is too short
        display(f'Your password is too short. Try again.', target='output')
    elif password.isalpha(): # if the letters aren't sufficient
        display(f'Add some letters to your password. Try again.', target='output')
    elif password.isdigit(): # if the numbers aren't sufficient
        display(f'Add some numbers to your password. Try again.', target='output')
    else: # if the information is fulfilled properly
        display(f'Welcome, {username}!', target='output')
