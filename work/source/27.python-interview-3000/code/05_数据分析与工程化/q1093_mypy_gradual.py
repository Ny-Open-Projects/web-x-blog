from typing import Optional

def normalize_email(raw: Optional[str]) -> str:
    if raw is None:
        return "unknown@example.com"
    return raw.strip().lower()

def parse_amount(text: str) -> float:
    try:
        return float(text.replace(",", ""))
    except ValueError:
        return 0.0

if __name__ == "__main__":
    print(normalize_email("  Bob@X.com "))
    print(parse_amount("1,234.5"))
    # 治理配置示例:
    # [tool.mypy] python_version = "3.12"
    # files = ["src"] ; disallow_untyped_defs = true ; ignore_missing_imports = true
    # 存量目录用 per-module overrides 逐个收紧
