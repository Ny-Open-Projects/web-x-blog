"""备份恢复演练:把最近备份恢复到沙箱并校验,坏备份当场拦截"""

import hashlib
import json
import os
import shutil
import tempfile

RESTORE_DIR = tempfile.mkdtemp(prefix="restore_demo_")

GOOD = {"rows": 1200, "data": list(range(1200))}
GOOD["checksum"] = hashlib.sha256(json.dumps(GOOD["data"]).encode()).hexdigest()
BAD = {"rows": 1200, "data": list(range(900)), "checksum": "deadbeef"}


def drill(backup):
    data = backup["data"]
    actual = hashlib.sha256(json.dumps(data).encode()).hexdigest()
    if actual != backup["checksum"]:
        return False, "校验和不匹配,备份已损坏"
    if len(data) != backup["rows"]:
        return False, f"行数不符 {len(data)} != {backup['rows']}"
    with open(os.path.join(RESTORE_DIR, "restored.json"), "w") as f:
        json.dump(data, f)
    return True, f"恢复成功,行数 {len(data)}"


if __name__ == "__main__":
    for name, b in (("good_backup", GOOD), ("bad_backup", BAD)):
        ok, msg = drill(b)
        print(f"{name}: {'通过' if ok else '未通过'} - {msg}")
    shutil.rmtree(RESTORE_DIR)
    print("要点:没恢复过的备份等于没备份;演练按固定周期跑,校验和与行数双检;演练失败要当事故处理,而不是改脚本让它变绿")
