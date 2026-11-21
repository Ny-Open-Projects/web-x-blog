"""接口回归用例自动生成: 从契约生成正向与必填缺失用例(纯标准库)。"""

CONTRACT = [
    {"endpoint": "POST /v1/goods", "required": ["name", "price"]},
    {"endpoint": "GET /v1/goods/{id}", "required": ["id"]},
]
SAMPLES = {"name": "demo", "price": 9.9, "id": "g-1"}


def gen_cases(spec):
    """正向一条, 每个必填字段缺失一条。"""
    cases = [{"name": "happy_path",
              "params": {k: SAMPLES.get(k, "x") for k in spec["required"]},
              "expect_status": 200}]
    for field in spec["required"]:
        params = {k: SAMPLES.get(k, "x") for k in spec["required"] if k != field}
        cases.append({"name": "missing_" + field, "params": params,
                      "expect_status": 400, "assert_field": field})
    return cases


total = 0
for spec in CONTRACT:
    print("##", spec["endpoint"])
    for case in gen_cases(spec):
        total += 1
        print("  test_{}_{:16s} params={} expect={}".format(
            spec["endpoint"].split()[0].lower(), case["name"],
            case["params"], case["expect_status"]))
print("共生成 {} 条用例; 契约即用例来源, 字段增删自动反映到回归集".format(total))
assert total == 5
print("要点: 自动生成保证覆盖率下限——每必填字段一条缺失用例; 业务语义断言仍要人补")
