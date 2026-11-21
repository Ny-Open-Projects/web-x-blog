"""字段级校验管线:声明式规则组合,error 阻断 warn 放行,产出统一校验报告。"""


class Rule:
    def __init__(self, name, level, fn):
        self.name, self.level, self.fn = name, level, fn

    def check(self, obj):
        try:
            ok, msg = self.fn(obj)
            return None if ok else f"{self.name}: {msg}"
        except Exception as e:
            return f"{self.name}: 规则异常 {e}"


class ValidatorPipeline:
    def __init__(self):
        self.rules = []

    def add(self, rule):
        self.rules.append(rule)
        return self

    def run(self, obj, scenario="default"):
        errors, warns = [], []
        for r in self.rules:
            if scenario not in r.scenarios:
                continue
            err = r.check(obj)
            if err:
                (errors if r.level == "error" else warns).append(err)
        return {"passed": not errors, "errors": errors, "warns": warns}


def rule(name, level, scenarios=("default",)):
    def deco(fn):
        r = Rule(name, level, fn)
        r.scenarios = scenarios
        return r
    return deco


@rule("金额为正数", "error")
def r_amount(o):
    return o.get("amount", 0) > 0, "amount 必须大于 0"


@rule("币种合法", "error")
def r_currency(o):
    return o.get("currency") in {"CNY", "USD"}, f"非法币种 {o.get('currency')}"


@rule("备注过长提醒", "warn")
def r_note(o):
    return len(o.get("note", "")) <= 50, "note 超过 50 字,建议精简"


if __name__ == "__main__":
    pipe = ValidatorPipeline().add(r_amount).add(r_currency).add(r_note)
    report = pipe.run({"amount": -5, "currency": "JPY", "note": "x" * 60})
    print("阻断:", report["errors"])
    print("警告:", report["warns"])
    assert not report["passed"] and len(report["errors"]) == 2
    ok_report = pipe.run({"amount": 10, "currency": "CNY", "note": ""})
    assert ok_report["passed"]
    print("正常单通过,error 阻断 warn 放行机制生效")
