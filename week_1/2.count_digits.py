def num_of_digits(n):
 
    n = abs(n)   # Ensuring n is non-negative for digit counting

    if n == 0:
        return 1
    elif n < 10:
        return 1
    else:
        return 1 + num_of_digits(n // 10)

if __name__ == "__main__":

    n = int(input("Enter the number: "))
    
    print(f"The number of digits in {n} is {num_of_digits(n)}")
