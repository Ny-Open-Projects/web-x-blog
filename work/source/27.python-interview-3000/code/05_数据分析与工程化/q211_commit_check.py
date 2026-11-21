import re

PATTERN = re.compile(
    r"^(feat|fix|refactor|test|docs|chore|perf|ci)(\(.+\))?: .{1,72}$"
)

def valid_commit(msg: str) -> bool:
    return bool(PATTERN.match(msg))

def test_conventional_commits():
    assert valid_commit("feat(auth): 支持 OAuth2 登录")
    assert valid_commit("fix: 修复越界")
    assert not valid_commit("改了点东西")
    assert not valid_commit("feat: " + "x" * 100)
