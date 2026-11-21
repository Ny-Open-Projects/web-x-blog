import sqlite3


class RepoError(Exception):
    """仓储层领域异常基类。"""


class NotFoundError(RepoError):
    pass


class ConstraintError(RepoError):
    pass


class FakeDB:
    """模拟底层驱动:抛底层异常。"""

    def query_user(self, uid):
        raise LookupError("no row for uid=%s" % uid)

    def insert_user(self, name):
        raise sqlite3.IntegrityError("UNIQUE constraint failed: users.name")


class UserRepo:
    def __init__(self, db):
        self.db = db

    def get_user(self, uid):
        try:
            return self.db.query_user(uid)
        except LookupError as err:
            raise NotFoundError("user %s not found in users table" % uid) from err

    def add_user(self, name):
        try:
            self.db.insert_user(name)
        except sqlite3.IntegrityError as err:
            raise ConstraintError("user name %r already exists" % name) from err


def handle_request(repo, action):
    """API 边界:把领域异常转成响应,底层类型不再外泄。"""
    try:
        return {"ok": True, "data": action()}
    except NotFoundError as err:
        return {"ok": False, "error": "not_found", "message": str(err)}
    except ConstraintError as err:
        return {"ok": False, "error": "conflict", "message": str(err)}


if __name__ == "__main__":
    repo = UserRepo(FakeDB())
    print(handle_request(repo, lambda: repo.get_user(42)))
    print(handle_request(repo, lambda: repo.add_user("alice")))

    # 验证原因链没断
    try:
        repo.get_user(7)
    except NotFoundError as err:
        print("cause type  :", type(err.__cause__).__name__)
        print("cause detail:", err.__cause__)
