---
title: [WCN-949] 编译错误恢复后 source map 还准吗：错误节点映射到最近的合法模板片段
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-949：编译错误恢复后 source map 还准吗：错误节点映射到最近的合法模板片段

**答**：
- 结论先行：编译器做错误恢复（跳过非法 token 继续编译）时，生成代码与源码的对应关系会「错位」——恢复跳过的那段没有生成产物，后续映射若仍按原行号累加就会偏移。
- 处理：错误恢复时把跳过的源码区间显式标记为「无映射段」（mappings 里该处无 segment），后续段按真实生成的行列继续，保证「合法部分」的映射仍准确。
- 最近合法片段策略：错误节点本身无法映射时，映射到最近的合法模板 span，并在错误信息里标注「此处之后跳过 N 字符」，帮助定位。
- 误差边界：恢复越激进（跳过越多），后续映射偏移风险越大；关键是每跳过一段就以「生成位置」为基准重新锚定，而非沿用源码行号推算。
- 追问钩子：面试官问「能不能干脆出错就中止编译」——答：IDE 场景需要错误恢复支持实时补全，所以用「映射+锚定」保证局部准确；CI 严格模式则失败即停，map 不重要。

```javascript
// 错误恢复：跳过非法区间后重新锚定生成列
function recoverMap(mappings, skippedChars) {
  // 跳过区间不产生 segment；后续以生成列为基准继续
  return mappings.map(seg => ({ ...seg,
    note: skippedChars ? `跳过 ${skippedChars} 字符后重新锚定` : null }));
}
const segs = [
  { genCol: 0, origLine: 1, origCol: 0 }, // 合法
  { genCol: 4, origLine: 1, origCol: 10 }, // 跳过 6 字符后，origCol 真实锚定
];
console.log(recoverMap(segs, 6)[1]);
// { genCol:4, origLine:1, origCol:10, note:'跳过 6 字符后重新锚定' }
```
