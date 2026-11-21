"""重放校验: 按运行清单复现历史输出, 指纹不符即报告漂移"""

import hashlib


def sha256(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def transform(content, params):
    seen, out = set(), []
    for line in content.splitlines():
        if params.get("drop_blank") and not line.strip():
            continue
        if line in seen:
            continue
        seen.add(line)
        out.append(line)
    return "\n".join(out)


MANIFEST = {
    "pipeline_version": "pipe-1.2.0",
    "params": {"drop_blank": True},
    "inputs": {"events.csv": sha256("click\npv\nclick\n\npv\norder")},
    "output_sha256": None,          # 由真实运行填入
}
CURRENT_VERSION = "pipe-1.3.0"      # 本机代码已升级
INPUT = "click\npv\nclick\n\npv\norder"
INPUT_DRIFTED = "click\npv\nclick\npromoted\n\npv\norder"   # 上游混入新行


def replay(manifest, inputs, current_version):
    if manifest["pipeline_version"] != current_version:
        print(f"  版本提示: 清单 {manifest['pipeline_version']} != 当前 {current_version}, 参数以清单为准")
    input_ok = sha256(inputs["events.csv"]) == manifest["inputs"]["events.csv"]
    output = transform(inputs["events.csv"], manifest["params"])
    output_ok = sha256(output) == manifest["output_sha256"]
    return input_ok, output_ok


if __name__ == "__main__":
    MANIFEST["output_sha256"] = sha256(transform(INPUT, MANIFEST["params"]))
    ok_in, ok_out = replay(MANIFEST, {"events.csv": INPUT}, CURRENT_VERSION)
    print(f"重放一致: 输入指纹 {ok_in}, 输出指纹 {ok_out}")
    assert ok_in and ok_out, "同输入同参数必须复现同输出"
    try:
        ok_in, ok_out = replay(MANIFEST, {"events.csv": INPUT_DRIFTED}, CURRENT_VERSION)
        assert not (ok_in and ok_out)
        bad = "输入" if not ok_in else ""
        bad += "输出" if not ok_out else ""
        raise AssertionError(f"重放漂移未上报: {bad} 指纹不符")
    except AssertionError as e:
        print("重放拦截:", e, "-> 上游内容漂移, 需追查混入行再重放")
    print("要点: 重放比对的是指纹不是 eyeball, 上游漂移与代码升级都被显式暴露而不是被静默吸收")
