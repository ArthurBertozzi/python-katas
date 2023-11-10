"""
In this kata, you will write a function that receives an array of string and returns a 
string that is either 'naughty' or 'nice'. Strings that start with the letters b, f, or k are naughty. 
Strings that start with the letters g, s, or n are nice. Other strings are neither naughty nor nice.

If there is an equal amount of bad and good actions, return 'naughty'

examples

bad_actions = ['broke someone\'s window', 'fought over a toaster', 'killed a bug']
whatListAmIOn(bad_actions)
#-> 'naughty'
good_actions = ['got someone a new car', 'saved a man from drowning', 'never got into a fight']
what_list_am_i_on(good_actions)
#-> 'nice'
actions = ['broke a vending machine', 'never got into a fight', 'tied someone\'s shoes']
what_list_am_i_on(actions)
#-> 'naughty'
"""

bad_actions = ['broke someone\'s window', 'fought over a toaster', 'killed a bug']
good_actions = ['got someone a new car', 'saved a man from drowning', 'never got into a fight']
actions = ['broke a vending machine', 'never got into a fight', 'tied someone\'s shoes']

def what_list_am_i_on(actions):
    #Your code
    category_count = {'naughty': 0, 'nice': 0}
    for action in actions:
        if action[0] in ['b', 'f', 'k']:
        
            category_count['naughty'] += 1
        elif action[0] in ['g', 's', 'n']:
            category_count['nice'] += 1        

    return max(category_count, key=category_count.get)

# other way
# def whatListAmIOn(actions):
#     good = [i for i in actions if i.startswith(('g','s' ,'n'))]
#     bad = [i for i in actions if i.startswith(('b','f' ,'k'))]
#     return 'nice' if len(good)>len(bad) else 'naughty'


