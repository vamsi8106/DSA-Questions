def factorial_number(n):
    if n==0:
        return 1
    else:
        return n * factorial_number(n-1)
 

if __name__ == "__main__":

    n = int(input("Enter the number: "))
    
    if n>=0:
        print(f"The factorial of a number {n} is {factorial_number(n)}")
    else:
        print(f"The factorial of a neagtive number is not defined")
