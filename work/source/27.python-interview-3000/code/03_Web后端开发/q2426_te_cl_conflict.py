"""Transfer-Encoding 与 Content-Length 冲突时的裁决规则(纯标准库)。"""


def parse_framing(header_lines):
    """从原始头行中提取帧信息, 返回 (te_present, chunked, cl_value)。"""
    te, chunked, cl = False, False, None
    for line in header_lines:
        name, _, value = line.partition(":")
        name = name.strip().lower()
        value = value.strip()
        if name == "transfer-encoding":
            te = True
            if "chunked" in value.lower():
                chunked = True
        elif name == "content-length":
            cl = value
    return te, chunked, cl


def decide(role, te_present, cl_present):
    """发送端禁止并存; 接收端 TE 优先; 中间人必须删除 CL 再转发。"""
    if te_present and cl_present:
        if role == "sender":
            return "拒绝发送", "客户端库应报错或剥离 Content-Length 再发"
        if role == "proxy":
            return "删CL转发", "按 TE 分帧并移除 CL, 防止下游解析分歧"
        return "TE优先", "RFC 7230: 存在 TE 时忽略 CL, CL 只是混淆向量"
    if te_present:
        return "TE分帧", "按 chunked 规则读到 0 长度块结束"
    if cl_present:
        return "CL定长", "按 Content-Length 读取指定字节数"
    return "读到关闭", "无帧信息, 只能读到连接关闭为止"


for role, te, cl in [("sender", True, True), ("proxy", True, True),
                     ("server", True, True), ("server", True, False),
                     ("server", False, True), ("server", False, False)]:
    action, why = decide(role, te, cl)
    print("{:6s} TE={:<5} CL={:<4} -> {:6s} | {}".format(role, te, str(cl), action, why))

lines = ["Transfer-Encoding: chunked", "Content-Length: 6", "X-Other: v"]
te, chunked, cl = parse_framing(lines)
assert te and chunked and cl == "6"
assert decide("server", te, cl)[0] == "TE优先"
assert decide("proxy", te, cl)[0] == "删CL转发"
print("要点: 双头并存是请求走私的经典入口, 规则三句话: 发送端不发, 接收端 TE 优先, 中间人删 CL")
