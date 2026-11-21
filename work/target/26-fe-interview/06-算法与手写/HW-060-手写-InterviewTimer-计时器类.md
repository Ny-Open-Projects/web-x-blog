---
title: [HW-060] 手写 InterviewTimer 计时器类
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-060：手写 InterviewTimer 计时器类

**答**：
- 评分点：**封装能力**是本题核心考点——私有状态（私有字段 `#` 或 `_` 前缀）、对外只暴露方法与只读 getter；计时用「**累计 + 时间戳**」法：pause/stop 时把本段时长累加进 total，resume 记录新的起点——绝不靠 setInterval 累加秒数（后台标签页会被节流导致不准，必讲）；状态机完整：idle → running → paused → stopped，非法状态转移要拒绝（如 idle 时 pause）；onTick 订阅每秒回调（展示事件封装）；stop 返回总时长并清理定时器防泄漏。

```javascript
// ===== 5 分钟速写版 =====
class InterviewTimer {
  #total = 0;        // 已累计毫秒
  #startAt = null;   // 当前段起点
  #state = 'idle';
  start() {
    if (this.#state !== 'idle') return;
    this.#startAt = Date.now();
    this.#state = 'running';
  }
  pause() {
    if (this.#state !== 'running') return;
    this.#total += Date.now() - this.#startAt; // 本段时长入账
    this.#startAt = null;
    this.#state = 'paused';
  }
  resume() {
    if (this.#state !== 'paused') return;
    this.#startAt = Date.now();
    this.#state = 'running';
  }
  stop() {
    if (this.#state === 'running') this.#total += Date.now() - this.#startAt;
    this.#state = 'stopped';
    return this.elapsed;
  }
  get elapsed() { // 只读出口
    return this.#total + (this.#state === 'running' ? Date.now() - this.#startAt : 0);
  }
}

// ===== 标准完整版（含边界处理）=====
class InterviewTimerPro {
  #total = 0;
  #startAt = null;
  #state = 'idle';
  #timer = null;
  #listeners = new Set();
  static IDLE = 'idle';
  static RUNNING = 'running';
  static PAUSED = 'paused';
  static STOPPED = 'stopped';
  get state() { return this.#state; }
  get elapsed() {
    // 用「累计值 + 当前段差值」实时计算，不依赖 interval 累加（防后台节流失准）
    return this.#total + (this.#state === InterviewTimerPro.RUNNING ? Date.now() - this.#startAt : 0);
  }
  get isRunning() { return this.#state === InterviewTimerPro.RUNNING; }
  start() {
    if (this.#state !== InterviewTimerPro.IDLE) {
      throw new Error(`cannot start from state: ${this.#state}`); // 状态机保护
    }
    this.#startAt = Date.now();
    this.#state = InterviewTimerPro.RUNNING;
    this.#scheduleTick();
    return this;
  }
  pause() {
    if (this.#state !== InterviewTimerPro.RUNNING) return this;
    this.#total += Date.now() - this.#startAt; // 入账后再清起点
    this.#startAt = null;
    this.#state = InterviewTimerPro.PAUSED;
    this.#clearTick();
    return this;
  }
  resume() {
    if (this.#state !== InterviewTimerPro.PAUSED) return this;
    this.#startAt = Date.now();
    this.#state = InterviewTimerPro.RUNNING;
    this.#scheduleTick();
    return this;
  }
  stop() {
    if (this.#state === InterviewTimerPro.RUNNING) {
      this.#total += Date.now() - this.#startAt;
      this.#startAt = null;
    }
    if (this.#state === InterviewTimerPro.STOPPED) return this.elapsed; // 幂等：重复 stop 无副作用
    this.#state = InterviewTimerPro.STOPPED;
    this.#clearTick();
    return this.elapsed; // 返回总毫秒
  }
  onTick(fn) {                       // 每秒广播一次（展示 UI）
    if (typeof fn !== 'function') throw new TypeError('listener must be a function');
    this.#listeners.add(fn);
    return () => this.#listeners.delete(fn); // 退订函数
  }
  #scheduleTick() {                  // 私有方法：仅驱动订阅回调，不参与计时
    this.#clearTick();
    this.#timer = setInterval(() => {
      const seconds = Math.floor(this.elapsed / 1000);
      [...this.#listeners].forEach(fn => fn(seconds, this.elapsed));
    }, 1000);
  }
  #clearTick() {
    if (this.#timer) { clearInterval(this.#timer); this.#timer = null; }
  }
  format(ms = this.elapsed) {        // 00:05:30 展示格式
    const s = Math.floor(ms / 1000);
    const h = String(Math.floor(s / 3600)).padStart(2, '0');
    const m = String(Math.floor(s % 3600 / 60)).padStart(2, '0');
    return `${h}:${m}:${String(s % 60).padStart(2, '0')}`;
  }
  destroy() { this.stop(); this.#listeners.clear(); } // 兜底清理
}
// 设计话术：计时真相只存在 elapsed getter 一处（单一数据源）；
// interval 只负责「提醒 UI 刷新」，崩了也不影响时长准确性。
```

---

## 结语：手写题应答心法

1. **先沟通再动笔**：确认函数签名、边界约定（如 get 不存在返回 -1 还是 undefined）、参数语义（times 是总次数还是重试次数）——这本身就是评分项。
2. **主干优先**：5 分钟内先写出能跑的主路径，再口头补充边界（「空数组我会先 resolve 掉，避免 pending」），比闷头写完美版更得分。
3. **边界自查三件套**：参数校验（类型 / 正整数 / 可迭代）、空输入（空数组 / 空对象 / 空字符串）、资源清理（timer、监听器、AbortController）。
4. **主动关联原理**：手写 useState 时讲 Hooks 顺序对齐，手写 p-limit 时讲浏览器并发限制——把「手写」升级成「原理验证」，是拉开差距的关键。
5. **高频回炉**：HW-001、014/015、016、021、040、050 是真实面试出现率最高的六题，考前一天务必盲写一遍。
