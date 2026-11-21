import os

def env_int(key, default=0):
    raw = os.environ.get(key)
    if raw is None:
        return default
    try:
        return int(raw)
    except ValueError:
        raise ValueError(f"env {key}={raw!r} is not an int") from None

def env_bool(key, default=False):
    return os.environ.get(key, "").strip().lower() in {"1", "true", "yes", "on"}

if __name__ == "__main__":
    os.environ["APP_PORT"] = "8080"
    os.environ["APP_DEBUG"] = "yes"
    print("port:", env_int("APP_PORT"), "| missing:", env_int("APP_MISSING", 80))
    print("debug:", env_bool("APP_DEBUG"), "| unset:", env_bool("APP_MISSING"))

    os.environ["APP_PORT"] = "abc"
    try:
        env_int("APP_PORT")
    except ValueError as e:
        print("bad config:", e)
