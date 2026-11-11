# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134661209
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def lemonadeChange(bills):  # 定义函数 lemonadeChange（参数：bills）
    # 钱箱贪心（另一种写法）：把零钱放进列表，找零时从大到小取
    pocket = []  # 把 [] 存入 pocket
    for bill in bills:  # 逐个取出 bills 的元素（bill）
        need = bill - 5  # 把 bill 减 5 存入 need
        if need:  # 若 need
            pocket.sort(reverse=True)  # 排序
            used = []  # 把 [] 存入 已用标记
            for note in pocket:  # 逐个取出 pocket 的元素（note）
                if note <= need:  # 若 note 不超过 need
                    need -= note  # need累减 note
                    used.append(note)  # 把 note 追加到列表尾部
                    if need == 0:  # 若 need 等于 0
                        break  # 跳出循环
            if need:  # 若 need
                return False  # 返回 False
            for note in used:  # 逐个取出 已用标记 的元素（note）
                pocket.remove(note)  # pocket 弹出 note)
        pocket.append(bill)  # 把 bill 追加到列表尾部
    return True  # 返回 True


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(lemonadeChange([5, 5, 5, 10, 20]))  # 打印输出
    print(lemonadeChange([5, 5, 10, 10, 20]))  # 打印输出
