// Package mq Kafka 数据同步（对应《服务隔离下解决数据同步——商品变更事件发送kafka消息》
// 与《Golang使用kafka的正确姿势》）。
//
// 场景：商品/订单变更时不直接写 ES，而是发一条事件到 Kafka，由消费者异步消费后写 ES，
// 从而把「业务写入」与「搜索索引写入」解耦（服务隔离 + 削峰）。
package mq

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"net"
	"time"

	"github.com/segmentio/kafka-go"
)

// EnsureTopic 若 topic 不存在则创建（broker 关闭 auto-create 时必须先建 topic）。
// 这让 es-demo mq-demo 在干净环境里也能直接跑通。
func EnsureTopic(brokers []string, topic string, partitions int) error {
	if len(brokers) == 0 {
		return fmt.Errorf("no kafka brokers")
	}
	conn, err := kafka.Dial("tcp", brokers[0])
	if err != nil {
		return err
	}
	defer conn.Close()
	controller, err := conn.Controller()
	if err != nil {
		return err
	}
	ctrl, err := kafka.Dial("tcp", net.JoinHostPort(controller.Host, fmt.Sprint(controller.Port)))
	if err != nil {
		return err
	}
	defer ctrl.Close()
	return ctrl.CreateTopics(kafka.TopicConfig{
		Topic:             topic,
		NumPartitions:     partitions,
		ReplicationFactor: 1,
	})
}

// Event 业务变更事件（发送到 Kafka，再由消费者写 ES）。
type Event struct {
	Op    string `json:"op"`    // insert/update/delete
	Index string `json:"index"` // 目标 ES 索引
	ID    string `json:"id"`
	Doc   []byte `json:"doc"`   // 文档 JSON（delete 时为空）
}

// Producer 事件生产者。
type Producer struct {
	w *kafka.Writer
}

// NewProducer 创建 Kafka 生产者。
func NewProducer(brokers []string, topic string) *Producer {
	return &Producer{w: &kafka.Writer{
		Addr:         kafka.TCP(brokers...),
		Topic:        topic,
		Balancer:     &kafka.LeastBytes{},
		BatchTimeout: 100 * time.Millisecond,
	}}
}

// Publish 发送一条变更事件。
func (p *Producer) Publish(ctx context.Context, e Event) error {
	b, err := json.Marshal(e)
	if err != nil {
		return err
	}
	return p.w.WriteMessages(ctx, kafka.Message{
		Key:   []byte(e.ID),
		Value: b,
	})
}

// Close 关闭生产者。
func (p *Producer) Close() error { return p.w.Close() }

// Consumer 事件消费者：消费后回调 handler 写 ES（解耦点）。
type Consumer struct {
	r *kafka.Reader
}

// NewConsumer 创建 Kafka 消费者（消费者组模式）。
func NewConsumer(brokers []string, topic, group string) *Consumer {
	return &Consumer{r: kafka.NewReader(kafka.ReaderConfig{
		Brokers:        brokers,
		Topic:          topic,
		GroupID:        group,
		CommitInterval: time.Second,
		StartOffset:    kafka.FirstOffset,
	})}
}

// Run 持续消费，把每条事件交给 handler 处理（handler 内写 ES）。
func (c *Consumer) Run(ctx context.Context, handle func(ctx context.Context, e Event) error) error {
	for {
		m, err := c.r.FetchMessage(ctx)
		if err != nil {
			if ctx.Err() != nil {
				return nil // 被取消，正常退出
			}
			return err
		}
		var e Event
		if err := json.Unmarshal(m.Value, &e); err != nil {
			log.Printf("[mq] bad message: %v", err)
			_ = c.r.CommitMessages(ctx, m)
			continue
		}
		if err := handle(ctx, e); err != nil {
			log.Printf("[mq] handle event %s failed: %v", e.ID, err)
			continue // 不 commit，等待重试（生产应进死信队列）
		}
		if err := c.r.CommitMessages(ctx, m); err != nil {
			return fmt.Errorf("commit: %w", err)
		}
	}
}

// Close 关闭消费者。
func (c *Consumer) Close() error { return c.r.Close() }
