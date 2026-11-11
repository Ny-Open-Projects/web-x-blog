/**
 ** LeetCode 202. 快乐数
 ** 方案：方案1：计算每位平方和
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145355335
 */

export function bitSquareSum(n: number): number {
  // 定义函数/方法 bitSquareSum
  let total = 0; // 把 0 存入 总和
  while (n) {
    // 循环，直到不满足「元素个数」
    const digit = n % 10; // 把 元素个数 对…取模 10 存入 digit
    total += digit * digit; // 总和累加 digit 乘 digit
    n = Math.floor(n / 10); // 把 向下取整(元素个数 除以 10) 存入 元素个数
  }
  return total; // 返回 总和
}

function isHappy(n: number): boolean {
  // 定义判定函数 isHappy：哈希集合判圈
  const seen = new Set<number>(); // 已见集合
  while (n !== 1 && !seen.has(n)) {
    // 未到 1 且未成环
    seen.add(n); // 记录当前值
    n = bitSquareSum(n); // 下一状态 = 各位平方和
  }
  return n === 1; // 收敛到 1 即快乐数
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  if (bitSquareSum(1) !== 1) throw new Error('FAILED 1'); // 若 bitSquareSum(1) 不等于 1) throw new Error(「FAILED 1」);
  if (bitSquareSum(19) !== 82)
    throw new Error('FAILED 19: ' + bitSquareSum(19));
  if (bitSquareSum(82) !== 68) throw new Error('FAILED 82'); // 若 bitSquareSum(82) 不等于 68) throw new Error(「FAILED 82」);
  if (isHappy(19) !== true) throw new Error('FAILED 19');
  if (isHappy(2) !== false) throw new Error('FAILED 2');
  if (isHappy(7) !== true) throw new Error('FAILED 7');
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
