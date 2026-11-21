---
title: "[话术JB-072] Object·wait与notify（语法语义）· 7 问"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## Object · wait与notify（语法语义）—— 7 类问法与标准话术

**Qjava-basics-498（概念考察·P4-P6）**
【面试官】请谈谈你对「Object」中「wait与notify」的理解。
【标准回答话术】wait/notify/notifyAll 是 Object 的 final 方法，必须在 synchronized 块内调用，否则抛 IllegalMonitorStateException。背后的原理是：wait 释放锁进入等待集，notify/notifyAll 唤醒等待线程重新竞争锁。
【评分点】① 准确说出核心机制（wait与notify）；② 能带出原理层而非背结论。 ③ 版本锚点：JLS 17.2

---

**Qjava-basics-499（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「wait 可以在任意位置调用。」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：wait/notify/notifyAll 是 Object 的 final 方法，必须在 synchronized 块内调用，否则抛 IllegalMonitorStateException。原因是：wait 释放锁进入等待集，notify/notifyAll 唤醒等待线程重新竞争锁。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（JLS 17.2）。

---

**Qjava-basics-500（原理深挖·P5-P7）**
【面试官】「wait与notify」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：wait 释放锁进入等待集，notify/notifyAll 唤醒等待线程重新竞争锁。落到结论：wait/notify/notifyAll 是 Object 的 final 方法，必须在 synchronized 块内调用，否则抛 IllegalMonitorStateException。
【评分点】① 讲出语法语义层面的机制；② 结论与机制对应不脱节。

---

**Qjava-basics-501（工程落地·P7-P9）**
【面试官】在你带过的项目里，「wait与notify」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：notify 在锁释放前不生效（锁释放后等待线程才真正被唤醒）。事实依据：wait/notify/notifyAll 是 Object 的 final 方法，必须在 synchronized 块内调用，否则抛 IllegalMonitorStateException。常见误区要规避：wait 可以在任意位置调用。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qjava-basics-502（版本演进·P8-P10）**
【面试官】关于「wait与notify」，版本上有什么需要特别注意的？
【标准回答话术】版本锚点：JLS 17.2。事实层面：wait/notify/notifyAll 是 Object 的 final 方法，必须在 synchronized 块内调用，否则抛 IllegalMonitorStateException。
【评分点】① 知道机制随版本的变化；② 面试回答带版本限定词（禁绝对化）。

---

**Qjava-basics-503（边界追问·P6-P9）**
【面试官】「wait与notify」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「wait 可以在任意位置调用。」是常见误区。正确的边界：wait/notify/notifyAll 是 Object 的 final 方法，必须在 synchronized 块内调用，否则抛 IllegalMonitorStateException。使用要点：notify 在锁释放前不生效（锁释放后等待线程才真正被唤醒）。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qjava-basics-504（追问链·P5-P8）**
【面试官】追问：如果有人按「notify 会立即释放锁。」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：wait/notify/notifyAll 是 Object 的 final 方法，必须在 synchronized 块内调用，否则抛 IllegalMonitorStateException。原理：wait 释放锁进入等待集，notify/notifyAll 唤醒等待线程重新竞争锁。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
