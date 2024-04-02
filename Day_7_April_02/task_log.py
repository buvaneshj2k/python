import logging

logging.basicConfig(level = logging.DEBUG, filename="log1.txt", filemode="a",  format="%(asctime)s - %(levelname)s -%(message)s")
# *, filename: StrPath | None = ..., filemode: str = ..., format: str = ..., datefmt: str |
# None = ..., style: _FormatStyle = ..., level: _Level | None = ..., stream: SupportsWrite[str] | 
# None = ..., handlers: Iterable[Handler]
# | None = ..., force: bool | None = ..., encoding: str | None = ..., errors: str | None = ...

try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    if isinstance(a, int) and isinstance(b, int):
        print("Sum:", a + b)
    else:
        print("The given inputs are not numbers")
except ValueError:
    logging.error("Invalid input: Please enter valid integers for numbers")
    