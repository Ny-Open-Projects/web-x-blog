"""函数内嵌类的适用边界:每次调用都是新类。"""
import pickle


def make_visitor(prefix):
    """类捕获闭包参数:同参数造一族行为不同的类。"""
    class Visitor:
        def visit(self, value):
            return f"{prefix} {value}"
    return Visitor


if __name__ == "__main__":
    V1, V2 = make_visitor("see"), make_visitor("walk")
    print("两次调用得到两个不同的类对象:", V1 is not V2, "|", V1.__qualname__)
    print("各自行为:", V1().visit("node"), "/", V2().visit("node"))

    print("跨调用 isinstance:", isinstance(V1(), V2))

    try:
        pickle.dumps(V1())
    except (pickle.PicklingError, AttributeError, TypeError) as e:
        print("pickle 失败:", str(e)[:52])

    print("适用:随闭包变化的类家族与测试替身;需要序列化或稳定身份就提到模块层")
