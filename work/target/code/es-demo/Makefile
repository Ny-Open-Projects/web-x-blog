# es-demo —— Elasticsearch × Go 工程示例
# 目标 ES：7.x（本地已装 7.7.1，compose 用 7.17.x 单节点）

GO       ?= go
BINARY   := bin/es-demo
ES_URL   ?= http://localhost:9200
REDIS_URL?= redis://localhost:6379
KAFKA    ?= localhost:9092

.PHONY: help build test vet tidy up up-full seed demo doctor down clean

help: ## 帮助
	@echo "Targets:"
	@echo "  make build     编译 es-demo 到 bin/"
	@echo "  make test      运行单元测试（mock ES，无需真实集群）"
	@echo "  make vet       go vet"
	@echo "  make up        启动 ES + Redis（docker compose）"
	@echo "  make up-full   额外启动 Kafka + Kibana"
	@echo "  make seed      连 ES 建索引 + 写样例数据"
	@echo "  make demo      运行全部知识点演示"
	@echo "  make doctor    检查 ES / Redis 连通性"
	@echo "  make down      停止 compose"

build:
	$(GO) build -o $(BINARY) ./cmd/es-demo

test:
	$(GO) test ./... -count=1

vet:
	$(GO) vet ./...

tidy:
	$(GO) tidy

up:
	docker compose up -d elasticsearch redis

up-full:
	docker compose up -d

seed: build
	ES_URL=$(ES_URL) $(BINARY) seed

demo: build
	ES_URL=$(ES_URL) REDIS_URL=$(REDIS_URL) KAFKA_BROKERS=$(KAFKA) $(BINARY) demo

doctor: build
	ES_URL=$(ES_URL) REDIS_URL=$(REDIS_URL) $(BINARY) doctor

down:
	docker compose down
