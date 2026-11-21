import sys

PLAN = ["mkdir /srv/app", "write config", "restart service"]

def confirm(prompt):
    if "--yes" in sys.argv:
        return True
    try:
        return input(prompt + " [y/N] ").strip().lower() == "y"
    except EOFError:
        print("非交互环境:请显式传 --yes 确认")
        return False

def main(argv):
    dry = "--dry-run" in argv
    print("执行计划:")
    for step in PLAN:
        print("  -", step)
    if dry:
        print("dry-run:未做任何修改")
        return 0
    if not confirm("确认执行以上动作?"):
        print("已取消")
        return 0
    print("已执行(演示)")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
