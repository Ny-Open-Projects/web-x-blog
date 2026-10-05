// Package model 定义示例业务文档与它们的 ES mapping。
//
// 对应知识点：
//   - KP-MAP-02 字段类型选型（text/keyword/numeric/date/nested/object）
//   - KP-MAP-04 _source / enabled / doc_values / index:false
//   - KP-DM-01 面向搜索性能的建模（宽表 + 反范式，避免 join）
//   - KP-MAP-05/KP-MAP-06 nested 与 join 两种保留数组元素关系的方式
package model

// Product 商品文档（商城搜索服务）。
// 设计：把搜索要用的字段尽量拍平到一张宽表，避免 join。
type Product struct {
	ID          string    `json:"id"`          // 商品ID，keyword
	Title       string    `json:"title"`       // 标题，text + 子 keyword
	CategoryID  int64     `json:"category_id"` // 类目，integer
	Price       int64     `json:"price"`       // 价格（单位：分），scaled_float 或 long
	Tags        []string  `json:"tags"`        // 标签数组，keyword
	OnSale      bool      `json:"on_sale"`     // 是否在售
	Sales       int64     `json:"sales"`       // 销量，用于排序
	CreatedAt   int64     `json:"created_at"`  // 时间戳，date(epoch_millis)
	// NestedDemo 演示 nested：一组「规格」，需要保留 (name,value) 的配对关系。
	Specs []Spec `json:"specs"`
}

// Spec 商品规格（name/value 必须成对，用 nested 保留关系）。
type Spec struct {
	Name  string `json:"name"`
	Value string `json:"value"`
}

// ProductMapping 商品索引 mapping。演示：text+keyword 双字段、numeric 选型、
// nested 保留数组关系、doc_values / index:false 等开关。
const ProductMapping = `{
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 0,
    "index": { "refresh_interval": "1s" }
  },
  "mappings": {
    "properties": {
      "id":         { "type": "keyword" },
      "title":      { "type": "text", "analyzer": "ik_max_word",
                      "fields": { "keyword": { "type": "keyword" } } },
      "category_id":{ "type": "integer" },
      "price":      { "type": "scaled_float", "scaling_factor": 100 },
      "tags":       { "type": "keyword" },
      "on_sale":    { "type": "boolean" },
      "sales":      { "type": "integer", "doc_values": true },
      "created_at": { "type": "date", "format": "epoch_millis" },
      "specs": {
        "type": "nested",
        "properties": {
          "name":  { "type": "keyword" },
          "value": { "type": "keyword" }
        }
      }
    }
  }
}`

// Order 订单文档（订单搜索场景）。
type Order struct {
	ID         string     `json:"id"`
	UserID     string     `json:"user_id"`
	Status     int        `json:"status"`
	PayAmount  int64      `json:"pay_amount"` // 单位：分
	CreatedAt  int64      `json:"created_at"`
	Items      []OrderItem `json:"items"`     // 用 nested 保留「商品+数量」配对
}

// OrderItem 订单项（nested）。
type OrderItem struct {
	SKU  string `json:"sku"`
	Name string `json:"name"`
	Num  int    `json:"num"`
}

// OrderMapping 订单索引 mapping，演示 nested（订单项）与 join 两种方案并存。
const OrderMapping = `{
  "settings": { "number_of_shards": 1, "number_of_replicas": 0 },
  "mappings": {
    "properties": {
      "id":         { "type": "keyword" },
      "user_id":    { "type": "keyword" },
      "status":     { "type": "integer" },
      "pay_amount": { "type": "scaled_float", "scaling_factor": 100 },
      "created_at": { "type": "date", "format": "epoch_millis" },
      "items": {
        "type": "nested",
        "properties": {
          "sku":  { "type": "keyword" },
          "name": { "type": "text" },
          "num":  { "type": "integer" }
        }
      },
      "join_field": {
        "type": "join",
        "relations": { "order": "item" }
      }
    }
  }
}`

// LogDoc 日志文档（时序/日志搜索场景，配合 ILM）。
type LogDoc struct {
	Timestamp int64  `json:"@timestamp"`
	Level     string `json:"level"`
	Service   string `json:"service"`
	Message   string `json:"message"`
	TraceID   string `json:"trace_id"`
}

// LogMapping 日志索引 mapping（用于 rollover 别名写入）。
const LogMapping = `{
  "settings": { "number_of_shards": 1, "number_of_replicas": 0 },
  "mappings": {
    "properties": {
      "@timestamp": { "type": "date" },
      "level":  { "type": "keyword" },
      "service":{ "type": "keyword" },
      "message":{ "type": "text" },
      "trace_id":{ "type": "keyword" }
    }
  }
}`

// EmailDoc 邮件文档（PB 级邮件搜索：倒排索引 + doc_values 分离、冷热分离）。
type EmailDoc struct {
	ID      string `json:"id"`
	From    string `json:"from"`
	To      string `json:"to"`
	Subject string `json:"subject"`
	Body    string `json:"body"`   // 大文本：text 用于全文检索
	HasAtt  bool   `json:"has_att"` // 是否有附件：keyword
	Date    int64  `json:"date"`
}

// EmailMapping 邮件索引 mapping：大文本 body 仅建倒排（index:true，
// doc_values:false 省空间），subject 同时给 text+keyword。
const EmailMapping = `{
  "settings": { "number_of_shards": 1, "number_of_replicas": 0 },
  "mappings": {
    "properties": {
      "id":      { "type": "keyword" },
      "from":    { "type": "keyword" },
      "to":      { "type": "keyword" },
      "subject": { "type": "text", "fields": { "kw": { "type": "keyword" } } },
      "body":    { "type": "text", "doc_values": false },
      "has_att": { "type": "boolean" },
      "date":    { "type": "date", "format": "epoch_millis" }
    }
  }
}`
