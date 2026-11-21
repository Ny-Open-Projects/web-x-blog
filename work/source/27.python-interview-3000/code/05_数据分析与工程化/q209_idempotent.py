import json
import pathlib


def load_state(path: pathlib.Path) -> dict:
    if path.exists():
        return json.loads(path.read_text())
    return {"processed": []}


def import_items(items: list[str], state_path: pathlib.Path) -> int:
    # 幂等导入:状态文件记录已处理的 item,重跑只处理增量
    state = load_state(state_path)
    done = set(state["processed"])
    imported = 0
    for item in items:
        if item not in done:
            state["processed"].append(item)
            imported += 1
    state_path.write_text(json.dumps(state))
    return imported


def test_rerun_is_noop(tmp_path):
    p = tmp_path / "state.json"
    assert import_items(["a", "b"], p) == 2
    assert import_items(["a", "b"], p) == 0  # 重跑不重复
    assert import_items(["c"], p) == 1
