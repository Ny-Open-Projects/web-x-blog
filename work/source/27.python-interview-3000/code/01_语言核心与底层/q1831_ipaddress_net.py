"""ipaddress:地址解析、网段判断与主机遍历。"""
import ipaddress


def classify(text):
    addr = ipaddress.ip_address(text)     # 自动识别 v4/v6,非法则 ValueError
    return type(addr).__name__, addr.is_private, addr.is_loopback


def subnet_membership():
    net = ipaddress.ip_network("192.168.8.0/22")
    inside = ipaddress.ip_address("192.168.9.7") in net
    outside = ipaddress.ip_address("192.168.12.1") in net   # /22 到 11.255 为止
    return inside, outside


def iterate_hosts(net_text="10.0.0.0/30", n=4):
    return [str(h) for h in ipaddress.ip_network(net_text).hosts()][:n]


def strict_check():
    # 10.0.0.1/24 不是网络地址;strict=False 才会归一化成 10.0.0.0/24
    try:
        ipaddress.ip_network("10.0.0.1/24", strict=True)
        return "没报错?"
    except ValueError as e:
        return str(e)[:46]


if __name__ == "__main__":
    print("8.8.8.8:", classify("8.8.8.8"))
    print("127.0.0.1:", classify("127.0.0.1"))
    print("::1:", classify("::1"))
    print("网段成员判定:", subnet_membership())
    print("可用主机:", iterate_hosts())
    print("strict 校验:", strict_check())
