/**
 ** LeetCode 146. LRU 缓存
 ** 方案：1 ) 方案1: 基于Map（有序字典语义）
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145094527
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  // LRUCache 忠实翻译 python ref solution_1_1_____1____Map.py（利用 Map 保序：get 时 delete+set 移到末尾，淘汰时删第一个键）
  class LRUCache {
    // 定义类型
    private capacity: number; // private capacity: number;
    private cache: Map<number, number> = new Map(); // 把 new Map(); 写入 private cache: Map<number, number>

    constructor(capacity: number) {
      // constructor(capacity: number) {
      this.capacity = capacity; // 把 capacity; 写入 this.capacity
    }

    get(key: number): number {
      // get(key: number): number {
      if (!this.cache.has(key)) {
        // 若 取反 this.cache.has(key
        return -1; // 返回 减 1
      }
      // Move to end (most recently used)
      const val = this.cache.get(key) as number; // 把 this.cache 查找 key) as number 存入 值
      this.cache.delete(key); // this.cache.delete(key);
      this.cache.set(key, val); // this.cache.set(key, 值);
      return val; // 返回 值
    }

    put(key: number, value: number): void {
      // put(key: number, value: number): void {
      if (this.cache.has(key)) {
        // 若 this.cache.has(key
        this.cache.delete(key); // this.cache.delete(key);
      } else if (this.cache.size >= this.capacity) {
        // 否则，若 this.cache.大小 不低于 this.capacity
        // Remove oldest (first item)
        const oldest = this.cache.keys().next().value as number; // 把 this.cache.keys().下一个().value as number 存入 oldest
        this.cache.delete(oldest); // this.cache.delete(oldest);
      }
      this.cache.set(key, value); // this.cache.set(key, value);
    }
  }

  type Op = ['put', number, number] | ['get', number]; // 定义类型

  interface Case {
    // 定义类型
    cap: number; // cap: number;
    ops: Op[]; // ops: Op[];
    want: (number | null)[]; // want: (number 按位或 null)[];
  }

  // want 由 python ref 实跑操作序列得到
  const cases: Case[] = [
    {
      cap: 2,
      ops: [
        ['put', 1, 1],
        ['put', 2, 2],
        ['get', 1],
        ['put', 3, 3],
        ['get', 2],
        ['put', 4, 4],
        ['get', 1],
        ['get', 3],
        ['get', 4],
      ],
      want: [null, null, 1, null, -1, null, -1, 3, 4],
    },
    {
      cap: 1,
      ops: [
        ['get', 1],
        ['put', 1, 1],
        ['get', 1],
        ['put', 2, 2],
        ['get', 1],
        ['get', 2],
        ['put', 2, 22],
        ['get', 2],
      ],
      want: [-1, null, 1, null, -1, 2, null, 22],
    },
    {
      cap: 2,
      ops: [
        ['put', 1, 1],
        ['put', 1, 10],
        ['get', 1],
        ['put', 2, 2],
        ['put', 3, 3],
        ['get', 1],
        ['get', 2],
        ['get', 3],
      ],
      want: [null, null, 10, null, null, -1, 2, 3],
    },
  ];

  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const cache = new LRUCache(c.cap); // 把 new LRUCache(字符.cap) 存入 cache
    const got: (number | null)[] = []; // 把 []; 写入 const got: (number | null)[]
    for (const op of c.ops) {
      // for (const op of 字符.ops) {
      if (op[0] === 'put') {
        // 若 op[0] 全等于 「put」
        cache.put(op[1], op[2]); // cache.put(op[1], op[2]);
        got.push(null); // 把 null 压入栈/数组尾部
      } else {
        // 否则
        got.push(cache.get(op[1])); // 把 cache 查找 op[1] 压入栈/数组尾部
      }
    }
    for (let i = 0; i < got.length; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 got.长度 就继续
      if (got[i] !== c.want[i]) {
        // 若 got[下标 i] 不等于 字符.want[下标 i]
        fail = true; // 把 true 存入 fail
        console.log(
          `FAIL cap=${c.cap} idx=${i} got=${got[i]} want=${c.want[i]}`,
        );
      }
    }
  }
  if (fail) {
    // 若 fail
    throw new Error('FAILED'); // throw new Error(「FAILED」);
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
