"""code review 清单的自检脚本骨架:静态检查 + 风险模式扫描。"""
import ast
import sys

RISKY_PATTERNS = {
    "eval": "禁止 eval 动态执行",
    "exec": "禁止 exec 动态执行",
    "shell=True": "禁止 shell=True 拼接命令",
    "except:": "禁止裸 except",
    "password = \"": "疑似硬编码密码",
    "verify=False": "禁止关闭 TLS 校验",
    "utcnow": "utcnow 已废弃, 用 now(timezone.utc)",
}


def scan_source(code: str) -> list:
    findings = []
    for lineno, line in enumerate(code.splitlines(), 1):
        for pattern, msg in RISKY_PATTERNS.items():
            if pattern in line:
                findings.append(f"L{lineno}: {msg} -> {line.strip()}")
    # 语法层面: 能解析才继续
    try:
        ast.parse(code)
    except SyntaxError as e:
        findings.append(f"语法错误: {e}")
    return findings


SAMPLE = '''
import subprocess
def run(user):
    try:
        subprocess.run("ping " + user, shell=True)
    except:
        pass
secret = "hunter2"
'''

if __name__ == "__main__":
    findings = scan_source(SAMPLE)
    for f in findings:
        print("[风险]", f)
    print("共发现", len(findings), "处, 均需在上线前修复")
    # 演示脚本固定 exit 0; 接入 CI 时改为 sys.exit(1 if findings else 0) 阻断合并
    sys.exit(0)
