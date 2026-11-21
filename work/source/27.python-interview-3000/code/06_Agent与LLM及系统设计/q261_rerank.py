"""两阶段检索:向量召回 50 条中的 5 条演示,再用伪交叉编码器重排。"""
import random


def vector_recall(query: str, docs: list[str], top_k: int) -> list[str]:
    # 假设向量召回把目标文档排在第 3 位,返回 top_k
    shuffled = docs[:]
    random.Random(42).shuffle(shuffled)
    return shuffled[:top_k]


def cross_encoder_score(query: str, doc: str) -> float:
    """伪交叉编码:query 词与 doc 词的交集占比越高越相关。"""
    q_terms = set(query)
    d_terms = set(doc)
    return len(q_terms & d_terms) / max(1, len(q_terms))


def rerank(query: str, candidates: list[str], top_n: int = 2) -> list[str]:
    scored = sorted(candidates, key=lambda d: -cross_encoder_score(query, d))
    return scored[:top_n]


if __name__ == "__main__":
    docs = ["Python GIL 限制多线程并行",
            "RAG 通过检索增强回答准确性",
            "向量数据库支持 ANN 检索",
            "重排模型提升检索精度",
            "今天中午吃什么好",
            "检索增强生成 RAG 的完整链路"]
    query = "RAG 检索"
    recall = vector_recall(query, docs, top_k=4)
    print("召回:", recall)
    print("重排后:", rerank(query, recall, top_n=2))
