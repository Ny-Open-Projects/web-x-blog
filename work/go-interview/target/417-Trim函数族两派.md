# 417 Trim 函数族两派：贪婪 vs 精确

> 分类：Go 语言基础 / 字符串处理 | 难度：L1~L2 | 题型：对比题 | 频率：中 | 关键词：**TrimRight**/**TrimSuffix**/**cutset 字符集**/**贪婪模式**/**TrimFunc**

> 原文锚点：第 1~22 段「TrimPrefix/TrimSuffix 只删一个…TrimLeft/TrimRight 删到不满足为止…Trim=TrimLeft+TrimRight…TrimFunc 回调」

## 一句话总述
strings 包的 trim 族分两派：**贪婪派**（`Trim`/`TrimLeft`/`TrimRight`）——第二参是**字符集**（cutset），从两端不停删、直到遇到不在集合里的字符；**精确派**（`TrimPrefix`/`TrimSuffix`）——第二参是**完整子串**，只删一次前/后缀。`Trim` = 两端各来一次贪婪。最易混点：`"go"` 在贪婪派里是 `{'g','o'}` 两个字符的集合，在精确派里是 `"go"` 一个子串。

## 面试官视角
- 意图：字符串处理是高频日常题，考察是否真读过函数签名——特别是 cutset 参数类型（string 当字符集用）。
- 分档：P5 知各函数删什么；P6 说清 cutset 字符集 vs 完整子串的本质差异；P7 能接 TrimFunc 回调语义与底层切片共享问题。
- 红旗答案：以为 `TrimRight(s, "go")` 是删掉子串 "go" 的所有重复——实际是删掉尾端所有 'g' 或 'o' 字符。
- 惊艳点：指出 trim 族返回的是**切片**，与原串共享底层数组——长串 TrimLeft 后持有小片段会阻碍整块回收，见 905 [经验]。

## 主问答
**Q（面试官原话）：** strings.TrimRight 和 strings.TrimSuffix 有什么区别？

**A：** 以 `s := "gogointerviewgogo"` 为例 [实测]：

1. **TrimSuffix**（精确派）：删**一次**尾部的子串 `"go"` → `gogointerviewgo`。同理 TrimPrefix 删一次头部子串 → `gointerviewgogo`。
2. **TrimRight**（贪婪派）：第二参 "go" 是字符集，从尾部连续删所有 'g'/'o' → `gogointerview`。TrimLeft 同理 → `interviewgogo`。
3. **Trim** = TrimLeft + TrimRight 两端贪婪 → `interview`。
4. **TrimFunc**：按 rune 回调定制，**回调返回 true 即剪除**该字符——`TrimFunc("《面试专题》2024", func(r rune) bool { return r < 128 })` 剪掉所有 ASCII 段字符，保留中文 → `《面试专题》` [实测]。
5. 一句口诀：**除 TrimPrefix/TrimSuffix 外全是贪婪模式，删到不满足为止；这俩只动一次**。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | 两个函数各删多少？ | 分不清一次vs贪婪 |
| L2 | 参数 "go" 是什么含义？ | 说不出字符集vs子串 |
| L3 | Trim 内部怎么实现？ | 不知道=Left+Right 组合 |
| L4 | 想按字符自定义规则？ | 写不出 TrimFunc 回调 |
| L5 | trim 后的串内存在哪？ | 不知道切片共享底层 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|------|------|------|
| 函数语义 Go 1 起稳定 | 无 | 1.0 至今行为不变；TrimFunc 自 1.1 提供，放心用 |

## 关键代码
```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	s := "gogointerviewgogo"
	fmt.Println("TrimPrefix :", strings.TrimPrefix(s, "go"))
	fmt.Println("TrimSuffix :", strings.TrimSuffix(s, "go"))
	fmt.Println("TrimLeft   :", strings.TrimLeft(s, "go"))
	fmt.Println("TrimRight  :", strings.TrimRight(s, "go"))
	fmt.Println("Trim       :", strings.Trim(s, "go"))
	fmt.Println("TrimFunc   :", strings.TrimFunc("《面试专题》2024",
		func(r rune) bool { return r < 128 })) // 回调 true=剪除
}
```

[实测] 输出：`gointerviewgogo` / `gogointerviewgo` / `interviewgogo` / `gogointerview` / `interview` / `《面试专题》`。

## 总结与追问预判
核心：**面试只考一句话——cutset 字符集 vs 完整子串；贪婪 vs 一次**。追问常往内存走：trim 族返回切片与原串共享底层数组，长串截短后可能拖住整块内存，答法见 905 与修复方案 `905-string-slice-fixes`；字符串赋值共享机制见 905。

## ⚠️ 原文纠错
1. 事实核校： [经验] 原文「ASCII 码值小于 128 的字符只可能是中文字符，所以输出面试专题」是硬伤——ASCII < 128 恰是英文与控制字符，中文字符的 Unicode 码值远大于 127。实际回调语义是「返回 true 即剪除」：条件 r<128 剪掉的是英文段，中文被**保留**，故输出中文。
2. 措辞核校： [经验] 原文说精确派「只要找到一个满足条件就终止」不精确——TrimPrefix/TrimSuffix 只尝试一次、只删一次，且参数是完整子串而非字符集。
3. 术语核校： [经验] 原文将 TrimSuffix/TrimPrefix 音转为多个崩坏串、将 ASCII 与 rune 音转，本卡统一为规范术语，不列举原词。
