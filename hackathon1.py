def generate_fibonacci(n):

    fibonacci_sequence = [0, 1]

    while len(fibonacci_sequence) < n:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence

def main():
    try:
        n = int(input("Enter the value of n: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return

        fibonacci_terms = generate_fibonacci(n)
        print(f"Fibonacci sequence up to term {n}:")
        print(fibonacci_terms)

    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

if __name__ == "__main__":
    main()
