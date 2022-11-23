
expenses = []
num_expenses = int(input("Etner # of expenses: "))
for expense in range(num_expenses):
    expenses.append(float(input("Enter an expense: ")))

print(f'My total week expenses were ${sum(expenses)}.')