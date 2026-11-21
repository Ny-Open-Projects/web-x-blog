"""引用溯源:片段编号表 + 标记解析 + 重叠归因兜底 + unsourced 标记。"""
import re


def token_set(s):
    return set(s.split())


def overlap(a, b):
    sa, sb = token_set(a), token_set(b)
    return len(sa & sb) / (len(sa) or 1)


class CitationMapper:
    def __init__(self, chunks):
        self.chunks = chunks                     # 编号即索引+1

    def map_answer(self, answer):
        out, mapping = [], {}
        for sent in re.split(r"(?<=[。.!])\s*", answer.strip()):
            if not sent:
                continue
            m = re.search(r"\[(\d+)\]", sent)
            if m and 1 <= int(m.group(1)) <= len(self.chunks):
                ref = int(m.group(1))
            else:                                 # 无标注 -> 重叠归因兜底
                best = max(range(len(self.chunks)),
                           key=lambda i: overlap(sent, self.chunks[i]))
                ref = best + 1 if overlap(sent, self.chunks[best]) >= 0.4 else None
            clean = re.sub(r"\s*\[\d+\]", "", sent).strip()
            mapping[clean] = ref
            out.append((clean, ref))
        return out, mapping


if __name__ == "__main__":
    chunks = [
        "退货运费 由 买家 承担 例外 是 质量 问题",
        "七天 无理由 退货 从 签收 日 起 算",
        "退款 在 3 个 工作日 内 原路 返回",
    ]
    cm = CitationMapper(chunks)
    answer = ("退货运费由买家承担,质量问题除外 [1]。退货期为签收后七天 [2]。今天天气不错。")
    rows, mapping = cm.map_answer(answer)
    for text, ref in rows:
        print(f"  句子: {text[:24]:<26} 引用: {ref}")
    assert mapping["退货运费由买家承担,质量问题除外。"] == 1
    assert mapping["退货期为签收后七天。"] == 2
    unsourced = [t for t, r in rows if r is None]
    print("无来源句:", unsourced)
    assert unsourced == ["今天天气不错。"], "完全无来源的句子必须被标记"
    print("引用映射与 unsourced 标记完成,可交给忠实度校验")
