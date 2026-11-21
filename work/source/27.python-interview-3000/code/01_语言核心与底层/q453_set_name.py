class Column:
    """声明式字段:自动以属性名作为列名"""
    def __init__(self, coltype, colname=None):
        self.coltype = coltype
        self.colname = colname

    def __set_name__(self, owner, name):
        self.colname = self.colname or name
        owner._columns = getattr(owner, "_columns", ()) + (self,)

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.colname)

    def __set__(self, obj, value):
        if not isinstance(value, self.coltype):
            raise TypeError(f"{self.colname}: {self.coltype.__name__} required")
        obj.__dict__[self.colname] = value

class User:
    username = Column(str)
    age = Column(int, colname="user_age")

    def __init__(self, username, age):
        self.username = username
        self.age = age

if __name__ == "__main__":
    u = User("alice", 30)
    print(u.username, u.age)
    print("columns:", [c.colname for c in User._columns])
    try:
        u.age = "old"
    except TypeError as e:
        print("rejected:", e)
