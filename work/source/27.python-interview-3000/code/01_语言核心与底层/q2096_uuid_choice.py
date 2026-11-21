"""uuid 选型:uuid1、uuid4 与 uuid5 的取舍。"""
import uuid


if __name__ == "__main__":
    u4a, u4b = uuid.uuid4(), uuid.uuid4()
    print("uuid4 随机:", str(u4a)[:18], "两次不同:", u4a != u4b)

    u1 = uuid.uuid1()
    print("uuid1 带时间戳与节点:", u1.fields[0] > 0, "| MAC 来自 node 字段:", hex(u1.node)[:10], "...")
    print("uuid1 生成端时间可比较:", uuid.uuid1().time >= u1.time)

    n1 = uuid.uuid5(uuid.NAMESPACE_DNS, "example.com")
    n2 = uuid.uuid5(uuid.NAMESPACE_DNS, "example.com")
    print("uuid5 确定性:同输入同输出:", n1 == n2, "|", n1)
    print("换命名空间结果改变:", uuid.uuid5(uuid.NAMESPACE_URL, "example.com") != n1)

    print("选型:常规唯一用 uuid4;确定性标识用 uuid5;uuid1 注意 MAC 隐私")
