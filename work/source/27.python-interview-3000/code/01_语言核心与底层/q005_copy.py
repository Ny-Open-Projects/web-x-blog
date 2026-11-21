import copy

a = [1, [2, 3]]
shallow = copy.copy(a)
deep = copy.deepcopy(a)

a[1].append(4)
print(shallow)   # [1, [2, 3, 4]] 内层被共享
print(deep)      # [1, [2, 3]]    完全独立

if __name__ == "__main__":
    loop = [1, 2]
    loop.append(loop)          # 循环引用
    d = copy.deepcopy(loop)
    print(d[2] is d)           # True,deepcopy 正确处理自引用

    lst = [[0]] * 3            # 三处指向同一个内层 list
    lst[0][0] = 9
    print(lst)                 # [[9], [9], [9]]
