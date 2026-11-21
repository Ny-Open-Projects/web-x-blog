from __future__ import annotations

import os
from typing import Optional

def load_secret(key: str, fallback_file: Optional[str] = None) -> str:
    value = os.environ.get(key)
    if value:
        return value
    if fallback_file and os.path.exists(fallback_file):
        with open(fallback_file, "r", encoding="utf-8") as f:
            return f.read().strip()          # docker/kubernetes secret 文件挂载
    raise RuntimeError(f"缺少密钥 {key}")    # 启动即失败

os.environ["DB_PASSWORD"] = "from-env"
print("环境变量注入:", load_secret("DB_PASSWORD") != "")
try:
    load_secret("NOT_EXIST")
except RuntimeError as e:
    print("fail-fast:", e)
