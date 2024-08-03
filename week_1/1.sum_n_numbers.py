def sum_of_numbers(n):
    if n <= 0:
        return 0
    else:
        return n + sum_of_numbers(n - 1)

if __name__ == "__main__":

    n = int(input("Enter the number: "))

    print(f"The sum of {n} natural numbers is {sum_of_numbers(n)}")
