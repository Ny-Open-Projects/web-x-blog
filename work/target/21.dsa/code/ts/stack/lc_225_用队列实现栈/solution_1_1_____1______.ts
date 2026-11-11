// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145113825

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

class MyStack {
  // 定义类型
  q1: number[];
  q2: number[]; // q1: number[]; q2: number[];
  constructor() {
    this.q1 = [];
    this.q2 = [];
  } // 把 []; this.q2 赋值为 []; } 写入 constructor() { this.q1
  push(x: number): void {
    this.q2.push(x);
    while (this.q1.length) this.q2.push(this.q1.shift()!);
    const t = this.q1;
    this.q1 = this.q2;
    this.q2 = t;
  } // 把 x 压入栈/数组尾部
  pop(): number {
    return this.q1.shift()!;
  } // 取出队首元素
  top(): number {
    return this.q1[0];
  } // top(): number { return this.q1[0]; }
  empty(): boolean {
    return this.q1.length === 0;
  } // 把 等于 0; } 写入 长度
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const obj = new MyStack(); // 把 new MyStack() 存入 obj
  obj.push(1);
  obj.push(2); // 把 1 压入栈/数组尾部
  assertEq(obj.top(), 2, 'top'); // 断言校验
  assertEq(obj.pop(), 2, 'pop'); // 断言校验
  assertEq(obj.empty(), false, 'empty'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
