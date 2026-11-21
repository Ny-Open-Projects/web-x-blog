"""string.Template 的安全替换:substitute 与 safe_substitute 的分工。"""
from string import Template

WELCOME = Template("你好 $name,你的订单 $order_id 已${action}。")


def render(template_text, mapping):
    """渲染用户可编辑的模板:缺变量时给出可读的错误。"""
    try:
        return Template(template_text).substitute(mapping)
    except KeyError as e:
        raise KeyError(f"模板缺少变量 {e},请检查上游数据") from None


if __name__ == "__main__":
    print("完整映射:", WELCOME.substitute(name="小明", order_id="A1024", action="发货"))

    try:
        WELCOME.substitute(name="小明")
    except KeyError as e:
        print("substitute 严格模式:", e)

    print("safe 模式缺啥留啥:", WELCOME.safe_substitute(name="小明"))

    user_typed = "你好 $name,余额 $$balance"
    print("用户输入模板:", render(user_typed, {"name": "小红", "balance": "100"}))
