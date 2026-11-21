#!/bin/bash
# Chapter 12 (MySQL) test environment manager -- ASCII only.
#
# Uses TCP (127.0.0.1:13307) as the primary connection: the unix socket at
# /tmp/mtdemo-mysql/my.sock can disappear (observed 2026-10-04 18:33) while the
# server keeps serving TCP, which used to make this script wrongly think the
# instance was down and then fail with "Address already in use".
#
# Usage:
#   bash _pipeline/mysql-env.sh check
#   bash _pipeline/mysql-env.sh start
#   bash _pipeline/mysql-env.sh stop
#   bash _pipeline/mysql-env.sh reset
#   bash _pipeline/mysql-env.sh vars
#   bash _pipeline/mysql-env.sh sql "SELECT 1"
#   bash _pipeline/mysql-env.sh file x.sql
#
# MySQL 8.0.33, port 13307, user root (no pass), db mtdemo
set -uo pipefail

BASE=/usr/local/mysql
DIR=/tmp/mtdemo-mysql
DATA=$DIR/data
SOCK=$DIR/my.sock
PORT=13307
PIDFILE=$DIR/my.pid
ERRLOG=$DIR/err.log
DB=mtdemo
HOST=127.0.0.1

mysql_cli()      { "$BASE/bin/mysql"      -h"$HOST" -P"$PORT" -uroot "$@"; }
mysqladmin_cli() { "$BASE/bin/mysqladmin" -h"$HOST" -P"$PORT" -uroot "$@"; }

# Alive = TCP answers. Fall back to socket probe only if TCP fails.
is_up() {
  mysqladmin_cli ping >/dev/null 2>&1 && return 0
  [ -S "$SOCK" ] && "$BASE/bin/mysqladmin" --socket="$SOCK" -uroot ping >/dev/null 2>&1
}

do_start() {
  if is_up; then echo "already running (port=$PORT)"; return 0; fi
  mkdir -p "$DIR"
  if [ ! -d "$DATA/mysql" ]; then
    echo "first start: initializing datadir ..."
    "$BASE/bin/mysqld" --initialize-insecure --datadir="$DATA" \
      --basedir="$BASE" --log-error="$DIR/init.log" || { echo "init failed: $DIR/init.log"; return 1; }
  fi
  "$BASE/bin/mysqld" --datadir="$DATA" --basedir="$BASE" \
    --socket="$SOCK" --port="$PORT" --pid-file="$PIDFILE" \
    --log-error="$ERRLOG" --mysqlx=0 --daemonize || { echo "start failed: $ERRLOG"; return 1; }
  for _ in $(seq 1 30); do sleep 1; is_up && break; done
  if is_up; then
    mysql_cli -e "CREATE DATABASE IF NOT EXISTS $DB CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
    echo "started (port=$PORT db=$DB)"
  else
    echo "cannot connect after start: $ERRLOG"; return 1
  fi
}

do_stop() {
  if is_up; then mysqladmin_cli shutdown && echo "stopped"; else echo "not running"; fi
}

do_check() {
  if is_up; then
    echo "OK: connected (port=$PORT)"
    mysql_cli -e "SELECT VERSION() AS version, @@transaction_isolation AS iso;"
    mysql_cli -e "SHOW DATABASES LIKE '$DB';"
    [ -S "$SOCK" ] && echo "socket: present" || echo "socket: MISSING (TCP still fine)"
  else
    echo "FAIL: cannot connect (port=$PORT) -- run: bash $0 start"; return 1
  fi
}

do_reset() {
  is_up || { echo "not running, run start first"; return 1; }
  mysql_cli -e "DROP DATABASE IF EXISTS $DB; CREATE DATABASE $DB CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
  echo "reset done: $DB"
}

do_vars() {
  is_up || { echo "not running, run start first"; return 1; }
  mysql_cli -e "SELECT @@version AS version, @@innodb_version AS innodb, @@log_bin AS log_bin, @@binlog_format AS binlog_format, @@sync_binlog AS sync_binlog, @@innodb_flush_log_at_trx_commit AS flush_at_commit, @@transaction_isolation AS default_iso;"
  mysql_cli -e "SELECT @@innodb_buffer_pool_size/1024/1024 AS bp_MB, @@innodb_page_size AS page_size, @@innodb_log_file_size/1024/1024 AS logfile_MB, @@performance_schema AS perf_schema;"
}

case "${1:-check}" in
  start) do_start ;;
  stop)  do_stop ;;
  reset) do_reset ;;
  vars)  do_vars ;;
  sql)   is_up || do_start; shift; mysql_cli -D "$DB" -e "$*" ;;
  file)  is_up || do_start; shift; mysql_cli -D "$DB" < "$1" ;;
  check|"") do_check ;;
  *) echo "unknown cmd: $1"; sed -n '12,22p' "$0"; exit 1 ;;
esac
