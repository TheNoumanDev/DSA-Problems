# Question Number 1

# to store the monthly expenses of a person in a list
monthly_expenses = [2200, 2350, 2600, 2130, 2190]

# 1. In Feb, how many dollars you spent extra compare to January?
print("In Feb, I spent extra", monthly_expenses[1] - monthly_expenses[0], "dollars")

# 2. Find out your total expense in first quarter (first three months) of the year.
print("Total expenses of first 3 month is", monthly_expenses[0] + monthly_expenses[1] + monthly_expenses[2], "dollars")

# 3. Find out if you spent exactly 2000 dollars in any month
print("Did I spent exactly 2000 dollars in any month?", 2000 in monthly_expenses)

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
monthly_expenses.append(1980)

# 5. You returned an item that you bought in a month of April and
monthly_expenses[3] = monthly_expenses[3] - 200
print("After returning an item in April, my expenses are", monthly_expenses[3], "dollars")

# 6. You received a birthday gift of 50 dollar in June. Add this to your monthly expense list
monthly_expenses[5] = monthly_expenses[5] + 50

# Question Number 2

heros=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
print("Length of the list is", len(heros))

# 2. Add 'black panther' at the end of this list
heros.append('black panther')

# 3. You realize that you need to add 'black panther' after 'hulk',
# so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
heros.insert(3, 'black panther')
print(heros)

# 4. Now you don't like thor and hulk because they get angry easily :)
# So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
# Do that with one line of code.
heros[1:3] = ['doctor strange']
print(heros)

# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print(heros)

# Question Number 3
#Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
max_number = int(input("Enter a number: "))
odd_numbers = []
for i in range(1, max_number + 1):
    if i % 2 != 0:
        odd_numbers.append(i)
print(odd_numbers)
