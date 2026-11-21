"""多轮改写状态:槽位累积与指代消解,把「它呢」改写成可检索的完整查询。"""


class RewriteState:
    def __init__(self):
        self.slots = {}          # 跨轮累积的槽位:属性 时空 等
        self.last_topic = None   # 最近话题,供指代回填

    def update(self, extracted):
        """每轮从对话里抽取到的槽位进来,显式槽位覆盖旧值。"""
        if "topic" in extracted:
            self.last_topic = extracted["topic"]
        for k, v in extracted.items():
            if k != "topic":
                self.slots[k] = v

    def rewrite(self, query):
        q = query.strip()
        if q in ("它呢", "那它呢", "怎么样", "它怎么样"):
            if not self.last_topic:
                return query            # 无状态可回填,原样交给澄清流程
            parts = [self.last_topic]
            parts += ["%s=%s" % (k, v) for k, v in sorted(self.slots.items())]
            return " ".join(parts)
        if self.last_topic and self.last_topic not in q:
            return self.last_topic + " " + q
        return q


if __name__ == "__main__":
    st = RewriteState()
    st.update({"topic": "iPhone 17", "info": "价格"})
    assert st.rewrite("它呢") == "iPhone 17 info=价格", "指代回填话题与累积槽位"

    st.update({"region": "国行"})
    assert st.rewrite("那它呢") == "iPhone 17 info=价格 region=国行", "槽位只增不丢"

    # 换话题:topic 被覆盖,但 info region 仍然有效,继承到新话题
    st.update({"topic": "iPad Pro"})
    assert st.rewrite("它怎么样") == "iPad Pro info=价格 region=国行"

    # 正常查询:不带指代但要补话题前缀,保证检索向量不漂移
    st2 = RewriteState()
    st2.update({"topic": "退货政策"})
    assert st2.rewrite("时效是多久") == "退货政策 时效是多久"
    assert st2.rewrite("退货政策时效") == "退货政策时效", "已在查询里的话题不重复"

    # 冷启动无状态:不硬改写,交回澄清
    st3 = RewriteState()
    assert st3.rewrite("它呢") == "它呢"
    print("多轮改写通过:两轮累积槽位,话题切换槽位继承,冷启动不硬改写")
