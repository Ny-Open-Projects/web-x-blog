import bisect

if __name__ == "__main__":
    scores = [60, 70, 80, 90]
    bisect.insort(scores, 75)
    print(scores)

    print("left of 80:", bisect.bisect_left(scores, 80))
    print("right of 80:", bisect.bisect_right(scores, 80))
    print("left of 75 :", bisect.bisect_left(scores, 75))

    def grade(score, breakpoints=[60, 70, 80, 90]):
        return "FDCBA"[bisect.bisect(breakpoints, score)]

    print([grade(s) for s in [59, 60, 71, 100]])

    def insert_unique(lst, x):
        pos = bisect.bisect_left(lst, x)
        if pos == len(lst) or lst[pos] != x:
            lst.insert(pos, x)
        return pos

    uniq = [1, 3, 5]
    insert_unique(uniq, 4)
    insert_unique(uniq, 4)
    print("unique insert:", uniq)
