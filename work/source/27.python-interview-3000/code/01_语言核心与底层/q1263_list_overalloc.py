import sys

if __name__ == "__main__":
    lst = []
    prev = sys.getsizeof(lst)
    marks = []
    for i in range(64):
        lst.append(i)
        s = sys.getsizeof(lst)
        if s != prev:                      # 容量跳变的时刻
            marks.append((len(lst), s))
            prev = s
    print("growth marks:", marks)
    print("一次到位:", sys.getsizeof(list(range(64))))
    print("append 曲线:扩容间距越来越长,均摊 O(1)")
