"""忠实度校验:数字一致 + 实体一致 + 词重叠三层,违规句粒度处置。"""
import re


def split_sentences(text):
    return [s for s in re.split(r"(?<=[。.!])\s*", text) if s.strip()]


def check_sentence(sent, contexts):
    joined = "".join(contexts)
    problems = []
    # 数字一致性
    for num in re.findall(r"\d+(?:\.\d+)?", sent):
        if num not in joined:
            problems.append(f"数字 {num} 无来源")
    # 实体一致性:大写词或书名号视为实体(桩)
    ents = re.findall(r"[A-Z]{2,}|《[^》]+》", sent)
    for e in ents:
        if e not in joined:
            problems.append(f"实体 {e} 无来源")
    # 字符级词重叠(中文按字比较)
    strip = lambda s: set(re.sub(r"[\s,。.!?::;、]", "", s))
    st, ct = strip(sent), strip(joined)
    ov = len(st & ct) / (len(st) or 1)
    if ov < 0.35 and not problems:
        problems.append(f"字重叠率 {ov:.0%} 过低")
    return problems


def audit_answer(answer, contexts):
    report = []
    for sent in split_sentences(answer):
        probs = check_sentence(sent, contexts)
        verdict = "pass" if not probs else ("drop" if any("数字" in p or "实体" in p for p in probs) else "flag")
        report.append({"sentence": sent, "verdict": verdict, "problems": probs})
    return report


if __name__ == "__main__":
    contexts = ["退货运费 由 买家 承担", "七天 无理由 退货", "退款 3 个 工作日 到账"]
    answer = "退货运费由买家承担。退款将在 5 个工作日到账。七天无理由退货。"
    report = audit_answer(answer, contexts)
    for r in report:
        print(f"[{r['verdict']:^5}] {r['sentence']:<24} {r['problems']}")
    verdicts = [r["verdict"] for r in report]
    assert verdicts[1] == "drop", "数字 5 与上下文 3 冲突必须 drop"
    assert verdicts[0] == "pass" and verdicts[2] == "pass"
    kept = [r["sentence"] for r in report if r["verdict"] != "drop"]
    print("保留句:", kept, "-> 只删违规句,不整条拒答")
