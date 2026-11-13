# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145345560
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class NestedInteger:  # 定义类
    def __init__(self, value=None):  # 构造函数：初始化成员
        if value is None:  # 若 value is None
            self._list = []  # 把 [] 写入 self._list
            self._is_int = False  # 把 False 写入 self._is_int
            self._int = None  # 把 None 写入 self._int
        elif isinstance(value, list):  # 否则，若 isinstance(value, 列表
            self._list = [
                NestedInteger(v) for v in value
            ]  # 把 [NestedInteger(值) for 值 in value] 写入 self._list
            self._is_int = False  # 把 False 写入 self._is_int
            self._int = None  # 把 None 写入 self._int
        else:  # 否则
            self._int = value  # 把 value 写入 self._int
            self._is_int = True  # 把 True 写入 self._is_int
            self._list = None  # 把 None 写入 self._list

    def isInteger(self):  # 定义函数 isInteger（参数：self）
        return self._is_int  # 返回 self._is_int

    def getInteger(self):  # 定义函数 getInteger（参数：self）
        return self._int  # 返回 self._int

    def getList(self):  # 定义函数 getList（参数：self）
        return self._list  # 返回 self._list


class NestedIterator:  # 定义类
    def __init__(self, nestedList):  # 构造函数：初始化成员
        self.vals = []  # 把 [] 写入 self.vals
        self._dfs(nestedList)  # self._dfs(nestedList)

    def _dfs(self, nestedList):  # 定义函数 _dfs（参数：self, nestedList）
        for nest in nestedList:  # 逐个取出 nestedList 的元素（nest）
            if nest.isInteger():  # 若 nest.isInteger(
                self.vals.append(nest.getInteger())  # 把 nest.getInteger( 追加到列表尾部
            else:  # 否则
                self._dfs(nest.getList())  # self._dfs(nest.getList())

    def next(self):  # 定义函数 next（参数：self）
        return self.vals.pop(0)  # 返回 self.vals 弹出 0)

    def hasNext(self):  # 定义函数 hasNext（参数：self）
        return len(self.vals) > 0  # 返回 长度(self.vals) 超过 0


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    nested = NestedInteger([1, [2, 3]]).getList()  # 把 NestedInteger([1, [2, 3]]).getList() 存入 nested
    it = NestedIterator(nested)  # 把 NestedIterator(nested) 存入 it
    out = []  # 把 [] 存入 out
    while it.hasNext():  # 循环，直到不满足「it.hasNext(」
        out.append(it.next())  # 把 it.下一个( 追加到列表尾部
    print(out)  # 打印输出
