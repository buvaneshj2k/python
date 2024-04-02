import logging

logging.basicConfig(level=logging.DEBUG, filename='log2.txt', filemode='a', format="%(asctime)s - %(levelname)s - %(message)s")

try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    if isinstance(a, int) == isinstance(b, int):
        print(a , b)
    else:
        logging.warning("The given inputs are not same numbers")
except ValueError:
    logging.error("Invalid input: Please enter valid integers for numbers")