# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145244333
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def findMinArrowShots(points):  # 定义函数 findMinArrowShots（参数：points）
    if not points:  # 若 not points
        return 0  # 返回 0
    points.sort(key=lambda x: x[1])  # 排序
    arrows = 1  # 把 1 存入 arrows
    end = points[0][1]  # 把 points[0][1] 存入 终点
    for start, end_point in points[1:]:  # for 起点, end_point in points[1:]:
        if start > end:  # 若 起点 超过 终点
            arrows += 1  # arrows累加 1
            end = end_point  # 把 end_point 存入 终点
    return arrows  # 返回 arrows


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(findMinArrowShots(None))  # 打印输出
