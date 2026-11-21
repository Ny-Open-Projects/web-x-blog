---
title: [DP-162] 回调地狱与面条代码的根源是什么？除了 async/await 还要做什么？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-162：回调地狱与面条代码的根源是什么？除了 async/await 还要做什么？（高频）
**答**：
- 根源不是"没用 async/await"，而是：一个函数承担多个职责、错误处理路径与主路径缠绕、步骤间通过共享可变量隐式通信。
- async/await 只解决"嵌套形状"，不解决"职责纠缠"——还要配合：每步提成命名函数（步骤可测）、错误集中到一个 catch + 分类策略（DP-149）、共享状态收敛为上下文对象。
- 长流程再考虑职责链/状态机（DP-103），别一上来就上模式。

```javascript
// 反面教材：职责纠缠 + 共享可变量 + 错误路径缠绕
let result, tmp;                                               // 全局可变中间态
function importCsv(file, done) {
  parse(file, (rows) => {
    validate(rows, (ok) => {
      if (!ok) { done('校验失败'); return; }
      dedupe(rows, (clean) => {
        tmp = clean;                                           // 隐式通信：靠外层变量传值
        save(clean, (r) => {
          result = r;
          report(r); done(null, result);                       // 埋点和主流程混在一起
        }, (e) => done(e));
      }, (e) => done(e));
    });
  }, (e) => done(e));
}
```

```javascript
// 重构：每步一个命名纯函数 + 上下文对象 + 集中错误分类
async function importCsv2(file) {                              // 主路径一线贯穿
  const rows = await parseCsv(file);                           // 步骤1 解析
  const valid = await validateRows(rows);                      // 步骤2 校验（不合法 throw）
  const clean = dedupeRows(valid);                             // 步骤3 去重（纯函数）
  const saved = await saveRows(clean);                         // 步骤4 落库
  reportQueue.push({ op: 'import-csv', count: saved.count });  // 埋点走观察者队列，不混主流程
  return saved;
}
// 调用层：一处 catch，按类型分治（策略见 DP-149）
importCsv2(file)
  .then((r) => toast(`导入 ${r.count} 条成功`))
  .catch(async (e) => {
    if (e instanceof ValidationError) return toast('文件内容有误：' + e.field);
    if (e instanceof NetworkError) return retryQueue.enqueue(() => importCsv2(file));
    reportError(e);                                            // 未知错误上报
  });
```
