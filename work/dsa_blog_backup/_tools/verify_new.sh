#!/bin/bash
# verify_new.sh — 验证 7 种新语言（rust/lua/c/cpp/r/zig/dart）
# 用法: ./verify_new.sh <lang> [topic]
set -u
DSA="/Users/Wang/Code/webfault-ai/dsa"
META="$DSA/_meta"
DART="$HOME/langs/dart-sdk/bin/dart"
ZIG="$HOME/langs/zig/zig"
RHOME="$HOME/langs/R.framework/Versions/4.3-x86_64/Resources"
timeout() { perl -e 'alarm shift; exec @ARGV' "$@"; }

lang="${1:?lang required: rust|lua|c|cpp|r|zig|dart}"
topic="${2:-}"
report="$META/verify_report_${lang}.txt"
: > "$report"

if [ -n "$topic" ]; then
  files=$(find "$DSA/$lang/$topic" -type f 2>/dev/null | sort)
else
  files=$(find "$DSA/$lang" -type f 2>/dev/null | sort)
fi

tmp=$(mktemp -d)
for f in $files; do
  out=""
  case "$lang" in
    rust)
      bin="$tmp/$(basename "$f" .rs)_bin"
      if timeout 60 rustc -O "$f" -o "$bin" 2>"$tmp/err"; then
        out=$(timeout 30 "$bin" 2>&1 | tail -1)
      else
        out="COMPILE: $(head -2 "$tmp/err" | tr '\n' ' ')"
      fi ;;
    lua)   out=$(timeout 30 lua "$f" 2>&1 | tail -1) ;;
    c)
      bin="$tmp/$(basename "$f" .c)_bin"
      if timeout 60 clang -O2 "$f" -o "$bin" 2>"$tmp/err"; then
        out=$(timeout 30 "$bin" 2>&1 | tail -1)
      else
        out="COMPILE: $(head -2 "$tmp/err" | tr '\n' ' ')"
      fi ;;
    cpp)
      bin="$tmp/$(basename "$f" .cpp)_bin"
      if timeout 90 clang++ -std=c++17 -O2 "$f" -o "$bin" 2>"$tmp/err"; then
        out=$(timeout 30 "$bin" 2>&1 | tail -1)
      else
        out="COMPILE: $(head -2 "$tmp/err" | tr '\n' ' ')"
      fi ;;
    r)     out=$(timeout 60 "$RHOME/Rscript" "$f" 2>&1 | tail -1) ;;
    zig)   out=$(timeout 120 "$ZIG" run "$f" 2>&1 | tail -1) ;;
    dart)  out=$(timeout 60 "$DART" run "$f" 2>&1 | tail -1) ;;
  esac
  if echo "$out" | grep -q "PASS"; then
    echo "PASS $f" >> "$report"
  else
    echo "FAIL $f :: $out" >> "$report"
  fi
done
rm -rf "$tmp"
echo "$lang: $(grep -c '^PASS' "$report") pass, $(grep -c '^FAIL' "$report") fail"
