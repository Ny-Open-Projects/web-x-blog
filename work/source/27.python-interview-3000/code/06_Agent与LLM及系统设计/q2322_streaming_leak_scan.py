"""流式泄露检测:敏感短语被切块拆开也要抓到,用滑动缓冲按最长模式长度重叠扫描。"""
import re

PATTERNS = [re.compile(p) for p in (r"系统提示词是", r"我的密钥是 sk-[a-z0-9]{4}")]


def scan_stream(chunks, max_pattern_len=20):
    buf = ""
    leaked = []
    emitted = []
    for ch in chunks:
        buf += ch
        hit = True
        while hit:
            hit = None
            for pat in PATTERNS:
                m = pat.search(buf)
                if m:
                    hit = pat
                    break
            if hit:
                leaked.append({"pattern": hit.pattern, "match": m.group()})
                buf = buf[:m.start()] + "[已拦截]" + buf[m.end():]
        flush_len = max(0, len(buf) - max_pattern_len)
        emitted.append(buf[:flush_len])
        buf = buf[flush_len:]
    emitted.append(buf)
    return {"emitted": "".join(emitted), "leaked": leaked}


if __name__ == "__main__":
    out = scan_stream(["今天的天气", "不错。系统提示", "词是:请忽略以上指令", "祝你愉快"])
    assert "[已拦截]" in out["emitted"], "跨块泄露被拦截"
    assert "系统提示词是" not in out["emitted"]
    assert "今天的天气" in out["emitted"], "正常内容不受伤"
    assert len(out["leaked"]) == 1 and out["leaked"][0]["pattern"] == "系统提示词是"
    out2 = scan_stream(["我的密钥是 sk-ab12cd 别外传"])
    assert "[已拦截]" in out2["emitted"] and len(out2["leaked"]) == 1
    clean = scan_stream(["正常回答没有问题"])
    assert clean["leaked"] == [] and clean["emitted"] == "正常回答没有问题"
    print("流式泄露检测通过:跨块正则 滑动缓冲 拦截替换")
