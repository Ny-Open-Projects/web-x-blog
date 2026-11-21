"""分页参数的统一校验与归一化(纯标准库)。"""

DEFAULT_PAGE, DEFAULT_SIZE, MAX_SIZE = 1, 20, 100


def normalize_page_params(page, size):
    """返回 (params, errors):非法时 params 为 None 并给出全部错误。"""
    try:
        p, s = int(page), int(size)
    except (TypeError, ValueError):
        return None, ["page 与 size 必须是整数"]
    errors = []
    if p < DEFAULT_PAGE:
        errors.append(f"page 必须 >= {DEFAULT_PAGE}")
    if s < 1:
        errors.append("size 必须 >= 1")
    if s > MAX_SIZE:
        errors.append(f"size 不得超过 {MAX_SIZE}")
    if errors:
        return None, errors
    return {"page": p, "size": s, "offset": (p - 1) * s}, []


print(normalize_page_params("2", "50"))
print(normalize_page_params("0", "500"))
print(normalize_page_params("abc", "20"))
