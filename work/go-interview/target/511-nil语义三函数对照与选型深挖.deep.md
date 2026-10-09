# 511 nil 语义三函数对照与选型深挖

> 覆盖源 5-11 的机制延伸：DeepEqual 的 IsNil 短路在源码里的位置与推论、bytes.Equal/slices.Equal 的 len+memequal 语义、三函数的性能量级与适用边界、nil 切片的工程规范。主卡已给分歧主线，本附录做机制与选型深挖。

## 思路与架构

```text
两个 []byte 相等性判定的三条通路
├─ b1 == b2
│   └─ 编译错误 (slice 不可 ==, 仅可与 nil 比)
├─ reflect.DeepEqual(b1, b2)
│   ├─ 递归入口 deepValueEqual
│   ├─ 硬规则: v1.IsNil() != v2.IsNil() -> 直接 false
│   ├─ 推论: "相等" = nil性相同 && 深度内容相等
│   └─ [实测] nil vs 空=false; 双nil=true
├─ bytes.Equal / slices.Equal
│   ├─ len 相等 && 内容逐字节同
│   ├─ nil 与空 len 均 0 -> 无区别 -> true
│   └─ 底层 memequal 可向量化, O(n) 纯内容
└─ 选型
    ├─ 比内容 (业务等价) -> bytes/slices.Equal
    └─ 比结构含 nil 性 (测试断言/深拷贝对照) -> DeepEqual
```

## 方案取舍
- **IsNil 短路是「设计选择」不是「实现瑕疵」**：DeepEqual 的目标读者是**测试与反射场景**——那里「nil 切片」与「空切片」常代表不同的程序状态（未初始化 vs 已初始化为空），把它们判为不等能暴露更多 bug。而 bytes.Equal 的读者是**协议/内容处理**——线上只关心字节内容。同一个 nil，在两个语义域里价值不同，**分歧是两套需求的正确投影** [经验]。
- **性能量级差一个世界**：bytes.Equal 底层走 `memequal`（可 SIMD 向量化），O(n) 纯内存比较；DeepEqual 走反射——每层取 Value、判断 Kind、分配 visit map（防循环），常数比前者高 1~2 个数量级。[实测] 结论方向明确：**热路径比字节用 bytes/slices.Equal，DeepEqual 只进测试代码**；把 DeepEqual 放进请求处理路径是常见的性能事故 [经验]。
- **slices.Equal 是泛型收口**：bytes.Equal 只收 `[]byte`，泛型前比 `[]int`/自定义元素切片要手写循环或退回 DeepEqual；1.21+ 的 `slices.Equal[T comparable]` 用泛型覆盖所有可比较元素类型，语义与 bytes.Equal 一致（nil 与空等价）。**新代码的默认选择**；`slices.EqualFunc` 再补自定义判等 [经验]。
- **nil 切片工程规范**：API 出参尽量统一——要么都返回 nil 表示「无」，要么都返回空切片，别让调用方猜；比较语义敏感的接口在文档里写明「nil 与空视为等价」或「区分 nil」。断言 nil 性用 `b == nil`（切片可合法与 nil 比），不要用 `len(b)==0` 判 nil（空切片也满足）[经验]。

## 答题技巧
- 先给分歧结论再给机制：「DeepEqual false 是因为 IsNil 不对称短路，bytes.Equal true 是因为只比内容」——一句话说清两套语义 [实测]。
- 报全景对账而非单点：「nil vs 空 false/true、双 nil true/true、非空同内容 true/true——分歧只在 nil 性不对称」——四组数字一次给全 [实测]。
- 被问「性能」→ 报「反射 vs memexact 向量化差 1~2 个数量级，DeepEqual 别进热路径」[经验]。
- 被问「泛型切片」→ slices.Equal 收口，顺带报 1.21 版本边界 [经验]。
- 主动边界到 `514-deepequal-vs-equal`（== 与 DeepEqual 三大差异）、`514-deepequal-mechanism`（DeepEqual 机制）、`514-deepequal-pitfalls`（误用清单）、`504-nil-comparability.deep`（nil 可比较性）、`1113-byteslice-to-string`（字节切片转换族），构成「相等性判断」专题 [边界]。
