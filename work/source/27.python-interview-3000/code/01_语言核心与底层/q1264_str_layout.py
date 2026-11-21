import sys

if __name__ == "__main__":
    samples = [("ascii UCS1", "a" * 10),
               ("中文 UCS2", "中" * 10),
               ("emoji UCS4", "\U0001f600" * 10)]
    for tag, s in samples:
        print("%-10s len=%d sizeof=%d" % (tag, len(s), sys.getsizeof(s)))
    print("升宽: 'aa' + '中' sizeof =", sys.getsizeof("aa" + "中"),
          "| 'aa' sizeof =", sys.getsizeof("aa"))
    print("编码后回到字节宽度:", len(("a" * 10).encode("ascii")), "bytes")
