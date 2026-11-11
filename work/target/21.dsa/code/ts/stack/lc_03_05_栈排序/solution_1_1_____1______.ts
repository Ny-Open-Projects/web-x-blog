// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397311

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

class SortedStack {
  // 定义类型
  stk1: number[];
  stk2: number[]; // stk1: number[]; stk2: number[];
  constructor() {
    this.stk1 = [];
    this.stk2 = [];
  } // 把 []; this.stk2 赋值为 []; } 写入 constructor() { this.stk1
  push(val: number): void {
    // push(值: number): void {
    while (this.stk1.length && this.stk1[this.stk1.length - 1] > val)
      this.stk2.push(this.stk1.pop()!);
    this.stk1.push(val); // 把 值 压入栈/数组尾部
    while (this.stk2.length) this.stk1.push(this.stk2.pop()!); // 循环，直到不满足「this.stk2.长度) this.stk1 追加 this.stk2 弹出 )取反 );」
  }
  pop(): void {
    if (!this.isEmpty()) this.stk1.pop();
  } // 弹出栈顶元素
  peek(): number {
    if (this.isEmpty()) return -1;
    return this.stk1[this.stk1.length - 1];
  }
  isEmpty(): boolean {
    return this.stk1.length === 0;
  } // 把 等于 0; } 写入 长度
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const s = new SortedStack(); // 把 new SortedStack() 存入 字符串
  for (const v of [4, 2, 5, 1, 3]) s.push(v); // 把 值 压入栈/数组尾部
  const out: number[] = []; // 把 []; 写入 const out: number[]
  while (!s.isEmpty()) {
    out.push(s.peek());
    s.pop();
  }
  assertEq(out, [5, 4, 3, 2, 1], 'sorted'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
