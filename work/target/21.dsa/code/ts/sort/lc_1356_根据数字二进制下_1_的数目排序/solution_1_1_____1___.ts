// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145381295
/**
 ** LeetCode 1356. 根据数字二进制下 1 的数目排序
 ** 方案：方案1（暴力统计 1 的个数）
 */

function onesCount(x: number): number {
  // 定义函数/方法 onesCount
  let c = 0; // 把 0 存入 字符
  let v = x; // 把 x 存入 值
  while (v > 0) {
    // 循环，直到不满足「值 超过 0」
    c += v % 2; // 字符累加 值 对…取模 2
    v = Math.floor(v / 2); // 把 向下取整(值 除以 2) 存入 值
  }
  return c; // 返回 字符
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  if (onesCount(1) !== 1) throw new Error('onesCount(1) should be 1');
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
