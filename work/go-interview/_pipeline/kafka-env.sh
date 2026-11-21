#!/usr/bin/env bash
# kafka-env.sh -- shared Kafka environment (KRaft single node, port 9092)
#
# Usage:
#   source _pipeline/kafka-env.sh
#   kafka_up                                  # liveness check
#   ktopics list                              # kafka-topics.sh ...
#   kproduce t910_orders <<< $'a\nb\nc'       # produce lines from stdin
#   kconsume t910_orders 3                    # read first 3 messages from beginning
#   kdesc t910_orders                         # describe topic (partitions / ISR)
#   kdel t910_orders                          # delete topic
#   kgroups                                   # consumer group list
#
# Environment facts (2026-10-04, all verified by the lead):
#   * Kafka 3.7.0, KRaft mode (NO ZooKeeper), single combined node id=1
#   * Install dir : /tmp/mtdemo-kafka/kafka_2.13-3.7.0
#   * Broker      : 127.0.0.1:9092
#   * Controller  : 127.0.0.1:19093   <-- NOT 9093! see below
#   * Java        : JDK 17 (Kafka 3.7 is tested against 8/11/17)
#   * Data dir    : /tmp/mtdemo-kafka/data
#
#   ⚠️ The controller port is 19093, not the default 9093, because
#      **Docker Desktop already listens on 127.0.0.1:9093** on this machine.
#      Symptom when they collide: the broker starts but never registers --
#      `RegistrationResponseHandler: channel manager timed out before sending
#      the request`, then `Unable to register the broker because the RPC got
#      timed out`. The process is alive but 9092 never opens.
#      => Before changing any port, run `lsof -nP -iTCP:<port>` first.
#
#   ⚠️ macOS has NO `timeout` command and NO `gtimeout` here.
#      Use:  perl -e 'alarm 20; exec @ARGV' <cmd>     (verified working)

KAFKA_HOME=${KAFKA_HOME:-/tmp/mtdemo-kafka/kafka_2.13-3.7.0}
KAFKA_BOOTSTRAP=${KAFKA_BOOTSTRAP:-127.0.0.1:9092}
export JAVA_HOME=${JAVA_HOME:-/Library/Java/JavaVirtualMachines/jdk-17.jdk/Contents/Home}
export PATH="$JAVA_HOME/bin:$KAFKA_HOME/bin:$PATH"

kafka_cli() { "$KAFKA_HOME/bin/$1" "${@:2}"; }

# Generic topic CLI: ktopics list | ktopics create ... | ...
ktopics() { "$KAFKA_HOME/bin/kafka-topics.sh" --bootstrap-server "$KAFKA_BOOTSTRAP" "$@"; }

kgroups() { "$KAFKA_HOME/bin/kafka-consumer-groups.sh" --bootstrap-server "$KAFKA_BOOTSTRAP" "$@"; }

kdesc() {
    local t="$1"; [ -z "$t" ] && { echo "usage: kdesc <topic>"; return 1; }
    ktopics --describe --topic "$t"
}

kdel() {
    local t="$1"; [ -z "$t" ] && { echo "usage: kdel <topic>"; return 1; }
    ktopics --delete --topic "$t"
}

# Create a topic with sane defaults for card experiments.
kcreate() {
    local t="$1" p="${2:-1}"
    [ -z "$t" ] && { echo "usage: kcreate <topic> [partitions]"; return 1; }
    ktopics --create --topic "$t" --partitions "$p" --replication-factor 1
}

# Produce lines read from stdin:  printf 'a\nb\n' | kproduce t1
kproduce() {
    local t="$1"; [ -z "$t" ] && { echo "usage: ... | kproduce <topic>"; return 1; }
    "$KAFKA_HOME/bin/kafka-console-producer.sh" --bootstrap-server "$KAFKA_BOOTSTRAP" --topic "$t"
}

# Consume N messages from the beginning (default 3).
# NOTE: we sleep briefly first, because right after topic creation the leader
# election may not be done yet and the consumer can hit a TimeoutException.
kconsume() {
    local t="$1" n="${2:-3}"
    [ -z "$t" ] && { echo "usage: kconsume <topic> [count]"; return 1; }
    sleep 3
    perl -e 'alarm 30; exec @ARGV' \
      "$KAFKA_HOME/bin/kafka-console-consumer.sh" \
      --bootstrap-server "$KAFKA_BOOTSTRAP" --topic "$t" \
      --from-beginning --max-messages "$n" --timeout-ms 12000
}

kafka_up() {
    lsof -nP -iTCP:9092 >/dev/null 2>&1 &&
      "$JAVA_HOME/bin/jps" -l 2>/dev/null | grep -q kafka.Kafka
}

kafka_start() {
    kafka_up && { echo "kafka already up"; return 0; }
    "$KAFKA_HOME/bin/kafka-server-start.sh" -daemon "$KAFKA_HOME/config/kraft/server.properties"
    for _ in $(seq 1 30); do sleep 2; kafka_up && { echo "kafka started on $KAFKA_BOOTSTRAP"; return 0; }; done
    echo "kafka FAILED to start -- check $KAFKA_HOME/logs/server.log" >&2
    return 1
}

kafka_stop() {
    "$KAFKA_HOME/bin/kafka-server-stop.sh" >/dev/null 2>&1
    sleep 3; pkill -f kafka.Kafka 2>/dev/null; sleep 1
    kafka_up && { echo "still up (?)" >&2; return 1; } || echo "kafka stopped"
}

kafka_check() {
    echo "--- kafka-env check ---"
    echo "KAFKA_HOME = $KAFKA_HOME"
    echo "JAVA_HOME  = $JAVA_HOME"
    kafka_up && echo "status: UP ($KAFKA_BOOTSTRAP)" || echo "status: DOWN"
    echo "--- listeners ---"
    lsof -nP -iTCP:9092 -iTCP:19093 2>/dev/null | grep LISTEN
    echo "--- topics ---"
    ktopics --list 2>/dev/null | head -20
}

case "${1:-}" in
    start)  kafka_start ;;
    stop)   kafka_stop ;;
    status) kafka_up && echo up || echo down ;;
    check)  kafka_check ;;
esac
