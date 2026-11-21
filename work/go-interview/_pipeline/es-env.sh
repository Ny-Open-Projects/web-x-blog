#!/usr/bin/env bash
# es-env.sh -- shared Elasticsearch environment (port 9200)
#
# Usage:
#   source _pipeline/es-env.sh
#   es_up                       # liveness check
#   es "GET /_cat/indices?v"    # curl wrapper against 127.0.0.1:9200
#   es_json "GET /idx/_search"  # same, but pretty-printed
#   es_del t1234_idx            # delete an index
#
# Notes (2026-10-04):
#   * Elasticsearch 7.7.1 was ALREADY INSTALLED on this machine at
#     /Library/elasticsearch-7.7.1 -- the lead did not install it.
#     It is a single-node instance bound to 127.0.0.1:9200.
#   * There is exactly ONE shared instance. Do not start a second one.
#   * Prefix your index names with your card number (e.g. t1108_files)
#     and DELETE them when done -- other workers share this cluster.
#   * ES 7.x specifics worth remembering: mapping types are gone except
#     the deprecated `_doc`; `include_type_name` defaults false;
#     security is OFF by default (no auth needed).
#   * ES 8.x differs a lot (security ON by default, type removed
#     completely). If a card claims "实测" it must say 7.7.1.

ES_HOST=${ES_HOST:-127.0.0.1}
ES_PORT=${ES_PORT:-9200}
ES_BASE="http://${ES_HOST}:${ES_PORT}"
ES_HOME=${ES_HOME:-/Library/elasticsearch-7.7.1}

# Curl against the cluster. Two call forms:
#   es "GET /_cat/indices?v"                 # REST style: METHOD + path in ONE string
#   es "/idx/_search" -H '...' -d '{...}'    # raw style: FIRST arg is the path, rest passed to curl
#
# 2026-10-04 fix (2nd): the raw style used to be `curl "${ES_BASE}$@"`, which glues the
# FIRST arg onto the base URL -- so `es -XPOST "/x" -d ...` produced `...9200-XPOST /x`
# and silently returned an empty body. A call that "returns nothing" is much harder to
# notice than one that errors, so always sanity-check that a query returns a JSON body.
# Now the first arg must be a path starting with `/`; everything else is forwarded.
es() {
    if [ $# -eq 1 ] && [ "${1#* }" != "$1" ]; then
        local method="${1%% *}" path="${1#* }"
        curl -s --max-time 30 -X "$method" "${ES_BASE}${path}"
    elif [ $# -ge 1 ] && [ "${1#/}" != "$1" ]; then
        curl -s --max-time 30 "${ES_BASE}$1" "${@:2}"
    else
        echo "es(): 第一个参数要么是 \"METHOD /path\"（一个字符串），要么是以 / 开头的路径" >&2
        return 2
    fi
}

# Pretty-print the JSON answer (needs python3 on PATH).
es_json() {
    es "$@" \
      | /Users/Wang/.workbuddy/binaries/python/versions/3.13.12/bin/python3 -c \
        'import sys,json
try: print(json.dumps(json.load(sys.stdin), ensure_ascii=False, indent=2))
except Exception: sys.stdout.write(sys.stdin.read())' 2>/dev/null
}

es_up() {
    curl -s --max-time 5 "${ES_BASE}" 2>/dev/null | grep -q '"number"'
}

es_del() {
    local idx="$1"
    [ -z "$idx" ] && { echo "usage: es_del <index>"; return 1; }
    es -XDELETE "/${idx}"
    echo
}

# List only the indices whose name starts with the given prefix.
es_mine() {
    local pfx="$1"
    [ -z "$pfx" ] && pfx="t"
    es "GET /_cat/indices/${pfx}*?v&h=health,status,index,docs.count,store.size"
    echo
}

es_check() {
    echo "--- es-env check (${ES_BASE}) ---"
    es_up && echo "status: UP" || echo "status: DOWN"
    es "GET /" | head -c 400
    echo
    echo "--- indices ---"
    es "GET /_cat/indices?v&h=health,status,index,pri,rep,docs.count,store.size"
    echo
}

case "${1:-}" in
    start)
        echo "ES is a pre-existing system install at ${ES_HOME}."
        echo "Start it yourself with:"
        echo "  ES_PATH_CONF=/tmp/mtdemo-es/conf ${ES_HOME}/bin/elasticsearch -d -p /tmp/mtdemo-es/es.pid"
        ;;
    status) es_up && echo "up" || echo "down" ;;
    check)  es_check ;;
esac
