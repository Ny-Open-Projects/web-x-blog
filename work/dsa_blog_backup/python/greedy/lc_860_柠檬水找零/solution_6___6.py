# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134661209
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def lemonadeChange(bills):  # 定义函数 lemonadeChange（参数：bills）
    # 钱箱贪心：用列表维护所有零钱，找零时优先用大面额（降序）凑足
    box = []  # 把 [] 存入 box
    for money in bills:  # 逐个取出 bills 的元素（money）
        change = money - 5  # 把 money 减 5 存入 change
        if change > 0:  # 若 change 超过 0
            box.sort(reverse=True)  # 排序
            for i in range(len(box)):  # 让 下标 i 从 长度(box 遍历
                if box[i] <= change:  # 若 box[下标 i] 不超过 change
                    change -= box[i]  # change累减 box[下标 i]
                    box[i] = 0  # 把 0 写入 box[i]
                    if change == 0:  # 若 change 等于 0
                        break  # 跳出循环
            if change != 0:  # 若 change 不等于 0
                return False  # 返回 False
            box = [x for x in box if x != 0]  # 把 [x for x in box if x 不等于 0] 存入 box
        box.append(money)  # 把 money 追加到列表尾部
    return True  # 返回 True


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(lemonadeChange([5, 5, 5, 10, 20]))  # 打印输出
    print(lemonadeChange([5, 5, 10, 10, 20]))  # 打印输出
