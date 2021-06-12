# Format and display (older way)
title = "General"
name = "Kenobi"
print("Hello there, %s %s" % (title, name))
print(f"Hello there, {title} {name}")

# Format and display (most recent way)
title = "General"
name = "Kenobi"
print("Hello there, {1} {0}".format(title, name))

header1 = "Name"
header2 = "Age"
name = "John"
age = 22

print(f"| {header1} | {header2} |")
print("-" * 27)
print(f"| {name} | {age} |")

# Changing the way the variable is displayed
n = 109.2345654324
print(f"{n: .3f}") # will display 109.234

percent = 0.71
print(f"{percent: .1%}") # will display 71.0%