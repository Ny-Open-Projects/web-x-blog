import sys

lines_executed = set()

def tracer(frame, event, arg):
    if frame.f_code.co_filename == __file__:
        if event == "line":
            lines_executed.add(frame.f_lineno)
    return tracer                          # 返回自己:继续逐行追踪

def measured():
    x = 1
    if x > 0:
        y = x + 1
    return y

if __name__ == "__main__":
    old = sys.gettrace()
    sys.settrace(tracer)
    measured()
    sys.settrace(old)

    first = measured.__code__.co_firstlineno
    covered = sorted(l for l in lines_executed if first <= l <= first + 5)
    print("lines of measured():", covered)
    print("total traced lines in file:", len(lines_executed))
