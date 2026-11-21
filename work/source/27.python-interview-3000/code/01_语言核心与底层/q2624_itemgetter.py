"""itemgetter 与 attrgetter:多键排序的标准写法。"""
from operator import attrgetter, itemgetter

rows = [
    {"dept": "b", "age": 30},
    {"dept": "a", "age": 40},
    {"dept": "a", "age": 20},
]


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == "__main__":
    print("多键排序:", sorted(rows, key=itemgetter("dept", "age")))
    print("单键取值:", itemgetter("dept")(rows[0]))

    people = [Person("bob", 30), Person("amy", 25)]
    print("attrgetter:", [p.name for p in sorted(people, key=attrgetter("age"))])
    print("点路径:", attrgetter("age")(people[0]))

    # 需要转换时才回 lambda
    print("转换型 key:", sorted(rows, key=lambda r: -r["age"]))
