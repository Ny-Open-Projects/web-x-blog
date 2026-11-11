// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133493400

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual); // 把 JSON.stringify(actual) 存入 数组
  const e = JSON.stringify(expected); // 把 JSON.stringify(expected) 存入 e
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function topKFrequent(nums: number[], k: number): number[] {
  // 定义函数/方法 topKFrequent
  const freq = new Map<number, number>(); // 把 new Map 小于 number, number 超过 () 存入 频次表
  for (const num of nums) freq.set(num, (freq.get(num) || 0) + 1); // for (const num of 数组) 频次表.set(num, (频次表 查找 num) 或 0) 加 1);
  const heap: [number, number][] = []; // 把 []; 写入 const heap: [number, number][]
  for (const [num, cnt] of freq) {
    // for (const [num, 计数] of 频次表) {
    heap.push([cnt, num]); // 把 [计数, num] 压入栈/数组尾部
    heap.sort((a, b) => a[0] - b[0]); // min-heap by cnt via sort (small n)
    if (heap.length > k) heap.shift(); // 若 堆.长度 超过 下标 k) 堆.shift();
  }
  return heap.map(([, num]) => num);
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(
    topKFrequent([1, 1, 1, 2, 2, 3], 2)
      .slice()
      .sort((a, b) => a - b),
    [1, 2],
    'topKFrequent',
  );
  assertEq(topKFrequent([1], 1), [1], 'topKFrequent single'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
