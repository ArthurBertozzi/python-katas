from main import what_list_am_i_on

bad_actions = ['broke someone\'s window', 'fought over a toaster', 'killed a bug']
good_actions = ['got someone a new car', 'saved a man from drowning', 'never got into a fight']
actions = ['broke a vending machine', 'never got into a fight', 'tied someone\'s shoes']

def test_actions():
    assert what_list_am_i_on(bad_actions) == 'naughty'
    assert what_list_am_i_on(good_actions) == 'nice'
    assert what_list_am_i_on(actions) == 'naughty'