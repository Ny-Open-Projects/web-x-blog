/**
 ** LeetCode 202. 快乐数
 ** 方案：2 ) 方案2：哈希判圈
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145355335
 */

export function isHappy(n: number): boolean {
  // 快乐数判定：哈希判圈（原 getNum 更名正名）  // 定义函数/方法 getNum
  const seen = new Set<number>(); // 把 new Set 小于 number 超过 () 存入 已见集合
  while (n !== 1) {
    // 循环，直到不满足「元素个数 不等于 1」
    if (seen.has(n)) return false; // 若 已见集合.has(元素个数)，直接返回 false
    seen.add(n); // 已见集合 追加 元素个数);
    let sum = 0; // 把 0 存入 累计和
    let x = n; // 把 元素个数 存入 x
    while (x) {
      // 循环，直到不满足「x」
      const d = x % 10; // 把 x 对…取模 10 存入 d
      sum += d * d; // 累计和累加 d 乘 d
      x = Math.floor(x / 10); // 把 向下取整(x 除以 10) 存入 x
    }
    n = sum; // 把 累计和 存入 元素个数
  }
  return true; // 返回 true
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  if (!isHappy(1)) throw new Error('FAILED 1'); // 若 取反 isHappy(1)) throw new Error(「FAILED 1」);
  if (!isHappy(19)) throw new Error('FAILED 19'); // 若 取反 isHappy(19)) throw new Error(「FAILED 19」);
  if (isHappy(2)) throw new Error('FAILED 2 (should be unhappy)');
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
