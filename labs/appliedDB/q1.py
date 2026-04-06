
def double(x):
    return x * 2

def main():
    numbers = [3, 7, 12, 5]   # list with numbers
    doubled = []              # empty list
    for num in numbers:
        doubled.append(double(num))
    print("Original:", numbers)
    print("Doubled:", doubled)

if __name__ == "__main__":
    main()