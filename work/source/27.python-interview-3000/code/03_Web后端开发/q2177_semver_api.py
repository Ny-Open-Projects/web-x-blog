"""语义化版本在 API 的落地: 同一 major 内的兼容承诺检查(纯标准库)。"""

CHANGE_TYPES = {
    "add_optional_field": ("minor", True),
    "add_endpoint": ("minor", True),
    "add_enum_value": ("minor", True),
    "add_optional_param": ("minor", True),
    "remove_field": ("major", False),
    "add_required_param": ("major", False),
    "narrow_type": ("major", False),
    "fix_validation_bug": ("patch", True),
}


def next_version(old, changes):
    """old: (major, minor, patch); 返回允许的新版本, 破坏性变更返回 None。"""
    major, minor, patch = old
    violations = [(c, CHANGE_TYPES[c][0]) for c in changes if not CHANGE_TYPES[c][1]]
    if violations:
        return None, violations
    if any(CHANGE_TYPES[c][0] == "minor" for c in changes):
        return (major, minor + 1, 0), violations
    return (major, minor, patch + 1), violations


cases = [
    ((1, 4, 2), ["add_optional_field", "fix_validation_bug"]),
    ((1, 4, 2), ["add_enum_value"]),
    ((1, 4, 2), ["remove_field"]),
    ((1, 4, 2), ["add_required_param"]),
]
for old, changes in cases:
    version, violations = next_version(old, changes)
    print("{:44s} -> {}".format(str(changes), version if version else "no-go " + str(violations)))
assert next_version((1, 4, 2), ["add_optional_field"])[0] == (1, 5, 0)
print("要点: minor 承诺只增不改, patch 只修不碰契约, 出现破坏项必须换 major 路径; 判定要自动化而不是靠记忆")
