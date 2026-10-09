# 515 判断对象是否拥有某方法：断言与反射

> 分类：Go 语言基础 / 方法与反射 | 难度：L1~L2 | 题型：机制题 | 频率：中 | 关键词：**类型断言**/**接口字面量**/**MethodByName**/**IsValid**/**方法集**

> 原文锚点：第 1~21 段「方式一类型转换结果判断…方式二 reflect 包 valueof+methodbyname+IsValid…空串返回 false」

## 一句话总述
两法探测「对象有没有某方法」：① **类型断言**——`v.(interface{ Speak() string })`，断言到一个**匿名接口字面量**，`ok` 即结果；② **反射**——`reflect.ValueOf(v).MethodByName(name).IsValid()`。两法结论永远一致，因为都查同一份**方法集**；分水岭在方法接收者：值接收者方法值/指针都可探到，**指针接收者方法只有指针可探到**。

## 面试官视角
- 意图：是否会「能力探测」这个反射入门场景，以及是否真懂方法集规则（值 vs 指针接收者）。
- 分档：P5 会写其中一法；P6 两法都会并说清 IsValid 语义；P7 能讲指针接收者反例与两法一致性根源（同一方法集）。
- 红旗答案：以为断言和反射是「两套独立机制可能结果不同」；不知道空方法名要守卫。
- 惊艳点：报出「同一对象、同一方法，传值 false 传指针 true」的反例，把八股变机制 [经验]。

## 主问答
**Q（面试官原话）：** 怎么判断一个 Go 对象是否拥有某个方法？

**A：** 以 `Person` 结构体的 `Speak() string` 为例 [实测]：

1. **方式一·类型断言**：把对象转到一个只含目标方法的匿名接口——`_, ok := v.(interface{ Speak() string })`；转换成功返回 true。写法轻量、编译期可查接口合法性，适合探测点固定的场景。
2. **方式二·反射**：`reflect.ValueOf(v).MethodByName("Speak").IsValid()`；注意三处细节——先判**空串直接 false**；`MethodByName` 返回 Value；用 `IsValid()` 判存在性。
3. **方法集反例**：`func (p *Person) Rename(string)` 是指针接收者——`Rename(p)`（值）探测 **false**，`Rename(pp)`（指针）**true**；值接收者的 `Speak` 则值/指针都 true [实测]。断言与反射结果完全一致，因为查的是同一份方法集。
4. **选型**：固定接口、热路径用断言（无反射开销）；方法名运行期才确定（配置/插件）只能反射；反射取值会引发逃逸见 `1119-fmt-reflect-escape`。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | 两种方式是什么？ | 写不出断言到接口字面量 |
| L2 | IsValid 判的是什么？ | 不知 MethodByName 缺失返回零 Value |
| L3 | 值和指针探测结果会不同吗？ | 说不出指针接收者反例 |
| L4 | 为什么两法结果一致？ | 讲不出都查方法集 |
| L5 | 反射的性能代价？ | 不知道逃逸与 1119 划界 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|------|------|------|
| 断言语法+reflect API | 无（1.x 稳定） | Go 1.18+ 可用泛型约束替代部分探测场景，但运行期探测仍靠这两法 |

## 关键代码
```go
package main

import (
	"fmt"
	"reflect"
)

type Person struct{ Name string }

func (p Person) Speak() string { return "I am " + p.Name }  // 值接收者
func (p *Person) Rename(s string) { p.Name = s }            // 指针接收者

func hasSpeakByAssert(v interface{}) bool {
	_, ok := v.(interface{ Speak() string }) // 断言到匿名接口
	return ok
}

func hasMethod(v interface{}, name string) bool {
	if name == "" {
		return false // 空串守卫
	}
	return reflect.ValueOf(v).MethodByName(name).IsValid()
}

func main() {
	p := Person{"Alice"}
	pp := &Person{"Alice"}
	fmt.Println(hasSpeakByAssert(p), hasSpeakByAssert(pp)) // true true
	fmt.Println(hasMethod(p, "Rename"), hasMethod(pp, "Rename")) // false true
	fmt.Println(hasMethod(p, "")) // false
}
```

[实测] 输出：`true true` / `false true` / `false`——指针接收者方法在值上探测为 false（断言法同验：`Rename(p)` false、`Rename(pp)` true）。

## 总结与追问预判
核心：**两法是「同一方法集的两种查询入口」；一句话拉满——「指针接收者方法，值探测不到」**。追问接方法集规则与接口机制：鸭子类型见 `613-duck-typing-interface`、隐式实现见 `615-interface-two-impls`、接口相等性的运行期表示见 `509-interface-compare-runtime`；反射性能代价见 `1119-fmt-reflect-escape`。

## ⚠️ 原文纠错
1. 术语核校： [经验] 原文将 false 音转为「footh」、true 音转为「处」、类型断言语法转写为「interface 关键字」，本卡统一为规范术语，不列举原词。
2. 事实核校： [经验] 原文「不传指针判断也返回 true」只对**值接收者**方法成立；对指针接收者方法，值传入探测为 false [实测]——方法集规则才是普适答案。
3. 补充核校： [经验] 原文反射法未提空串守卫的场景差异——MethodByName("") 恒返回零 Value，IsValid=false，但显式守卫更可读。
