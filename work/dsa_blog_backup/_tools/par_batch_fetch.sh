#!/bin/bash
# 并行批量抓取（10 个并发），从 _meta/failed.txt 读取失败的链接
set -e

META_DIR="/Users/Wang/Code/webfault-ai/dsa/_meta"
ART_DIR="${META_DIR}/articles"
FAILED="${META_DIR}/failed.txt"
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"

if [ ! -f "$FAILED" ]; then
    echo "No failed.txt"
    exit 0
fi

mkdir -p "$ART_DIR"

# 限制并发到 6
PARALLEL=6

fetch_one() {
    local line="$1"
    local aid=$(echo "$line" | cut -f1)
    local url=$(echo "$line" | cut -f2)
    local out="${ART_DIR}/${aid}.html"

    # 如果文件存在且有效，跳过
    if [ -f "$out" ]; then
        if grep -q "title-article" "$out" 2>/dev/null && ! grep -q "Security Verification\|安全验证" "$out" 2>/dev/null; then
            return 0
        fi
    fi

    curl -s -L -A "$UA" -H "Accept-Language: zh-CN,zh;q=0.9" \
        -H "Referer: https://blog.csdn.net/tyro_java/category_6186626.html" \
        "$url" -o "$out" --max-time 60 || rm -f "$out"
}

export -f fetch_one
export ART_DIR UA

cat "$F" | xargs -I {} -P "$PARALLEL" bash -c 'fetch_one "$@"' _ {}

echo "Done."
ls "$ART_DIR" | wc -l