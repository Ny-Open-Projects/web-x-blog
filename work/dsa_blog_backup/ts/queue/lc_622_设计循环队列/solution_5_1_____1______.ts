// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130471048
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  class MyCircularQueue {
    // 定义类型
    private capacity: number; // private capacity: number;
    private data: number[]; // private data: number[];
    private front: number; // private front: number;
    private rear: number; // private rear: number;
    private size: number; // private 大小: number;
    constructor(k: number) {
      // constructor(下标 k: number) {
      this.capacity = k; // 把 下标 k; 写入 this.capacity
      this.data = new Array(k).fill(0); // 把 new Array(下标 k).fill(0); 写入 this.data
      this.front = 0; // 把 0; 写入 this.front
      this.rear = 0; // 把 0; 写入 this.rear
      this.size = 0; // 把 0; 写入 大小
    }
    enQueue(value: number): boolean {
      // enQueue(value: number): boolean {
      if (this.isFull()) return false; // 若 this.isFull()，直接返回 false
      this.data[this.rear] = value; // 把 value; 写入 this.data[this.rear]
      this.rear = (this.rear + 1) % this.capacity; // 把 (this.rear 加 1) 对…取模 this.capacity; 写入 this.rear
      this.size += 1; // this.size累加 1
      return true; // 返回 true
    }
    deQueue(): boolean {
      // deQueue(): boolean {
      if (this.isEmpty()) return false; // 若 this.isEmpty()，直接返回 false
      this.front = (this.front + 1) % this.capacity; // 把 (this.front 加 1) 对…取模 this.capacity; 写入 this.front
      this.size -= 1; // this.size累减 1
      return true; // 返回 true
    }
    Front(): number {
      // Front(): number {
      if (this.isEmpty()) return -1; // 若 this.isEmpty()，直接返回 减 1
      return this.data[this.front]; // 返回 this.data[this.front]
    }
    Rear(): number {
      // Rear(): number {
      if (this.isEmpty()) return -1; // 若 this.isEmpty()，直接返回 减 1
      return this.data[(this.rear - 1 + this.capacity) % this.capacity];
    }
    isEmpty(): boolean {
      return this.size === 0;
    } // 把 等于 0; } 写入 大小
    isFull(): boolean {
      return this.size === this.capacity;
    } // 把 等于 this.capacity; } 写入 大小
  }
  function solution(): (boolean | number)[] {
    // 定义函数/方法 solution
    const q = new MyCircularQueue(3); // 把 new MyCircularQueue(3) 存入 节点
    const results: (boolean | number)[] = []; // 把 []; 写入 const results: (boolean | number)[]
    results.push(q.enQueue(1)); // 把 节点.enQueue(1 压入栈/数组尾部
    results.push(q.enQueue(2)); // 把 节点.enQueue(2 压入栈/数组尾部
    results.push(q.enQueue(3)); // 把 节点.enQueue(3 压入栈/数组尾部
    results.push(q.enQueue(4)); // 把 节点.enQueue(4 压入栈/数组尾部
    results.push(q.Rear()); // 把 节点.Rear( 压入栈/数组尾部
    results.push(q.isFull()); // 把 节点.isFull( 压入栈/数组尾部
    results.push(q.deQueue()); // 把 节点.deQueue( 压入栈/数组尾部
    results.push(q.enQueue(4)); // 把 节点.enQueue(4 压入栈/数组尾部
    results.push(q.Rear()); // 把 节点.Rear( 压入栈/数组尾部
    return results; // 返回 results
  }
  const want: (boolean | number)[] = [
    true,
    true,
    true,
    false,
    3,
    true,
    true,
    true,
    4,
  ];
  const got = solution(); // 把 solution() 存入 got
  let fail = false; // 把 false 存入 fail
  if (got.length !== want.length) {
    fail = true;
    console.log('FAIL length got ' + got.length);
  } else {
    // 否则
    for (let i = 0; i < want.length; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 want.长度 就继续
      if (got[i] !== want[i]) {
        fail = true;
        console.log(
          'FAIL idx ' +
            i +
            ' got ' +
            String(got[i]) +
            ' want ' +
            String(want[i]),
        );
      }
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
