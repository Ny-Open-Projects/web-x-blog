#!/usr/bin/env bash
# redis-env.sh -- shared Redis test environment (port 16399)
#
# Usage:
#   source _pipeline/redis-env.sh
#   rcli ping
#   rcli set k v
#   rsql "INFO memory"        # same as rcli but reads nicer for multi-word
#   redis_up || redis_start
#
# Hard safety rules (set by lead, DO NOT relax):
#   1) bind 127.0.0.1 ONLY.
#      NEVER use "bind * -::*". Redis' protected-mode only protects you when
#      the bind directive is ABSENT -- once you bind "*", protected-mode is
#      effectively off and anyone on the LAN can connect without a password.
#   2) maxmemory 2gb. Prevents a runaway test from eating the whole machine.
#      If you need to test eviction policies, change it temporarily and
#      RESTORE it to 2gb when done (see redis_restore below).
#   3) No persistence: --save '' --appendonly no. Keeps /tmp and disk usage ~0.
#   4) FLUSHDB between unrelated tests so results do not contaminate each other.
#
# 2026-10-04: gpL brought up Redis 7.2.3 on 16399 with --daemonize yes,
# which defaulted to bind "* -::*" (LAN-exposed, no password).
# Lead fixed it live via CONFIG SET bind (no restart, data preserved) and
# wrote this script so the next worker does not repeat the mistake.

REDIS_BASE=${REDIS_BASE:-/usr/local/redis/src}
REDIS_PORT=${REDIS_PORT:-16399}
# 多 worker 隔离：每个 worker 认领一个 DB（Redis 默认 db0~db15）。
# 不要用 db0（默认库，最容易撞）。分派：gpM=1  gpK=2  gpL=3
REDIS_DB=${REDIS_DB:-0}
REDIS_BIN="$REDIS_BASE/redis-server"
REDIS_CLI="$REDIS_BASE/redis-cli"

# -n <db> 让每次调用都落在自己的库上，不会污染别人
redis_cli() { "$REDIS_CLI" -p "$REDIS_PORT" -n "$REDIS_DB" "$@"; }

# Short alias for everyday use
rcli() { redis_cli "$@"; }

# 只清自己那个库（FLUSHALL 会连别人的库一起清掉，禁止使用）
rflush() { redis_cli flushdb; }

is_up() {
    redis_cli ping 2>/dev/null | grep -q PONG
}

redis_up() { is_up; }

do_start() {
    if is_up; then
        echo "redis already up on $REDIS_PORT"
        return 0
    fi
    "$REDIS_BIN" \
        --port "$REDIS_PORT" \
        --daemonize yes \
        --bind 127.0.0.1 \
        --maxmemory 2gb \
        --maxmemory-policy noeviction \
        --save '' \
        --appendonly no \
        --dir /tmp \
        2>/dev/null
    sleep 1
    if is_up; then
        echo "redis started on $REDIS_PORT (bind 127.0.0.1, maxmemory 2gb, no persistence)"
    else
        echo "redis FAILED to start on $REDIS_PORT" >&2
        return 1
    fi
}

do_stop() {
    is_up || { echo "redis not running"; return 0; }
    redis_cli shutdown nosave 2>/dev/null
    sleep 1
    is_up && { echo "redis still up (?)" >&2; return 1; }
    echo "redis stopped"
}

# Restore the safe defaults after an eviction-policy experiment
redis_restore() {
    redis_cli config set maxmemory 2gb >/dev/null
    redis_cli config set maxmemory-policy noeviction >/dev/null
    echo "restored: maxmemory=2gb policy=noeviction"
}

# Print the safety-critical config in one shot (use this in card evidence)
redis_check() {
    echo "--- redis-env safety check (port $REDIS_PORT) ---"
    redis_cli config get bind
    redis_cli config get maxmemory
    redis_cli config get maxmemory-policy
    redis_cli config get save
    redis_cli config get appendonly
    redis_cli info memory | grep -E "used_memory_human|maxmemory_human|maxmemory_policy"
}

# Run a command, starting the server first if needed
rdo() {
    is_up || do_start
    redis_cli "$@"
}

# Subcommand dispatch -- ONLY when executed directly.
# Guard matters: if we dispatched on "$1" while being *sourced*, the caller's
# positional args would accidentally trigger start/stop. (Same class of bug
# as mysql-env.sh: keep the two env scripts consistent -- pure ASCII, no
# full-width parens inside ${...}, and an execution guard.)
if [ "${BASH_SOURCE[0]:-$0}" = "$0" ]; then
    case "${1:-}" in
        start)   do_start ;;
        stop)    do_stop ;;
        status)  is_up && echo "up on $REDIS_PORT" || echo "down" ;;
        check)   redis_check ;;
        restore) redis_restore ;;
    esac
fi
