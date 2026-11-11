// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114011
// Faithful translation of python reference. Self-check via demo().
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  class MyQueue {
    // 定义类型
    inStack: number[] = []; // 把 []; 写入 inStack: number[]
    outStack: number[] = []; // 把 []; 写入 outStack: number[]
    push(x: number): void {
      this.inStack.push(x);
    } // 把 x 压入栈/数组尾部
    pop(): number {
      // pop(): number {
      if (this.outStack.length === 0) this._in2out(); // 若 this.outStack.长度 全等于 0) this._in2out();
      return this.outStack.pop()!; // 返回 this.outStack 弹出 )取反
    }
    peek(): number {
      // peek(): number {
      if (this.outStack.length === 0) this._in2out(); // 若 this.outStack.长度 全等于 0) this._in2out();
      return this.outStack[this.outStack.length - 1]; // 返回 this.outStack[this.outStack.长度 减 1]
    }
    empty(): boolean {
      return this.outStack.length === 0 && this.inStack.length === 0;
    } // 把 等于 0 且 this.inStack.长度 全等于 0; } 写入 长度
    _in2out(): void {
      // _in2out(): void {
      while (this.inStack.length) this.outStack.push(this.inStack.pop()!);
    }
  }
  const q = new MyQueue(); // 把 new MyQueue() 存入 节点
  q.push(1);
  q.push(2); // 把 1 压入栈/数组尾部
  const got = [q.peek(), q.pop(), q.empty()]; // 把 [节点.peek(), 节点 弹出 ), 节点 是否为空] 存入 got
  q.push(3); // 把 3 压入栈/数组尾部
  got.push(q.pop());
  got.push(q.pop()); // 把 节点 弹出 压入栈/数组尾部
  const want = [1, 1, false, 2, 3]; // 把 [1, 1, false, 2, 3] 存入 want
  for (let i = 0; i < got.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 got.长度 就继续
    if (got[i] !== want[i])
      throw new Error('FAIL idx ' + i + ' got ' + got[i] + ' want ' + want[i]);
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
