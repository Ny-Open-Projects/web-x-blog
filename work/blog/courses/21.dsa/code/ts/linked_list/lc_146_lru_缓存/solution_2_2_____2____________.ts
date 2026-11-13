/**
 ** LeetCode 146. LRU 缓存
 ** 方案：2 ) 方案2: 哈希表 + 双向链表
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145094527
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  // DLinkedNode 忠实翻译 python ref solution_2_2_____2____________.py
  class DLinkedNode {
    // 定义类型
    key: number; // key: number;
    value: number; // value: number;
    prev: DLinkedNode | null; // 前一个: DLinkedNode 按位或 null;
    next: DLinkedNode | null; // 下一个: DLinkedNode 按位或 null;

    constructor(key = 0, value = 0) {
      // 把 0, value 赋值为 0) { 写入 constructor(key
      this.key = key; // 把 key; 写入 this.key
      this.value = value; // 把 value; 写入 this.value
      this.prev = null; // 把 null; 写入 前一个
      this.next = null; // 把 null; 写入 下一个
    }
  }

  // LRUCache 忠实翻译 python ref（dummy head/tail + addToHead/removeNode/moveToHead/removeTail）
  class LRUCache {
    // 定义类型
    private capacity: number; // private capacity: number;
    private cache: Map<number, DLinkedNode> = new Map(); // 把 new Map(); 写入 private cache: Map<number, DLinkedNode>
    private size = 0; // 把 0; 写入 private size
    private head: DLinkedNode; // private 头节点: DLinkedNode;
    private tail: DLinkedNode; // private 尾节点: DLinkedNode;

    constructor(capacity: number) {
      // constructor(capacity: number) {
      this.capacity = capacity; // 把 capacity; 写入 this.capacity
      this.head = new DLinkedNode(); // 把 new DLinkedNode(); 写入 头节点
      this.tail = new DLinkedNode(); // 把 new DLinkedNode(); 写入 尾节点
      this.head.next = this.tail; // 把 this.尾节点; 写入 下一个
      this.tail.prev = this.head; // 把 this.头节点; 写入 前一个
    }

    private addToHead(node: DLinkedNode): void {
      // private addToHead(节点: DLinkedNode): void {
      node.prev = this.head; // 把 this.头节点; 写入 前一个
      node.next = this.head.next; // 把 this.头节点.下一个; 写入 下一个
      (this.head.next as DLinkedNode).prev = node; // 把 节点; 写入 前一个
      this.head.next = node; // 把 节点; 写入 下一个
    }

    private removeNode(node: DLinkedNode): void {
      // private removeNode(节点: DLinkedNode): void {
      (node.prev as DLinkedNode).next = node.next; // 把 节点.下一个; 写入 下一个
      (node.next as DLinkedNode).prev = node.prev; // 把 节点.前一个; 写入 前一个
    }

    private moveToHead(node: DLinkedNode): void {
      // private moveToHead(节点: DLinkedNode): void {
      this.removeNode(node); // this.removeNode(节点);
      this.addToHead(node); // this.addToHead(节点);
    }

    private removeTail(): DLinkedNode {
      // private removeTail(): DLinkedNode {
      const node = this.tail.prev as DLinkedNode; // 把 this.尾节点.前一个 as DLinkedNode 存入 节点
      this.removeNode(node); // this.removeNode(节点);
      return node; // 返回 节点
    }

    get(key: number): number {
      // get(key: number): number {
      if (!this.cache.has(key)) {
        // 若 取反 this.cache.has(key
        return -1; // 返回 减 1
      }
      const node = this.cache.get(key) as DLinkedNode; // 把 this.cache 查找 key) as DLinkedNode 存入 节点
      this.moveToHead(node); // this.moveToHead(节点);
      return node.value; // 返回 节点.value
    }

    put(key: number, value: number): void {
      // put(key: number, value: number): void {
      if (!this.cache.has(key)) {
        // 若 取反 this.cache.has(key
        const newNode = new DLinkedNode(key, value); // 把 new DLinkedNode(key, value) 存入 newNode
        this.cache.set(key, newNode); // this.cache.set(key, newNode);
        this.addToHead(newNode); // this.addToHead(newNode);
        this.size += 1; // this.size累加 1
        if (this.size > this.capacity) {
          // 若 this.大小 超过 this.capacity
          const removed = this.removeTail(); // 把 this.removeTail() 存入 removed
          this.cache.delete(removed.key); // this.cache.delete(removed.key);
          this.size -= 1; // this.size累减 1
        }
      } else {
        // 否则
        const node = this.cache.get(key) as DLinkedNode; // 把 this.cache 查找 key) as DLinkedNode 存入 节点
        node.value = value; // 把 value; 写入 node.value
        this.moveToHead(node); // this.moveToHead(节点);
      }
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
