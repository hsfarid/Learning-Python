# outer_count = 5

# while outer_count > 0:
#   # Outer loop controls the number of times the inner loop runs
#   inner_count = 1
#   while inner_count <= outer_count:
#     # Inner loop repeats for each outer loop iteration
#     print(inner_count, end=" ")
#     inner_count += 1
#   print()  # Move to a new line after each outer loop iteration
#   outer_count -= 1


# rows = int(input("Enter number of rows: "))
# col = int(input("Enter number of columns: "))

# i = 0


# while i < rows:
#     j = 0
#     while j < col:
#         print("*", end=" ")
#         j += 1
#     print("*")
#     i += 1

#printing a multiplication table
# for i in range(1, 11):
#   # Outer loop iterates through rows (multiplication factors)
#   for j in range(1, 11):
#     # Inner loop iterates through columns (other factors)
#     product = i * j
#     print(f"{i} x {j} = {product}", end="\t")  # Print with tabs for better formatting
#   print()  # Move to a new line after each row

# Printing a Right Triangle of Asterisks

rows = 5

for i in range(1, rows + 1):
  # Outer loop controls the number of rows
  for j in range(1, i + 1):
    # Inner loop prints asterisks for each row
    print("*", end="")
  print()  # Move to a new line after each row of asterisks
