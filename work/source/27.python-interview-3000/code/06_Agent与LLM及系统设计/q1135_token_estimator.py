"""启发式 token 估算器:中文按字、英文按词,带安全余量,用于预算控制。"""
import re


def estimate_tokens(text: str, margin: float = 0.1) -> int:
    if not text:
        return 0
    cjk = len(re.findall(r"[\u4e00-\u9fff]", text))            # 中文字符
    no_cjk = re.sub(r"[\u4e00-\u9fff]", " ", text)
    words = len(re.findall(r"[A-Za-z0-9]+", no_cjk))           # 英文词/数字串
    punct = len(re.findall(r"[^\s\w\u4e00-\u9fff]", no_cjk))   # 标点符号
    raw = cjk * 1.0 + words * 1.3 + punct * 0.5
    return int(raw * (1 + margin))


if __name__ == "__main__":
    cases = [
        ("你好,世界", 6),
        ("hello world foo", 6),
        ("混合文本 mixed 123!", 12),
    ]
    for text, upper in cases:
        est = estimate_tokens(text)
        print(f"{text!r} -> 估算 {est} tokens")
        assert est <= max(upper + 6, 10), "估算严重偏大"
    long_text = "这是一个用于回归测试的较长中文句子。" * 50
    est = estimate_tokens(long_text)
    print(f"长文本 {len(long_text)} 字符 -> 估算 {est} tokens")
    assert 0.5 <= est / len(long_text) <= 1.6, "比例失真"
    print("估算器通过")
