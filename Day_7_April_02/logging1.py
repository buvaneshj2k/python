import logging

logging.basicConfig(level = logging.DEBUG, filename='log12.txt', filemode = 'a',  format="%(asctime)s - %(levelname)s -%(message)s")

a = input("Enter a first number : ")
b = input("Enter the second number : ")
try:
    if (type(int(a))==int) and (type(int(b))==int):
        print(int(a)+int(b))
except ValueError as e:
    print(e)
    logging.warning("The given inputs are not numbers",exc_info=True)
        