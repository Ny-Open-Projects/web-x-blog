"""推导式里不能写 try:把异常处理下沉到辅助函数。"""
import math


def safe_log(value):
    """非法输入统一表达为 None,不炸整批。"""
    try:
        return round(math.log(value), 3)
    except ValueError:
        return None


if __name__ == "__main__":
    xs = [1, math.e, 0, -2, math.e ** 2]
    print("输入:", xs)
    print("辅助函数版:", [safe_log(x) for x in xs])
    print("前置过滤版:", [round(math.log(x), 3) for x in xs if x > 0])

    try:
        [math.log(x) for x in xs]
    except ValueError as e:
        print("裸推导整批报废:", e)
