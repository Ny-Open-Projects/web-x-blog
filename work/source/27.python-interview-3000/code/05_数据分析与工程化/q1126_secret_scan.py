import re

PATTERNS = [
    ("aws-key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("generic-secret", re.compile(r"(?i)(password|secret)\s*=\s*['\"][^'\"]{8,}")),
    ("private-key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
]
FILES = {
    "app.py": "token = 'abcd1234efgh'\n",
    "conf.yml": "password = \"hunter2secret\"\n",
    "readme.md": "hello\n",
}

def scan(files):
    hits = []
    for path, text in files.items():
        for i, line in enumerate(text.splitlines(), 1):
            for name, pat in PATTERNS:
                if pat.search(line):
                    hits.append((path, i, name))
    return hits

for path, line, kind in scan(FILES):
    print(f"{path}:{line} 疑似 {kind}")
print("接入 pre-commit 与 CI:发现即阻断;已泄露先轮换凭证再清历史")
