#!/usr/bin/env python3

print("sudoku")

# Data structure definitions:
# I0: An integer in 0..9
# I9: An integer in 1..9
# L3: A list with 3 items
# L9: A list with 9 items

# put: The problem to solve.
# L9.L9.I0: I0 means (to me) an integer in 0..9
#           L9 means a list with 9 items.
# The Daily Herald 2022-08-17
put = [ [ 0, 6, 0  , 0, 5, 0  , 0, 7, 0 ]
      , [ 0, 0, 4  , 0, 6, 8  , 0, 5, 0 ]
      , [ 0, 0, 8  , 0, 0, 0  , 0, 0, 3 ]

      , [ 2, 0, 0  , 0, 8, 0  , 7, 1, 0 ]
      , [ 0, 0, 0  , 9, 4, 7  , 0, 0, 0 ]
      , [ 0, 8, 7  , 0, 2, 0  , 0, 0, 9 ]

      , [ 3, 0, 0  , 0, 0, 0  , 9, 0, 0 ]
      , [ 0, 7, 0  , 6, 9, 0  , 1, 0, 0 ]
      , [ 0, 5, 0  , 0, 3, 0  , 0, 4, 0 ]
      ]

wrk = [ [ [], [], []  , [], [], []  , [], [], [] ]
      , [ [], [], []  , [], [], []  , [], [], [] ]
      , [ [], [], []  , [], [], []  , [], [], [] ]

      , [ [], [], []  , [], [], []  , [], [], [] ]
      , [ [], [], []  , [], [], []  , [], [], [] ]
      , [ [], [], []  , [], [], []  , [], [], [] ]

      , [ [], [], []  , [], [], []  , [], [], [] ]
      , [ [], [], []  , [], [], []  , [], [], [] ]
      , [ [], [], []  , [], [], []  , [], [], [] ]
      ]

wrk_todo = []

def setup():
    for row in range(9):
        for col in range(9):
            tgt = put[row][col]
            if tgt:
                wrk_todo.append((row, col, tgt))
                wrk[row][col].append(tgt)
            else:
                for k in range(1, 10):
                    wrk[row][col].append(k)
    print(wrk)
    print()
    print(wrk_todo)
    print()

def sprint(x, sub=" "):
    """Print an L9.L9.I0, defaulting to subbing a space for a zero"""
    h = "+-------+-------+-------+"
    for i in range(3):
        print(h)
        for j in range(3):
            r = x[i * 3 + j]
            for k in range(3):
                print("|.", end="")
                for l in range(3):
                    c = r[k * 3 + l]
                    print( ( sub if c == 0 else str(c) ) + ".", end="")
            print("|")
    print(h)

def rule0_sub(row, col, tgt):
    """ For an L9.I9 at a given row and column:
        - If the list is more than one item long and the target value is
          in the list, then remove that value from the list.
        - If the list just became one item long, add what's left there to
          wrk_todo to also remove that item from every row, column and
          3x3box."""
    lst = wrk[row][col]
    if len(lst) > 1 and tgt in lst:
        lst.remove(tgt)
        if len(lst) == 1:
            wrk_todo.append((row, col, lst[0]))

def rule0():
    """ For a given target row, column and value, remove that value from
        that row, column and 3x3box from wrk, except don't remove that
        value if the list it is in is one item long. """
    tgt_row, tgt_col, tgt_val = wrk_todo.pop(0)
    for row in range(9):
        rule0_sub(row, tgt_col, tgt_val)
    for col in range(9):
        rule0_sub(tgt_row, col, tgt_val)
    box_row_beg = tgt_row // 3
    box_col_beg = tgt_col // 3
    box_row_end = box_row_beg + 3
    box_col_end = box_col_beg + 3
    for row in range(box_row_beg, box_row_end):
        for col in range(box_col_beg, box_col_end):
            rule0_sub(row, col, tgt_val)

def rule1():
    """" Look for in-3x3box in-line pairs and eliminate stuff... """
    ret = 1
    for box_row in range(3):
        for box_col in range(3):
            pass
    return ret

def main():
    sprint(put, "-")
    setup()
    while True:
        if len(wrk_todo) > 0:
            rule0()
        elif rule1():
            break
                
    print(wrk)
    print()
    print(wrk_todo)
    print()


if __name__ == "__main__":
    main()
