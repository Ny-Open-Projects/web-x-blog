import time

BUDGETS = {"parse": 0.05, "aggregate": 0.2}

def parse():
    time.sleep(0.01)
    return "ok"

def aggregate():
    time.sleep(0.3)
    return "ok"

def check_budget():
    failures = []
    for name, fn in (("parse", parse), ("aggregate", aggregate)):
        t0 = time.perf_counter()
        fn()
        cost = time.perf_counter() - t0
        status = "OK" if cost <= BUDGETS[name] else "超预算"
        print(f"{name}: {cost:.3f}s 预算 {BUDGETS[name]}s {status}")
        if cost > BUDGETS[name]:
            failures.append(name)
    return failures

if __name__ == "__main__":
    bad = check_budget()
    print("CI 门禁:", "通过" if not bad else f"阻断,超预算项 {bad}")
