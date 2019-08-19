def greet(name="taeyoon", time="morning"):
    print(f'Good {time}, {name}')


name = input("what is your name?")
time = input("what time?")

greet(name, time)
