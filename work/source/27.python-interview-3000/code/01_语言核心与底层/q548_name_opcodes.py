import dis

GLOBAL = "global value"

def outer():
    enclosed = "enclosed value"

    def inner(local_param):
        local_var = local_param + 1
        return (local_var, enclosed, GLOBAL, len)

    return inner

if __name__ == "__main__":
    for ins in dis.get_instructions(outer()):
        if ins.opname.startswith("LOAD") or ins.opname in {"STORE_FAST", "RETURN_VALUE"}:
            print(f"{ins.offset:4d} {ins.opname:16s} {ins.argrepr}")

    print("call result:", outer()(1))
