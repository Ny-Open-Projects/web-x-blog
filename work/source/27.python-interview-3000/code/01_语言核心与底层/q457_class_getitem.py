class Repository:
    """支持 Repository[Entity] 的参数化语法"""
    _bound = {}

    def __class_getitem__(cls, entity):
        key = (cls, entity)
        if key not in Repository._bound:
            name = f"{cls.__name__}[{entity.__name__}]"
            Repository._bound[key] = type(name, (cls,), {"entity": entity})
        return Repository._bound[key]

class User:
    pass

class Order:
    pass

if __name__ == "__main__":
    UserRepo = Repository[User]
    OrderRepo = Repository[Order]
    print(type(UserRepo).__name__, UserRepo.entity)
    print(issubclass(UserRepo, Repository))
    print(UserRepo is Repository[User])   # 同参数返回同一子类
    print(UserRepo is OrderRepo)
