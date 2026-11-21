"""切换后的会话粘性:故障切换后同会话粘住备用供应商,新会话仍回主路保缓存。"""


class StickyRouter:
    def __init__(self, primary, backups):
        self.primary = primary
        self.backups = list(backups)
        self.session_map = {}      # session -> 当前供应商
        self.switch_count = 0

    def pick(self, session):
        return self.session_map.get(session, self.primary)

    def report_failure(self, session, provider):
        """只有当前在用供应商的故障上报才会触发迁移,过期上报忽略。"""
        if provider != self.pick(session):
            return None
        chain = [self.pick(session)] + [b for b in self.backups
                                        if b != self.pick(session)]
        idx = 0
        if idx + 1 < len(chain):
            self.session_map[session] = chain[idx + 1]
            self.switch_count += 1
            return chain[idx + 1]
        return None

    def end_session(self, session):
        """会话结束清粘性:新会话从主路开始,不继承旧会话的切换状态。"""
        return self.session_map.pop(session, None)


if __name__ == "__main__":
    router = StickyRouter("openai", ["azure", "bedrock"])

    assert router.pick("s1") == "openai", "新会话默认主路"
    assert router.pick("s2") == "openai"

    nxt = router.report_failure("s1", "openai")
    assert nxt == "azure"
    assert router.pick("s1") == "azure" and router.pick("s2") == "openai", \
        "只有故障会话切走,别的会话不跟风"

    # 粘住期间对 azure 的继续上报才推进;对已弃用 openai 的迟到上报忽略
    assert router.report_failure("s1", "azure") == "bedrock"
    assert router.report_failure("s1", "openai") is None, "过期上报不得改路由"
    assert router.pick("s1") == "bedrock"

    router.end_session("s1")
    assert router.pick("s1") == "openai", "会话结束后粘性清除"

    assert router.switch_count == 2
    print("粘性路由通过:故障会话切走且逐级推进,迟到上报忽略,会话结束清粘")
