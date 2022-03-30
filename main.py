# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


print(add_time("11:06 PM", "2:02")) #expect 1:08AM next day
print(add_time("8:00 PM", "466:02")) #expect 6:02 PM (20 days later)
print(add_time("11:50 PM", "24:15")) #expect 12:05 AM (2 days later)


# Run unit tests automatically
main(module='test_module', exit=False)