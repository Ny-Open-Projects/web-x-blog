"""用决策表模拟向量库选型:按规模、现有栈、功能需求打分。"""


RULES = [
    # (条件函数, 推荐产品, 理由)
    (lambda n, stack, hybrid: n < 100_000 and "postgres" in stack,
     "pgvector", "复用现有 Postgres,运维零新增"),
    (lambda n, stack, hybrid: hybrid and n < 10_000_000,
     "Redis Stack / Elasticsearch", "原生混合检索与标量过滤"),
    (lambda n, stack, hybrid: n >= 10_000_000,
     "Milvus", "亿级向量,HNSW 与分片能力成熟"),
]


def choose_vector_db(num_vectors: int, existing_stack: str, need_hybrid: bool) -> tuple[str, str]:
    for cond, product, reason in RULES:
        if cond(num_vectors, existing_stack, need_hybrid):
            return product, reason
    return "FAISS(自建)", "轻量嵌入式,需自行管理持久化"


if __name__ == "__main__":
    cases = [(50_000, "postgres+django", False),
             (1_000_000, "java微服务", True),
             (200_000_000, "golang", False)]
    for n, stack, hy in cases:
        product, reason = choose_vector_db(n, stack, hy)
        print(f"{n=:>12_} {stack=:<16} hybrid={hy} -> {product} | {reason}")
