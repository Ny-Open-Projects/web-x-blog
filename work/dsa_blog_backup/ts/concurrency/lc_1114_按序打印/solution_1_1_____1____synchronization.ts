/**
 ** LeetCode 1114. 按序打印
 ** 方案：1 ) 方案1：使用 synchronization
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145385760
 */

class Foo {
  // 定义类型
  private firstResolve: () => void = () => {};
  private secondResolve: () => void = () => {};
  private firstDone: Promise<void>; // private firstDone: Promise 小于 void 超过 ;
  private secondDone: Promise<void>; // private secondDone: Promise 小于 void 超过 ;

  constructor() {
    // constructor() {
    this.firstDone = new Promise<void>((resolve) => {
      this.firstResolve = resolve;
    });
    this.secondDone = new Promise<void>((resolve) => {
      this.secondResolve = resolve;
    });
  }

  first(printFirst: () => void): void {
    printFirst(); // printFirst();
    this.firstResolve(); // this.firstResolve();
  }

  async second(printSecond: () => void): Promise<void> {
    await this.firstDone; // await this.firstDone;
    printSecond(); // printSecond();
    this.secondResolve(); // this.secondResolve();
  }

  async third(printThird: () => void): Promise<void> {
    await this.secondDone; // await this.secondDone;
    printThird(); // printThird();
  }
}

export async function demo(): Promise<void> {
  // 程序入口：跑内嵌自测用例
  const out: string[] = []; // 把 []; 写入 const out: string[]
  const foo = new Foo(); // 把 new Foo() 存入 foo
  await Promise.all([
    foo.third(() => out.push('third')),
    foo.second(() => out.push('second')),
    foo.first(() => out.push('first')),
  ]); // ]);
  if (out.join(' ') !== 'first second third') {
    // 若 out.join(「 」) 不等于 「 」
    throw new Error('FAILED: ' + out.join(' ')); // 拼接为字符串
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo().catch((e) => {
  console.error(String(e));
  process.exit(1);
});
