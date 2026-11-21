"""文档解析流水线:路由 -> 清洗 -> 规范化 -> 质量门,保留清洗审计。"""
import re, unicodedata


def clean(text, audit):
    rules = [
        ("页眉页脚", re.compile(r"^\s*第\s*\d+\s*页.*$", re.M)),
        ("连续空白", re.compile(r"[ \t]{2,}")),
        ("广告噪声", re.compile(r"(扫码关注|立即咨询)[^\n]*")),
    ]
    for name, pat in rules:
        text, n = pat.subn("" if name != "连续空白" else " ", text)
        audit[name] = audit.get(name, 0) + n
    return text


def normalize(text):
    text = unicodedata.normalize("NFKC", text)      # 全角转半角等
    return text.replace("\r\n", "\n").strip()


def quality_gate(text):
    if len(text) < 10:
        return "too_short"
    garbage = sum(1 for ch in text if 0xE000 <= ord(ch) < 0xF900)  # 私有区乱码
    if garbage / max(len(text), 1) > 0.3:
        return "mojibake"
    return "ok"


def pipeline(raw, doc_type, audit):
    if doc_type == "html":
        raw = re.sub(r"<[^>]+>", " ", raw)
    raw = clean(raw, audit)
    raw = normalize(raw)
    verdict = quality_gate(raw)
    return raw, verdict


if __name__ == "__main__":
    audit = {}
    raw_html = "<p>退货政策</p>\n<p>七天无理由退货,运费买家承担。</p>\n第 3 页\n扫码关注公众号"
    cleaned, verdict = pipeline(raw_html, "html", audit)
    print("清洗结果:", cleaned)
    print("规则命中:", audit, "质量门:", verdict)
    assert "扫码关注" not in cleaned and "第 3 页" not in cleaned
    assert "七天无理由退货" in cleaned, "有效内容必须保留"
    bad, v2 = pipeline("\uE000\uE001\uE002\uE003\uE004\uE005\uE006\uE007 乱码样本", "pdf", audit)
    print("乱码文档质量门:", v2)
    assert v2 == "mojibake", "乱码进隔离区不进索引"
    print("流水线:格式路由/清洗审计/质量门 全部生效")
