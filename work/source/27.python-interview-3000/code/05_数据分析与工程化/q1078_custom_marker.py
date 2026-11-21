
TESTS = []

def marker(*names):
    def deco(fn):
        fn.marks = set(names)
        TESTS.append(fn)
        return fn
    return deco

@marker("slow", "db")
def test_backup():
    return "backup done"

@marker("slow")
def test_big_report():
    return "report done"

@marker("fast")
def test_add():
    return "2"

def run(only=None, skip=None):
    only, skip = set(only or []), set(skip or [])
    for t in TESTS:
        if t.marks & skip:
            continue
        if only and not (t.marks & only):
            continue
        print("RUN", t.__name__, "->", t())

if __name__ == "__main__":
    # pytest.ini: markers = slow: 超过 1s 的测试;db: 依赖数据库
    # -m "slow and not db" 的等价过滤:
    print("== slow and not db ==")
    run(only=["slow"], skip=["db"])
