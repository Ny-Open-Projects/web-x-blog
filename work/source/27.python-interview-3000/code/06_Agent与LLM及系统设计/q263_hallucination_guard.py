"""幻觉防线演示:引用约束 Prompt + 输出后置校验,不合格触发降级。"""

SYSTEM_CONSTRAINT = ("仅根据下面提供的材料回答问题。"
                     "如果材料中没有答案,必须原样输出:材料中未提及。")


class GuardedRAG:
    def __init__(self, llm):
        self.llm = llm

    def check(self, answer: str, evidence: str) -> bool:
        """后置校验:答案与证据做字符级重叠度检查(拒答视为合规)。"""
        if "材料中未提及" in answer:
            return True  # 合规的拒答
        chars = set(answer) - set("。,、 ")
        if not chars:
            return True
        overlap = len(chars & set(evidence)) / len(chars)
        return overlap >= 0.6

    def answer(self, question: str, evidence: str) -> str:
        raw = self.llm.chat([{"role": "system", "content": SYSTEM_CONSTRAINT + evidence},
                             {"role": "user", "content": question}])
        if self.check(raw, evidence):
            return raw
        return "回答未通过证据校验,已拦截"


class GoodFakeLLM:
    def chat(self, messages):
        return "知识库文档支持 PDF 格式上传。"


class BadFakeLLM:
    def chat(self, messages):
        return "知识库支持上传视频并且能自动剪辑视频。"


if __name__ == "__main__":
    evidence = "知识库支持上传 PDF 和 Word 文档,单文件不超过 50MB。"
    for llm in (GoodFakeLLM(), BadFakeLLM()):
        print(GuardedRAG(llm).answer("支持什么格式?", evidence))
