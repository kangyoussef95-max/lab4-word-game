def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursion.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
        
    Examples:
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(5)
        5
        >>> fibonacci(10)
        55
    """
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    """Demonstrate the recursive Fibonacci function."""
    print("Recursive Fibonacci Function")
    print("-" * 30)
    
    # Test with several values
    test_values = [0, 1, 5, 10, 15]
    
    for n in test_values:
        result = fibonacci(n)
        print(f"fibonacci({n}) = {result}")


if __name__ == "__main__":
    main()
