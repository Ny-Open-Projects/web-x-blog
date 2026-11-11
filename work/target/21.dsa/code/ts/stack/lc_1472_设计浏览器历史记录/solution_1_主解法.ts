// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145354313

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

class BrowserHistory {
  // 定义类型
  history: string[];
  current: number; // history: string[]; current: number;
  constructor(homepage: string) {
    this.history = [homepage];
    this.current = 0;
  }
  visit(url: string): void {
    this.history = this.history.slice(0, this.current + 1);
    this.history.push(url);
    this.current = this.history.length - 1;
  } // 把 url 压入栈/数组尾部
  back(steps: number): string {
    this.current = Math.max(0, this.current - steps);
    return this.history[this.current];
  }
  forward(steps: number): string {
    this.current = Math.min(this.history.length - 1, this.current + steps);
    return this.history[this.current];
  }
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const browser = new BrowserHistory('leetcode.com'); // 把 new BrowserHistory(「leetcode.com」) 存入 browser
  browser.visit('google.com'); // browser.visit(「google.com」);
  browser.visit('facebook.com'); // browser.visit(「facebook.com」);
  browser.visit('youtube.com'); // browser.visit(「youtube.com」);
  assertEq(browser.back(1), 'facebook.com', 'back1'); // 断言校验
  assertEq(browser.forward(2), 'youtube.com', 'fwd2'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
