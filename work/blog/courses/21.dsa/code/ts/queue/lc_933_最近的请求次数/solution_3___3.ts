// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130470370
// Faithful translation of python reference. Self-check via demo().
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  class RecentCounter {
    // 定义类型
    q: number[] = []; // 把 []; 写入 q: number[]
    ping(t: number): number {
      // ping(另一字符串: number): number {
      this.q.push(t); // 把 另一字符串 压入栈/数组尾部
      while (this.q[0] < t - 3000) this.q.shift(); // 循环，直到不满足「this.节点[0] 小于 另一字符串 减 3000) this.节点.shift();」
      return this.q.length; // 返回 this.节点.长度
    }
  }
  const c = new RecentCounter(); // 把 new RecentCounter() 存入 字符
  const got = [c.ping(1), c.ping(100), c.ping(3001), c.ping(3002)];
  const want = [1, 2, 3, 3]; // 把 [1, 2, 3, 3] 存入 want
  for (let i = 0; i < got.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 got.长度 就继续
    if (got[i] !== want[i])
      throw new Error('FAIL case ' + i + ' got ' + got[i] + ' want ' + want[i]);
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
