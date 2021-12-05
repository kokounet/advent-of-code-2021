import numpy as np


def read_lines(path) -> np.ndarray:
    """Return a list of line of shape (numlines, 2, pointdim)"""
    with open(path) as file:
        return np.array([
            list(list(map(int, frag.split(","))) for frag in line.strip().split(" -> "))
            for line in file
        ])


def solution1(path):
    lines = read_lines(path)
    board = np.zeros(lines.max((0, 1))+1)
    no_diags = np.array(list(filter(lambda l: (l[0, :] == l[1, :]).any(), lines)))
    for ((x1, y1), (x2, y2)) in no_diags:
        xslice = slice(x1, x2+1) if x1 <= x2 else slice(x2, x1+1)
        yslice = slice(y1, y2+1) if y1 <= y2 else slice(y2, y1+1)
        board[yslice, xslice] += 1
    return np.sum(board >=2)
    

def solution2(path):
    lines = read_lines(path)
    board = np.zeros(lines.max((0, 1))+1)
    for ((x1, y1), (x2, y2)) in lines:
        xstep = 1 if x1 <= x2 else -1
        ystep = 1 if y1 <= y2 else -1
        x = slice(x1, x2+xstep, xstep)
        y = slice(y1, y2+ystep, ystep)
        if x1 == x2 or y1 == y2:
            board[y, x] += 1
        else:
            print(board[y, x])
            
            diag = np.eye(abs(x.stop - x.start))
            board[y, x] += diag
        print(board)
        print()
        
    return np.sum(board >= 2)

def main():
    print(solution1("input.txt"))
    print(solution2("example.txt"))


if __name__ == "__main__":
    main()