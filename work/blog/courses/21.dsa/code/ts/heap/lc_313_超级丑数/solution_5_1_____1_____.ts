// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133625091

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function nthSuperUglyNumber(n: number, primes: number[]): number {
  // 定义函数/方法 nthSuperUglyNumber
  const ugly = new Array(n).fill(1); // 把 new Array(元素个数).fill(1) 存入 ugly
  const idx = new Array(primes.length).fill(0); // 把 new Array(primes.长度).fill(0) 存入 idx
  const val = primes.slice(); // 把 primes 截取 ) 存入 值
  for (let i = 1; i < n; i++) {
    // 让 下标 i 从 1 开始计数，下标 i 小于 元素个数 就继续
    let next = Infinity; // 把 Infinity 存入 下一个
    for (let k = 0; k < primes.length; k++) next = Math.min(next, val[k]); // 让 下标 k 从 0 开始计数，下标 k 小于 primes.长度 就继续
    ugly[i] = next; // 把 下一个; 写入 ugly[i]
    for (let k = 0; k < primes.length; k++) {
      // 让 下标 k 从 0 开始计数，下标 k 小于 primes.长度 就继续
      if (val[k] === next) {
        idx[k]++;
        val[k] = ugly[idx[k]] * primes[k];
      }
    }
  }
  return ugly[n - 1]; // 返回 ugly[元素个数 减 1]
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(nthSuperUglyNumber(12, [2, 7, 13, 19]), 32, 'ugly12'); // 断言校验
  assertEq(nthSuperUglyNumber(1, [2, 7, 13, 19]), 1, 'ugly1'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
