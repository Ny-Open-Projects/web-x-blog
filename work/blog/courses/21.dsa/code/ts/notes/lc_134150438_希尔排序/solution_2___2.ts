// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134150438

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function shellSort(lst: number[]): number[] {
  // 定义函数/方法 shellSort
  const a = lst.slice();
  const length = a.length;
  let gap = Math.floor(length / 2);
  while (gap > 0) {
    // 循环，直到不满足「gap 超过 0」
    for (let i = gap; i < length; i++) {
      // 让 下标 i 从 gap 开始计数，下标 i 小于 长度 就继续
      const tmp = a[i];
      let p = i; // 把 数组[下标 i]; let 节点 赋值为 下标 i 存入 临时变量
      while (p - gap >= 0 && a[p - gap] > tmp) {
        a[p] = a[p - gap];
        p -= gap;
      }
      a[p] = tmp; // 把 临时变量; 写入 a[p]
    }
    gap = Math.floor(gap / 2); // 把 向下取整(gap 除以 2) 存入 gap
  }
  return a; // 返回 数组
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(
    shellSort([9, 12, 1, 3, -1, 22, 22, 31, 1, 0]),
    [-1, 0, 1, 1, 3, 9, 12, 22, 22, 31],
    'shell',
  ); // 断言校验
  assertEq(shellSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5], 'rev'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
