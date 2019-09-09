if __name__ == '__main__': ## creates the basis for how the program is going to intake and return data

    birthdays = {   # creates the dictionary and labels it  

        'Quentin Tarantino': '03/27/1963', 
        'Kanye West': '06/08/1977',
        'James Baldwin': '08/02/1924',
        'Ingmar Bergman': '07/14/1918',
        'Joan Didion': '12/05/1934',
        'Phil Elverum': '05/23/1978'}
        # these are some of my favorite artists, which is why they've been included in this list 

    print('Hello User! Welcome to the Birthday Repository! We know the birthdays of:')
    "prints the opening statement and greeting, as well as the full list of birthdays stored here"
    for name in birthdays: ## fills in the information listed in the dictionary function above
        print(name) 

    print('Which birthday would you like to look up?')
    "'prints the ending line of the opening statement"
    name = input()
    if name in birthdays: # displays the requested information if correct input is received
            print('{}\'s birthday is {}. '.format(name, birthdays[name]))
    else: # displays an error message if an incorrect statement is entered
        print('Sadly, we don\'t have {}\'s birthday in our repository. Try again!'.format(name))

