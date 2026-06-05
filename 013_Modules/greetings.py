__all__ = ["greet", "greetName", "greetInteractive", "Test2"]

def greet():
    print("Hi there!")

def greetName(name):
    greeting = "Hello"
    finalGreeting = prepGreeting(greeting, name)
    print(finalGreeting)

def prepGreeting(greeting, name):   # Helper function
    return f"{greeting} {name}!"

def greetInteractive():
    name = input("Hi, what's your name: ")
    greeting = "Hello"
    finalGreeting = prepGreeting(greeting, name)
    print(finalGreeting)

def Test():
    greet()
    greetName("Rakesh")
    # greetInteractive()

def Test2():
    greet()
    greetName("Rakesh")
    # greetInteractive()

# print(f"Greetings --> {__name__ = }")

if __name__ == "__main__":
    Test()