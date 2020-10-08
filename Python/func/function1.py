
def bar():
    print('+','----', '+',end=' ')
    print('+','----', '+',end=' ')
    print('+','----', '+',end=' ')
    print('+','----', '+')
    
def roll():
    print('|', end='    ')
    print('  |', end=' ')
    print('|', end='      ')
    print('|', end=' ')

def do_four(f):
    print()
    f()
    f()

def grid():
    bar()
    roll()
    roll()
    do_four(roll)
    do_four(roll)
    do_four(roll)
    print()
    bar()

def four(f):
    f()
    f()
    f()
    f()

print(four(grid))