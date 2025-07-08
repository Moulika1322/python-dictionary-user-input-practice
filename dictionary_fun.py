# Function to print all key-value pairs in a dictionary
def moulika(data):
    for k, v in data.items():
        print(k, ':', v)

# Static dictionary with initial data
mydata = {
    'name': 'kirankumar',
    'age': 18,
    'city': 'vizianagaram',
    'country': 'India'
}

# Adding a new key-value pair dynamically
mydata['mobile'] = 9652630360

print("\n--- Printing Static Dictionary Data ---")
moulika(mydata)

# Dynamic dictionary creation using user input
userdata = {}
m = 1

while m != '0':
    userkey = input('Enter the key: ')
    uservalue = input('Enter the value: ')
    userdata[userkey] = uservalue
    m = input('Enter 0 to exit or any key to continue adding... ')

print("\n--- Printing User-Entered Dictionary Data ---")
moulika(userdata)
