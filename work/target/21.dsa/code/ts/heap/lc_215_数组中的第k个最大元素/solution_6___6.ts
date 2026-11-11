// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
// Faithful translation of python reference. Self-check via demo().
class MinHeap {
  // 定义类型
  heap: number[] = []; // 把 []; 写入 heap: number[]
  size(): number {
    return this.heap.length;
  } // 大小(): number { return this.堆.长度; }
  peak(): number {
    return this.heap[0];
  } // peak(): number { return this.堆[0]; }
  insert(val: number): void {
    // insert(值: number): void {
    this.heap.push(val); // 把 值 压入栈/数组尾部
    let i = this.heap.length - 1; // 把 this.堆.长度 减 1 存入 下标 i
    while (i > 0) {
      // 循环，直到不满足「下标 i 超过 0」
      const p = (i - 1) >> 1; // 把 (下标 i 减 1) 超过 超过 1 存入 节点
      if (this.heap[p] <= this.heap[i]) break; // 若 this.堆[节点] 不超过 this.堆[下标 i]) break;
      const t = this.heap[p];
      this.heap[p] = this.heap[i];
      this.heap[i] = t;
      i = p; // 把 节点 存入 下标 i
    }
  }
  pop(): number {
    // pop(): number {
    const top = this.heap[0]; // 把 this.堆[0] 存入 top
    const last = this.heap.pop()!; // 把 this.堆 弹出 )取反 存入 last
    if (this.heap.length > 0) {
      // 若 this.堆.长度 超过 0
      this.heap[0] = last; // 把 last; 写入 this.heap[0]
      let i = 0; // 把 0 存入 下标 i
      const n = this.heap.length; // 把 this.堆.长度 存入 元素个数
      while (true) {
        // 循环，直到不满足「true」
        let l = 2 * i + 1,
          r = 2 * i + 2,
          sm = i; // 把 2 乘 下标 i 加 1, 右指针 赋值为 2 乘 下标 i 加 2, sm 赋值为 下标 i 存入 左指针
        if (l < n && this.heap[l] < this.heap[sm]) sm = l; // 若 左指针 小于 元素个数 且 this.堆[左指针] 小于 this.堆[sm]) sm 赋值为 左指针;
        if (r < n && this.heap[r] < this.heap[sm]) sm = r; // 若 右指针 小于 元素个数 且 this.堆[右指针] 小于 this.堆[sm]) sm 赋值为 右指针;
        if (sm === i) break; // 若 sm 全等于 下标 i) break;
        const t = this.heap[sm];
        this.heap[sm] = this.heap[i];
        this.heap[i] = t;
        i = sm; // 把 sm 存入 下标 i
      }
    }
    return top; // 返回 top
  }
}

function find_kth_largest(nums: number[], k: number): number {
  // 定义函数/方法 find_kth_largest
  const h = new MinHeap(); // 把 new MinHeap() 存入 h
  for (const n of nums) {
    // for (const 元素个数 of 数组) {
    h.insert(n); // h 插入 元素个数);
    if (h.size() > k) h.pop(); // 若 h.大小() 超过 下标 k) h 弹出 );
  }
  return h.peak(); // 返回 h.peak()
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const cases = [
    [[3, 2, 1, 5, 6, 4], 2],
    [[3, 2, 3, 1, 2, 4, 5, 5, 6], 4],
  ];
  const want = [5, 4]; // 把 [5, 4] 存入 want
  for (let i = 0; i < cases.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 cases.长度 就继续
    const got = find_kth_largest(cases[i][0].slice(), cases[i][1]);
    if (got !== want[i])
      throw new Error('FAIL case ' + i + ' got ' + got + ' want ' + want[i]);
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
