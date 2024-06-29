#basic syntax
# match expression:
#     case pattern1:
#         code_block_1
#     case pattern2:
#         code_block_2
#     ...
#     case pattern_n:
#         code_block_n
#     # Optional: _ (wildcard) for default case

day = input("Enter the day of the week (Monday-Sunday): ").lower()

match day:
    case 'monday':
        print("It is Monday")
    case "tuesday":
        print("ugh! another weekday")
    case "wednesday":
        print("It is Wednesday")
    case "thursday":
        print("It is Thursday")
    case "friday":
        print("TGIF")
    case "saturday" | "sunday":
        print("It is weekends")
    case _:
        print("Enter a valid day")

# Matching Data Types:
# Match Case can also be used to match against data types:
value = input("Enter a value (number or string): ")

match value:
    case int():
        print("You entered an integer", value)
    case str():
        print("You entered a string", value)
    case _:
        print("Invalid data type entered.")