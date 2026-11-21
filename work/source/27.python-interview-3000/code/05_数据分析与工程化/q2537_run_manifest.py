"""管道运行清单: 版本 参数 输入输出校验和, 给历史可复现留证据"""

import hashlib
import json


def sha256(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def transform(content, params):
    """确定性变换: 原地去重保序 + 可选过滤空行"""
    seen, out = set(), []
    for line in content.splitlines():
        if params.get("drop_blank") and not line.strip():
            continue
        if line in seen:
            continue
        seen.add(line)
        out.append(line)
    return "\n".join(out)


def run(version, params, inputs):
    manifest = {
        "pipeline_version": version,
        "params": params,
        "inputs": {name: sha256(body) for name, body in inputs.items()},
    }
    output = transform(inputs["events.csv"], params)
    manifest["output_sha256"] = sha256(output)
    return manifest, output


INPUT = "click\npv\nclick\n\npv\norder"
INPUT_CHANGED = "click\npv\nclick\ncart"      # 上游内容变了


if __name__ == "__main__":
    params = {"drop_blank": True}
    m1, out1 = run("pipe-1.2.0", params, {"events.csv": INPUT})
    m2, out2 = run("pipe-1.2.0", params, {"events.csv": INPUT})
    print(f"两次同参运行输出校验和一致: {m1['output_sha256'][:12]} == {m2['output_sha256'][:12]}")
    assert m1["output_sha256"] == m2["output_sha256"]
    print(f"输出内容: {out1.splitlines()}")
    m3, _ = run("pipe-1.2.0", params, {"events.csv": INPUT_CHANGED})
    assert m3["output_sha256"] != m1["output_sha256"]
    print(f"上游变更后校验和变化: {m1['output_sha256'][:12]} -> {m3['output_sha256'][:12]}")
    print("清单要素: 版本 + 参数 + 输入指纹 + 输出指纹, 四件套齐了历史才谈得上可复现")
    print(json.dumps(m1, ensure_ascii=False)[:100], "...")
