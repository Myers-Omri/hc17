

def parse(data_set):
    data_ex = open('data/'+data_set, 'r')
    lines = list(data_ex)
    lp = list(lines[0])
    ROWS = int(lp[0])
    COLS = int(lp[2])
    L = int(lp[4])
    H = int(lp[6])

    params = { 'R': ROWS, 'C': COLS, 'L': L, 'H': H}

    ros = lines[1:]
    piz = []
    for r in ros:
        piz.append(list(r)[0:COLS])

    return params, piz



if __name__ == '__main__':

    parm , pizz = parse("example.in")
    print('params are:')
    print(parm)
    print('the pizza is:')
    print(pizz)