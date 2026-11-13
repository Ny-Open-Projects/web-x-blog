#!/bin/bash
# verify_all.sh — 验证所有语言所有文件可运行并输出 PASS
# 用法: ./verify_all.sh [go|ts|java|python|all] [topic]
# 输出: _meta/verify_report_{lang}.txt

set -u
DSA="/Users/Wang/Code/github/web-x-blog/work/blog/courses/21.dsa"
META="$DSA/_meta"
mkdir -p "$META"

# macOS 无 timeout 命令，用 perl alarm 模拟
timeout() { perl -e 'alarm shift; exec @ARGV' "$@"; }

verify_go() {
  local report="$META/verify_report_go.txt"
  : > "$report"
  find "$DSA/code/go" -name "*.go" | sort | while read -r f; do
    out=$(cd /tmp && timeout 30 go run "$f" 2>&1 | tail -1)
    if echo "$out" | grep -q "PASS"; then
      echo "PASS $f" >> "$report"
    else
      echo "FAIL $f :: $out" >> "$report"
    fi
  done
  echo "Go: $(grep -c '^PASS' "$report") pass, $(grep -c '^FAIL' "$report") fail"
}

verify_ts() {
  local report="$META/verify_report_ts.txt"
  : > "$report"
  find "$DSA/code/ts" -name "*.ts" | sort | while read -r f; do
    out=$(cd /tmp && NODE_NO_WARNINGS=1 timeout 30 node "$f" 2>&1 | tail -1)
    if echo "$out" | grep -q "PASS"; then
      echo "PASS $f" >> "$report"
    else
      echo "FAIL $f :: $out" >> "$report"
    fi
  done
  echo "TS: $(grep -c '^PASS' "$report") pass, $(grep -c '^FAIL' "$report") fail"
}

verify_python() {
  # 老仓库 python 文件遵循"打印结果"约定而非统一输出 PASS，
  # 判据为：能独立运行且退出码 0（无异常），与历史 py_compile+语义 验收口径一致
  local report="$META/verify_report_python.txt"
  : > "$report"
  find "$DSA/code/python" -name "solution_*.py" | sort | while read -r f; do
    out=$(cd "$DSA/code/python" && timeout 30 python3 "$f" 2>&1)
    if [ $? -eq 0 ]; then
      echo "PASS $f" >> "$report"
    else
      echo "FAIL $f :: $(echo "$out" | tail -2)" >> "$report"
    fi
  done
  echo "Python: $(grep -c '^PASS' "$report") pass, $(grep -c '^FAIL' "$report") fail"
}

verify_java() {
  local report="$META/verify_report_java.txt"
  : > "$report"
  local work=$(mktemp -d)
  find "$DSA/code/java" -name "*.java" | sort | while read -r f; do
    rm -rf "$work/j" && mkdir -p "$work/j"
    err=$(javac -d "$work/j" "$f" 2>&1)
    if [ $? -ne 0 ]; then
      echo "FAIL $f :: COMPILE: $(echo "$err" | head -2)" >> "$report"
      continue
    fi
    # 提取主类名：main 方法所在的最近顶层级类（仅匹配列 0 的 class/public/final/abstract class；
    # 排除 "static class X" 这类列 0 起始的嵌套类声明）
    cls=$(awk '/^class |^public class |^final class |^abstract class / {for(i=1;i<=NF;i++) if($i=="class"){lastTop=$(i+1)}} /static void main/ {print lastTop; exit}' "$f")
    [ -z "$cls" ] && cls=$(awk '/^public class |^class / {for(i=1;i<=NF;i++) if($i=="class"){print $(i+1); exit}}' "$f")
    [ -z "$cls" ] && cls=$(basename "$f" .java)
    out=$(cd "$work/j" && timeout 30 java -cp . "com.webfault.dsa.$cls" 2>&1 | tail -1)
    if echo "$out" | grep -q "PASS"; then
      echo "PASS $f" >> "$report"
    else
      echo "FAIL $f :: RUN[$cls]: $out" >> "$report"
    fi
  done
  rm -rf "$work"
  echo "Java: $(grep -c '^PASS' "$report") pass, $(grep -c '^FAIL' "$report") fail"
}

case "${1:-all}" in
  go) verify_go ;;
  ts) verify_ts ;;
  java) verify_java ;;
  python) verify_python ;;
  all) verify_go; verify_ts; verify_java; verify_python ;;
esac
