def num(n):
    print(n)

def catch_this():
    the_list = (1, 2, 3, 4, 5)

    for i in range(20):
        try:
            num(the_list[i])
        except IndexError: # Raised when accessing a non-existing index of a list
            num(0)

catch_this()
