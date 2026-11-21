import dis
import types

def compute():
    x = 2 ** 10                 # 折叠为 1024
    y = 1 + 2 * 3               # 折叠为 7
    z = "ab" "cd"               # 相邻字面量拼接
    return x, y, z

if __name__ == "__main__":
    print(compute())
    consts = [c for c in compute.__code__.co_consts
              if not isinstance(c, types.CodeType)]
    print("folded consts:", consts)
    for ins in dis.get_instructions(compute):
        print(f"  {ins.opname:14s} {ins.argrepr}")
