import dis, sys

def build():
    xs = [i * 2 for i in range(5)]
    return xs

print(sys.version_info[:2])
print(build())

code = build.__code__
comps = [c for c in code.co_consts if hasattr(c, "co_name")]
print("hidden comp functions:", [c.co_name for c in comps])
# 3.11 及以前: ['<listcomp>']  3.12+: []  —— PEP 709 已内联

print("---- outer bytecode ----")
dis.dis(build)
# 3.12+ 直接可见 RANGE/LOAD_FAST/SWAP 等指令,无 CALL <listcomp>
