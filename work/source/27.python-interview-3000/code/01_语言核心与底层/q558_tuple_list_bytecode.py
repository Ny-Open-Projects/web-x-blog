import dis

def build_list():
    return [1, 2, 3]

def build_tuple():
    return (1, 2, 3)

def build_tuple_dynamic(x):
    return (x, 2, 3)

if __name__ == "__main__":
    for func in (build_list, build_tuple, build_tuple_dynamic):
        print(func.__name__)
        for ins in dis.get_instructions(func):
            print(f"  {ins.opname:14s} {ins.argrepr}")
