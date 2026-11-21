import sys
import timeit


def work(x):
    return x * 2


def with_try(x):
    try:
        return work(x)
    except Exception:
        raise


if __name__ == "__main__":
    print("python:", sys.version.split()[0])
    n = 200000
    t_plain = timeit.timeit(lambda: work(7), number=n)
    t_try = timeit.timeit(lambda: with_try(7), number=n)
    print("plain: %.1f ms | wrapped in try: %.1f ms" % (t_plain * 1000, t_try * 1000))
    if sys.version_info >= (3, 11):
        print("3.11+: try 本身零指令成本,异常表只在抛出时寻址")
    else:
        print("3.10-: SETUP_FINALLY 有少量固定开销,但同样便宜")
