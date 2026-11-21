"""工具结果超长治理:超限裁剪加游标分页,截断有标记,续读可取剩余部分。"""


class ResultGovernor:
    """工具结果门卫:单条结果超预算就截断,给出 cursor 让 Agent 需要时再取下一段。"""

    def __init__(self, page_chars=60):
        self.page_chars = page_chars
        self.buffers = {}                  # cursor_id -> 剩余文本
        self.seq = 0

    def shape(self, tool, raw):
        """返回 {"text", "truncated", "cursor"};短结果原样透传。"""
        if len(raw) <= self.page_chars:
            return {"text": raw, "truncated": False, "cursor": None, "tool": tool}
        self.seq += 1
        cid = f"{tool}:{self.seq}"
        self.buffers[cid] = raw[self.page_chars:]
        return {"text": raw[:self.page_chars] + "…[截断 共" + str(len(raw)) + "字]",
                "truncated": True, "cursor": cid, "tool": tool}

    def more(self, cursor):
        """按 cursor 续取下一页;取完返回 has_more False 并释放缓冲。"""
        rest = self.buffers.get(cursor)
        if rest is None:
            return {"text": "", "has_more": False, "cursor": None}
        if len(rest) <= self.page_chars:
            del self.buffers[cursor]
            return {"text": rest, "has_more": False, "cursor": None}
        self.buffers[cursor] = rest[self.page_chars:]
        return {"text": rest[:self.page_chars], "has_more": True, "cursor": cursor}

    def live_buffers(self):
        return len(self.buffers)


if __name__ == "__main__":
    gov = ResultGovernor(page_chars=50)
    big = "日志行。" * 30                        # 120 字
    shaped = gov.shape("read_log", big)
    assert shaped["truncated"] is True and shaped["cursor"] == "read_log:1"
    assert len(shaped["text"]) <= 50 + 12, "截断页不能显著超出预算"

    page2 = gov.more(shaped["cursor"])
    assert page2["has_more"] is True and page2["cursor"] == shaped["cursor"]
    page3 = gov.more(shaped["cursor"])
    assert page3["has_more"] is False and gov.live_buffers() == 0

    joined = shaped["text"].split("…")[0] + page2["text"] + page3["text"]
    assert joined == big, "分页拼回必须还原完整原文"
    assert gov.live_buffers() == 0, "取完必须释放缓冲 防止内存泄漏"

    small = gov.shape("get_time", "12:00")
    assert small["truncated"] is False and small["cursor"] is None
    exhausted = gov.more("read_log:1")
    assert exhausted == {"text": "", "has_more": False, "cursor": None}
    print("结果治理通过:120 字结果切成 3 页,拼回原文一致,缓冲随取随清")
