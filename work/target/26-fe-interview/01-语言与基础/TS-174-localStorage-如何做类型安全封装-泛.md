---
title: [TS-174] localStorage 如何做类型安全封装（泛型 + 版本迁移）？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-174：localStorage 如何做类型安全封装（泛型 + 版本迁移）？
**答**：
- 存储条目带版本号 `{ v, data }`，读取时版本匹配走校验、不匹配走迁移函数。
- validate 是运行时防线（localStorage 天然不可信），migrate 负责 v1→v2 数据形状演进。
- 泛型 T 由调用方声明，get/set 全链路同类型。

```typescript
interface Entry<T> { v: number; data: T }

class TypedStore<T> {
  constructor(
    private key: string,
    private version: number,
    private validate: (raw: unknown) => T | null,
    private migrate: (old: unknown, from: number) => T,
  ) {}

  get(): T | null {
    const raw = localStorage.getItem(this.key);
    if (!raw) return null;
    const parsed = JSON.parse(raw) as Entry<unknown>;
    if (parsed.v === this.version) return this.validate(parsed.data);
    return this.migrate(parsed.data, parsed.v); // 旧版本数据走迁移链
  }

  set(data: T) {
    const entry: Entry<T> = { v: this.version, data };
    localStorage.setItem(this.key, JSON.stringify(entry));
  }
}

const prefStore = new TypedStore<{ theme: "dark" | "light" }>(
  "pref",
  2,
  (raw) => (typeof raw === "object" && raw !== null && "theme" in raw)
    ? raw as { theme: "dark" | "light" }
    : null,
  (old) => ({ theme: (old as { dark?: boolean }).dark ? "dark" : "light" }), // v1.dark → v2.theme
);
```

**追问**：

1. 存储被外部写坏、`JSON.parse` 抛错会怎样？ → get 直接抛出导致整页崩溃；必须 try/catch，解析失败时返回 null 并清掉这个坏键。
2. 迁移函数抛错或返回不合法的数据怎么办？ → 应回退到默认值、删除旧键并上报，否则每次读取都会在同一处抛错，形成死循环。
3. localStorage 写满抛 `QuotaExceededError` 怎么处理？ → set 必须 try/catch，触发缓存淘汰或提示用户清理，不能假设写入一定成功。
