"""实现递归切块:段落 -> 句子 -> 固定长度,带 overlap,尊重结构边界。"""
import re


def recursive_chunk(text: str, max_len: int = 40, overlap: int = 8) -> list[str]:
    # 先按结构边界(段落)切
    paras = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks: list[str] = []
    for para in paras:
        if len(para) <= max_len:
            chunks.append(para)
            continue
        # 段落过长再按句子切
        sents = re.split(r"(?<=[。!?])\s*", para)
        buf = ""
        for s in sents:
            if len(buf) + len(s) <= max_len:
                buf += s
            else:
                if buf:
                    chunks.append(buf)
                buf = (buf[-overlap:] if buf and overlap else "") + s
        if buf:
            chunks.append(buf)
    return chunks


if __name__ == "__main__":
    doc = ("RAG 检索增强生成是主流方案。它分为离线与在线两个阶段。\n\n"
           "切块要尊重语义边界,避免把一个完整句子切成两半。重叠区能缓解边界信息丢失。"
           "最后一步是评估检索质量,持续迭代。")
    for i, c in enumerate(recursive_chunk(doc, max_len=30, overlap=6)):
        print(f"chunk{i} ({len(c)}字): {c}")
