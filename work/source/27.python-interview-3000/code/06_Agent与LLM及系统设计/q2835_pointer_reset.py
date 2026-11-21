"""Q2835 多轮对话的指针重置语义:软重置 硬重置与悬空指代。

用户说「重新开个话题」时,很多系统直接清空全部状态,把用户名、
偏好等还需要的事实一起丢了;另一些系统什么也不清,新话题里还残留
旧槽位。正确语义是分级:软重置清历史与未钉槽位、保留钉住的事实,
硬重置全清;重置后指代解析必须显式失败,逼系统开口问而不是瞎猜。
"""


class DialogueState:
    def __init__(self):
        self.history = []
        self.slots = {}
        self.pinned = set()

    def turn(self, text):
        self.history.append(text)

    def pin(self, key):
        self.pinned.add(key)

    def soft_reset(self):
        """软重置:清历史,槽位只留钉住的。"""
        self.history = []
        self.slots = {k: v for k, v in self.slots.items() if k in self.pinned}

    def hard_reset(self):
        """硬重置:历史 槽位 钉住关系全清。"""
        self.history = []
        self.slots = {}
        self.pinned = set()

    def resolve_pronoun(self):
        """指代解析:没有历史可锚定时必须显式失败。"""
        if len(self.history) < 1:
            return None
        return self.history[-1]


def main():
    st = DialogueState()
    st.turn("帮我查北京的天气")
    st.slots["user_city"] = "北京"
    st.slots["user_name"] = "王工"
    st.pin("user_name")
    # 软重置:话题重开,身份保留,城市这种话题槽位清掉
    st.soft_reset()
    assert st.history == [], st.history
    assert st.slots == {"user_name": "王工"}, st.slots
    assert st.resolve_pronoun() is None  # 历史空了,「它」无从解析
    # 用户接着说「它明天呢」——系统必须追问而不是猜
    need_ask = st.resolve_pronoun() is None
    assert need_ask is True
    # 硬重置:连钉住的身份一起清(退出登录场景)
    st.hard_reset()
    assert st.slots == {} and st.pinned == set(), (st.slots, st.pinned)
    print("软重置后槽位:", {"user_name": "王工"}, "悬空指代需追问:", need_ask)
    print("硬重置后全部清空,适合登出或换账号场景")


if __name__ == "__main__":
    main()
