# 1114 JSON 序列化性能优化全景（换库 → 避 map → 结构）

> 分类：Go 性能 / 序列化 · 全景 | 难度：L3 | 题型：深挖 | 关键词：**序列化性能** / **jsoniter** / **RawMessage** / **protobuf**
> 原文锚点：第 1~64 段「三方向：更快库 / 避 map / 优化标签结构」

## 思路与架构
JSON 序列化优化按**收益递减**分三招，本波为干净首覆盖（全库无 JSON 序列化性能专用卡）：
1. **换更快的库（1114-json-fast-lib）**：标准库反射慢多分配；jsoniter 兼容且反序列化优、easyjson 预编译最快、protobuf 跨服务更优。
2. **避免 map 反序列化（1114-avoid-map-deserialize）**：结构体字段确定无反射；map 需 interface{} 多分配（7 vs 16）；RawMessage 延迟解析。
3. **优化标签与结构（1114-optimize-tags-struct）**：简短标签/简单类型/少嵌套，边际优化、优先级最低。

## 方案取舍
| 手段 | 收益 | 适用 | 代价 |
|---|---|---|---|
| jsoniter | 高 | 通用替换 | 引入依赖 |
| easyjson | 最高 | 热路径 | 重编译维护差 |
| 结构体替代 map | 高 | 反序列化 | 需定结构 |
| RawMessage | 中 | 个别 key | 二次解析 |
| 标签/结构 | 低 | 最后手段 | 可读性略降 |

## 答题技巧
- 答优化按"换库 → 避 map → 结构"收益递减递进，先数量级后边际。
- 口诀：**反射是瓶颈，jsoniter 顶；map 装箱贵，结构体为先；标签是末招，莫本末倒颠**。
- 验证：用 `go test -bench` 看 ns/op 与 allocs/op。

## 细节与核心 API

**① 换更快的库**（标准库反射慢、多分配）：

```go
import jsoniter "github.com/json-iterator/go"
var json = jsoniter.ConfigCompatibleWithStandardLibrary // 直接替换标准库入口，零改业务
// easyjson：go:generate easyjson -all model.go，预编译 marshaler，热路径最快
// protobuf：跨服务用，省文本解析开销
```

**② 避免 map 反序列化**（结构体字段确定、无反射；map 走 `interface{}` 多分配）：

```go
type Req struct {
    UserID int64  `json:"user_id"`
    Name   string `json:"name"`
}
data, _ := json.Marshal(Req{UserID: 1, Name: "x"}) // 比 map[string]any 少分配（约 7 vs 16 次）

// RawMessage 延迟解析个别 key
type Envelope struct {
    Type string          `json:"type"`
    Body json.RawMessage `json:"body"` // 不立即解析，按需再 Unmarshal
}
```

**③ 标签/结构边际优化**：简短标签、简单类型、少嵌套；最后手段。

```go
// 验证：go test -bench=. -benchmem 看 ns/op 与 allocs/op，先数量级后边际
```

> 边界：反射瓶颈见 112；基准测试写法见 113。本卡只讲 JSON 序列化性能三方向。
