"""响应压缩放在哪一层做: 应用层、反代层还是边缘层(纯标准库)。"""
import zlib

COMPRESSIBLE_PREFIX = ("application/json", "text/", "application/javascript")
ALREADY_COMPRESSED = ("image/", "video/", "audio/", "application/zip",
                      "application/pdf", "application/wasm")
MIN_BYTES = 860


def choose_layer(content_type, size, cacheable, cpu_saturated):
    """返回 (layer, reason)。层级选错要么白烧 CPU, 要么缓存键分裂。"""
    if any(content_type.startswith(p) for p in ALREADY_COMPRESSED):
        return "skip", "内容本身已压缩, 再压只会变大"
    if not any(content_type.startswith(p) for p in COMPRESSIBLE_PREFIX):
        return "skip", "未知或不可压类型"
    if size < MIN_BYTES:
        return "skip", "体积不足, 压缩收益抵不过 CPU 开销"
    if cacheable:
        return "cdn", "可缓存内容在边缘压一次, 全链路复用压缩结果"
    if cpu_saturated:
        return "nginx", "应用 CPU 紧张, 把压缩挪到反代层, 挪不动就放弃"
    return "app", "动态响应体积大且不可缓存, 应用层按内容类型精确控制"


def detect_double_encoding(headers):
    """Content-Encoding 值里 gzip 重复出现, 就是双重压缩事故。"""
    enc = headers.get("Content-Encoding")
    if not enc:
        return False
    tokens = [t.strip().lower() for t in enc.split(",") if t.strip()]
    return len(tokens) != len(set(tokens)) or tokens.count("gzip") > 1


CASES = [
    ("application/json", 10240, False, False),
    ("image/png", 10240, False, False),
    ("text/html", 300, False, False),
    ("application/json", 10240, True, False),
    ("application/json", 10240, False, True),
]
for ct, size, cacheable, cpu in CASES:
    layer, reason = choose_layer(ct, size, cacheable, cpu)
    print("%-20s %6dB cache=%-5s cpu=%-5s -> %-6s %s" % (ct, size, cacheable, cpu, layer, reason))

assert choose_layer(*CASES[0])[0] == "app"
assert choose_layer(*CASES[1])[0] == "skip"
assert choose_layer(*CASES[3])[0] == "cdn"
assert choose_layer(*CASES[4])[0] == "nginx"

assert not detect_double_encoding({"Content-Encoding": "gzip"})
assert detect_double_encoding({"Content-Encoding": "gzip, gzip"})
co = zlib.compressobj(6, zlib.DEFLATED, 16 + zlib.MAX_WBITS)
twice = co.compress(b"x" * 100) + co.flush()
print("双重压缩检测通过; 记住输出依赖 Accept-Encoding 时必须回 Vary 头")
