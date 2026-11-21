"""builder 链式调用:每步返回 self,build 时校验并冻结成品。"""
import copy


class QueryBuilder:
    def __init__(self):
        self._table = None
        self._wheres = []
        self._limit = None

    def table(self, name):
        self._table = name
        return self

    def where(self, cond):
        self._wheres.append(cond)
        return self

    def limit(self, n):
        self._limit = n
        return self

    def build(self):
        if not self._table:
            raise ValueError("必须先指定 table")
        sql = "SELECT * FROM " + self._table
        if self._wheres:
            sql += " WHERE " + " AND ".join(self._wheres)
        if self._limit is not None:
            sql += " LIMIT " + str(self._limit)
        return sql


class FrozenBuilder(QueryBuilder):
    """不可变变体:每个配置方法返回副本,可复用可缓存。"""

    def table(self, name):
        new = copy.deepcopy(self)
        new._table = name
        return new

    def where(self, cond):
        new = copy.deepcopy(self)
        new._wheres.append(cond)
        return new


if __name__ == "__main__":
    sql = QueryBuilder().table("users").where("age > 18").where("active = 1").limit(10).build()
    print(sql)

    base = QueryBuilder().table("orders")
    print(base.where("paid = 1").build())
    print("可变 builder 会累积:", base.where("paid = 0").build())

    fb = FrozenBuilder().table("a")
    print("不可变链互不影响:", fb.table("b")._table, "与", fb._table)
