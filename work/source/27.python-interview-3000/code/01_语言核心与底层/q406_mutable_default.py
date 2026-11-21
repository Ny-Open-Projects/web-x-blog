import dis

def append_to(x, acc=[]):
    acc.append(x)
    return acc

print(append_to(1))        # [1]
print(append_to(2))        # [1, 2] —— 共享同一个默认 list!
print(append_to.__defaults__)      # ([1, 2],) 默认值就存在函数对象里

append_to.__defaults__ = ([],)     # 甚至可以运行期重置
print(append_to(9))                # [9]

print("---- bytecode of the def ----")
dis.dis(compile("def f(x, acc=[]): pass", "<demo>", "exec"))
# 可见 LOAD_CONST 一个空 list 后 MAKE_FUNCTION:默认值随函数对象创建
