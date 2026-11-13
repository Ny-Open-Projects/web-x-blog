// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145245934
// Faithful translation of python reference. Self-check via demo().
function last(arr: number[]): number {
  return arr[arr.length - 1];
} // 定义函数/方法 last
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  class MinStack {
    // 定义类型
    stack: number[] = []; // 把 []; 写入 stack: number[]
    mins: number[] = []; // 把 []; 写入 mins: number[]
    push(val: number): void {
      // push(值: number): void {
      this.stack.push(val); // 把 值 压入栈/数组尾部
      this.mins.push(this.mins.length ? Math.min(last(this.mins), val) : val); // 把 this.mins.长度 ? Math.取较小值 last(this.mins 压入栈/数组尾部
    }
    pop(): void {
      this.stack.pop();
      this.mins.pop();
    } // 弹出栈顶元素
    top(): number {
      return this.stack[this.stack.length - 1];
    } // top(): number { return this.栈[this.栈.长度 减 1]; }
    getMin(): number {
      return last(this.mins);
    } // getMin(): number { return last(this.mins); }
  }
  const minStack = new MinStack(); // 把 new MinStack() 存入 minStack
  minStack.push(-2);
  minStack.push(0);
  minStack.push(-3); // 把 减 2 压入栈/数组尾部
  const got = [
    minStack.getMin(),
    (minStack.pop(), minStack.top()),
    minStack.getMin(),
  ];
  const want = [-3, 0, -2]; // 把 [ 减 3, 0, 减 2] 存入 want
  for (let i = 0; i < got.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 got.长度 就继续
    if (got[i] !== want[i])
      throw new Error('FAIL idx ' + i + ' got ' + got[i] + ' want ' + want[i]);
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
