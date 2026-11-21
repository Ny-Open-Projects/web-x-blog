"""Cache-Control 解析与新鲜度判定(纯标准库)。"""


def parse_cache_control(header):
    directives = {}
    for part in header.split(","):
        part = part.strip()
        if not part:
            continue
        if "=" in part:
            key, _, value = part.partition("=")
            directives[key.strip()] = value.strip().strip('"')
        else:
            directives[part] = True
    return directives


def num(directives, key):
    value = directives.get(key)
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def cache_decision(directives, age):
    if directives.get("no-store"):
        return "do-not-store", 0
    if directives.get("no-cache"):
        return "revalidate-first", 0
    max_age = num(directives, "max-age")
    if age < max_age:
        return "fresh", max_age - age
    swr = num(directives, "stale-while-revalidate")
    if age < max_age + swr:
        return "serve-stale-then-refresh", max_age + swr - age
    return "refetch", 0


cases = [
    ("public, max-age=60", 30),
    ("public, max-age=60, stale-while-revalidate=300", 100),
    ("public, max-age=60, stale-while-revalidate=300", 500),
    ("no-cache", 0),
    ("no-store", 0),
]
for header, age in cases:
    print(f"{header:52s} age={age:3d} -> {cache_decision(parse_cache_control(header), age)}")
