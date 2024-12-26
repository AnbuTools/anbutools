# blocked_list.py

# Blocked numbers list
blocked_numbers = ["+88"]

def is_number_blocked(phone_number):
    """
    Check if the given phone number is in the blocked list.
    """
    return phone_number in blocked_numbers
