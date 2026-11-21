"""__set_name__ 当调试钩子:实例复用的早期报警。"""


class Field:
    def __set_name__(self, owner, name):
        prev = getattr(self, "slot", None)
        if prev is not None:
            raise TypeError("Field 实例被复用: " + prev + " 与 " + name)
        self.slot = name
        self.owner = owner.__name__

    def describe(self):
        return self.owner + "." + self.slot


class Article:
    id = Field()
    title = Field()


def reuse_alarm():
    shared = Article.id                    # 反面用法:把已归属的实例再挂到新类
    try:
        type("Comment", (), {"body": shared})
    except RuntimeError as e:
        # 3.9 会把 __set_name__ 里的 TypeError 包成 RuntimeError,原异常在 __context__
        return str(e)[:42] + " | 原因: " + str(e.__context__.__class__.__name__)
    return "没拦住"


if __name__ == "__main__":
    print("id 归属:", Article.id.describe(), "| title 归属:", Article.title.describe())
    print("复用报警:", reuse_alarm())
