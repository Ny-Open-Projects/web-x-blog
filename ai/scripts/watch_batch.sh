#!/usr/bin/env bash
# 夜间守望：等 B1 / B2（或任意指定批次）全部落盘，或超时退出。
# 用法: watch_batch.sh B1 B2 [最长分钟]
cd /Users/Wang/Code/github/web-x-blog || exit 1
BATCHES="$1 $2"
MAXMIN="${3:-210}"
START=$(date +%s)

check() {
  /Users/Wang/.workbuddy/binaries/python/versions/3.13.12/bin/python3 - "$BATCHES" <<'PY'
import json, re, sys
from pathlib import Path
NIGHT = Path("ai/night"); TGT = Path("work/target/k8stop")
want = []
for b in sys.argv[1].split():
    want += json.loads((NIGHT / f"todo_{b}.json").read_text(encoding="utf-8"))
have = {re.match(r"^(\d+-\d+)_", f.name).group(1) for f in TGT.glob("*.md")
        if re.match(r"^\d+-\d+_", f.name)}
miss = [w["num"] for w in want if w["src"] not in have]
print(f"{len(want)-len(miss)}/{len(want)}")
if miss:
    print("缺:", ",".join(f"#{n}" for n in miss[:20]))
PY
}

while true; do
  NOW=$(date +%s)
  ELAPSED=$(( (NOW - START) / 60 ))
  RES=$(check)
  echo "[$(date '+%H:%M:%S')] 已过 ${ELAPSED}min :: $RES"
  LINE=$(echo "$RES" | head -1)
  A="${LINE%%/*}"; B="${LINE##*/}"
  if [ "$A" = "$B" ]; then echo "[守望] 全部落盘，退出"; exit 0; fi
  if [ "$ELAPSEDMIN" ] ; then :; fi
  if [ "$ELAPSED" -ge "$MAXMIN" ]; then echo "[守望] 超时 ${MAXMIN}min，退出"; exit 3; fi
  sleep 120
done
