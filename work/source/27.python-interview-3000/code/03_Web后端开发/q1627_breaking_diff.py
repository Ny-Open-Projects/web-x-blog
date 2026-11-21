"""OpenAPI 破坏性变更分级: diff 分类器(纯标准库)。"""

V1 = {
    "required": ["amount"],
    "response_fields": {"id": "str", "status": "str", "amount": "float"},
}
V2 = {
    "required": ["amount", "currency"],        # 新增必填 -> 破坏
    "response_fields": {"id": "str", "status": "str", "amount": "float", "coupon": "str|none"},
}
V3 = {
    "required": ["amount"],                     # 与 V1 相同 -> 不因必填破坏
    "response_fields": {"id": "str", "amount": "decimal"},   # 删字段 + 改类型 -> 破坏
}


def diff_operation(old, new, label):
    findings = []
    removed = sorted(set(old["response_fields"]) - set(new["response_fields"]))
    added = sorted(set(new["response_fields"]) - set(old["response_fields"]))
    for f in removed:
        findings.append(("breaking", f"{label}: 响应删除字段 {f}"))
    for f in added:
        findings.append(("compatible", f"{label}: 响应新增字段 {f}"))
    for f in sorted(set(old["response_fields"]) & set(new["response_fields"])):
        if old["response_fields"][f] != new["response_fields"][f]:
            findings.append(("breaking", f"{label}: 字段 {f} 类型变更"))
    for f in sorted(set(new["required"]) - set(old["required"])):
        findings.append(("breaking", f"{label}: 请求新增必填 {f}"))
    for f in sorted(set(old["required"]) - set(new["required"])):
        findings.append(("compatible", f"{label}: 请求放宽必填 {f}"))
    return findings


def verdict(findings):
    bad = [msg for level, msg in findings if level == "breaking"]
    return "阻断合并" if bad else "放行"


for old, new, label in ((V1, V2, "V1->V2"), (V1, V3, "V1->V3")):
    fs = diff_operation(old, new, label)
    for level, msg in fs:
        print(f"[{level:10}] {msg}")
    print("结论:", verdict(fs))
    print()

print("经验: 新增可选输出、放宽校验是兼容; 删字段、改类型、加必填是破坏")
