# Blocked Number List
blocked_numbers = ["01689380185", "+8801689380185", "01736197499", "+8801736197499"]

# ব্লকড চেক ফাংশন
def is_number_blocked(phone_number):
    return phone_number in blocked_numbers
