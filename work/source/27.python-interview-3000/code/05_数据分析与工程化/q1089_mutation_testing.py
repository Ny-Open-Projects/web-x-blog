
def is_adult(age):
    return age >= 18

TESTS = [(-1, False), (17, False), (18, True), (60, True)]

def suite_passes(fn):
    return all(fn(a) == exp for a, exp in TESTS)

MUTANTS = {
    "gt_instead_of_ge": lambda age: age > 18,
    "boundary_17": lambda age: age >= 17,
    "negated": lambda age: not (age >= 18),
    "swap_81": lambda age: age >= 81,   # 存活变异:现有测试抓不到
}

if __name__ == "__main__":
    killed, survived = [], []
    for name, mutant in MUTANTS.items():
        (killed if not suite_passes(mutant) else survived).append(name)
    print("被杀死:", killed)
    print("存活:", survived, "-> 存活变异暴露测试盲区,补充 81/80 边界用例可杀死")
    print(f"变异分数 {len(killed)}/{len(MUTANTS)} = {len(killed) / len(MUTANTS):.0%}")
