
def choice(message, items):
    '''helper function for giving the user a choice between some number of items'''
    '''each item MUST be a string.'''
    print(message)
    print(items)
    choice = input()
    while choice not in items:
        print("please choose something from the list.")
        choice = input()
    return items.index(choice)
