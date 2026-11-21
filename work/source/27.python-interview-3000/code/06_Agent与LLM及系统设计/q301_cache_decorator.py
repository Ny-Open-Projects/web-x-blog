import functools
import time


def ttl_cache(seconds: float, maxsize: int = 128):
    def deco(fn):
        cache: dict = {}

        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            now = time.monotonic()
            hit = cache.get(key)
            if hit and hit[0] > now:
                return hit[1]
            value = fn(*args, **kwargs)
            if len(cache) >= maxsize:  # 简单淘汰:清空过期项
                for k in [k for k, v in cache.items() if v[0] <= now]:
                    del cache[k]
            cache[key] = (now + seconds, value)
            return value

        wrapper.invalidate = lambda *a, **kw: cache.pop(
            (a, tuple(sorted(kw.items()))), None)
        return wrapper
    return deco


_calls = 0


@ttl_cache(seconds=1.0)
def get_user_profile(uid: str) -> dict:
    global _calls
    _calls += 1
    return {"id": uid, "level": 3}


if __name__ == "__main__":
    get_user_profile("u1"); get_user_profile("u1")
    print("calls:", _calls)          # 1,命中缓存
    get_user_profile.invalidate("u1")
    get_user_profile("u1")
    print("calls after invalidate:", _calls)  # 2
