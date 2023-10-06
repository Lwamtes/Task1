# Importing two libraries: "Faker" and "pandas."
# "Faker" is used to generate fake data like names, addresses, social security numbers, etc
# "pandas" is used to create and manipulate data in tabular form like DataFrame

from faker import Faker
import pandas as pd


# Next create a Faker instance with Norwegian data
# Create a "Faker" instance and specify the locale ('no_NO') to generate fake data that resembles Norwegian information

fake = Faker(['no_NO'])

# Create an empty DataFrame named "df" to store our generated fake data
# It will have columns named 'Name', 'Address', 'SSN' (Social Security Number), 'Credit Card Number', and 'IPv4 Address'

df = pd.DataFrame(columns=['Name', 'Address', 'SSN', 'Credit Card Number', 'IPv4 Address'])

# How to generate fake data for 100 persons and add it to the DataFrame?
# Use a loop to generate fake data for 100 people. In each iteration of the loop
# Then generate a random name, address, SSN, credit card number (with a specified card type, 'mastercard'), and IPv4 address using the "fake" instance
# Create a list "row" containing these generated value
# Finally add this "row" to our DataFrame "df" at the current index (i) to store the generated data

for i in range(100):
    row = [fake.name(), fake.address(), fake.ssn(), fake.credit_card_number(card_type='mastercard'), fake.ipv4()]
    df.loc[i] = row


# Print to look at the 100 fake data
print(df)