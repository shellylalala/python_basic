print(issubclass(ZeroDivisionError, ArithmeticError))  # True
print(issubclass(ZeroDivisionError, Exception))  # True
print(issubclass(ValueError, Exception))  # True
print(issubclass(KeyboardInterrupt, Exception))  # False
print(issubclass(KeyboardInterrupt, BaseException))  # True
