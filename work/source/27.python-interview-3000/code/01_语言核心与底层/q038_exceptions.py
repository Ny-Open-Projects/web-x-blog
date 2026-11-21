class AppError(Exception):
    """业务异常基类"""

class NotFound(AppError):
    pass

class PermissionDenied(AppError):
    pass

def load_user(uid):
    db = {1: "alice"}
    if uid not in db:
        raise NotFound(f"user {uid} not found")
    return db[uid]

def get_profile(uid):
    try:
        return load_user(uid)
    except NotFound as err:
        raise PermissionDenied("profile hidden") from err

if __name__ == "__main__":
    try:
        get_profile(99)
    except AppError as e:
        print(type(e).__name__, "-", e)
        print("cause:", type(e.__cause__).__name__)

    try:
        raise ValueError("inner")
    except ValueError:
        try:
            raise RuntimeError("outer") from None   # 抑制链,慎用
        except RuntimeError as e:
            print("outer caught:", e)
            print("__cause__:", e.__cause__, "| __context__:", type(e.__context__).__name__)
