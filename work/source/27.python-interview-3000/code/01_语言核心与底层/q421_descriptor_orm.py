import weakref

class Field:
    def __set_name__(self, owner, name):    # 类体创建时自动调用
        self.name, self.attname = name, "_" + name
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self                     # 类访问返回字段对象本身,ORM 靠这拿元数据
        return getattr(obj, self.attname)
    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise TypeError(f"{self.name} must be str")
        obj.__dict__[self.attname] = value
        obj.__dirty__.add(self.name)        # 数据描述符优先于实例 dict

class Model:
    name = Field()
    def __init__(self):
        self.__dirty__ = set()

class User(Model):
    pass

u = User()
u.name = "alice"                 # 走 Field.__set__
print("dirty:", u.__dirty__)
print("via descriptor:", u.name) # 走 Field.__get__
try:
    u.name = 42
except TypeError as e:
    print("validation:", e)

print("类访问返回字段:", User.name.__class__.__name__)
print("查找优先级演示: 数据描述符压过实例 dict")
