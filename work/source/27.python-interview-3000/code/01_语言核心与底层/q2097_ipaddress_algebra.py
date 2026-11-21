"""ipaddress 网段代数:切分、上卷合并与挖洞排除。"""
import ipaddress

block = ipaddress.ip_network("10.0.0.0/24")


if __name__ == "__main__":
    subs = sorted(block.subnets(new_prefix=26))
    print("/24 切成 4 个 /26:", [str(s) for s in subs])

    merged = subs[0].supernet(prefixlen_diff=2)
    print("上卷两个前缀级回到 /24:", merged == block)

    pieces = block.address_exclude(ipaddress.ip_network("10.0.0.64/26"))
    print("挖掉 10.0.0.64/26 后剩余:", [str(p) for p in pieces])

    rng = ipaddress.summarize_address_range(
        ipaddress.ip_address("192.168.0.8"), ipaddress.ip_address("192.168.0.15"))
    print("散 IP 区间归并为 CIDR:", [str(n) for n in rng])

    print("strict=False 自动掩掉主机位:", ipaddress.ip_network("10.0.0.1/24", strict=False))
    try:
        ipaddress.ip_network("10.0.0.1/24")
    except ValueError as e:
        print("默认 strict 校验:", e)
