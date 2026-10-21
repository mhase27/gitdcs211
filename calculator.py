def add(a,b):
    return a+b
def subtract(a,b):
    return a-b

def main()->None:
    x = int(input("Enter the value of the first number: "))
    y = int(input("Enter the value of the second number: "))
    print("Simple Calculator")
    print("Addition:", add(x,y))
    print("Subtraction:", subtract(x,y))

main()
