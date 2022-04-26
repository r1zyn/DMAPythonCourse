lower: str = input("Enter a number: ")
lower: int = int(lower)
upper: str = input("Enter another number: ")
upper: int = int(upper)

primeNumbers: list[int] = []

if lower >= upper:
    print("The lower number must be less than the upper number.")
    exit(1)
else:   
    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primeNumbers.append(num)

    print("Prime numbers between {} and {} are: {}".format(lower, upper, ", ".join([str(n) for n in primeNumbers])))