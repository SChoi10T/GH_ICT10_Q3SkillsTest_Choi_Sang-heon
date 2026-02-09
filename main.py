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
    if username_length < 7 and password_length < 10: # Checks if the information isn't valid/long enough
        display(f'Invalid output.', target='output')
    elif username_length < 7: # Checks if the username length requirement is too short
        display(f'Your username is too short. Try again.', target='output')
    elif password_length < 10: # Checks if the password length requirement is too short
        display(f'Your password is too short. Try again.', target='output')
    elif password.isalpha(): # Checks if the required letters aren't sufficient
        display(f'Password must contain at least one letter. Try again.', target='output')
    elif password.isdigit(): # Checks if the required numbers aren't sufficient
        display(f'Password must contain at least one number. Try again.', target='output')
    else: # If all conditions are satisfied
        display(f'Welcome, {username}!', target='output')
