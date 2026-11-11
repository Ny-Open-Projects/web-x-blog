// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145244140
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function eraseOverlapIntervals(intervals: number[][][] | null): number {
    // 定义函数/方法 eraseOverlapIntervals
    if (!intervals || intervals.length === 0) return 0; // 若 取反 intervals 或 intervals.长度 全等于 0，直接返回 0
    const arr = intervals.slice().sort((a, b) => a[1] - b[1]);
    let count = 1; // 把 1 存入 计数
    let end = arr[0][1]; // 把 数组[0][1] 存入 终点
    for (let i = 1; i < arr.length; i++) {
      // 让 下标 i 从 1 开始计数，下标 i 小于 数组.长度 就继续
      if (arr[i][0] >= end) {
        count++;
        end = arr[i][1];
      } // 若 数组[下标 i][0] 不低于 终点) { 计数 加一 ; 终点 赋值为 数组[下标 i][1]; }
    }
    return arr.length - count; // 返回 数组.长度 减 计数
  }
  const cases = [
    {
      in: [
        [1, 2],
        [2, 3],
        [3, 4],
        [1, 3],
      ],
      want: 1,
    },
    { in: [], want: 0 },
    {
      in: [
        [1, 2],
        [1, 3],
        [1, 4],
      ],
      want: 2,
    },
    { in: null, want: 0 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = eraseOverlapIntervals(c.in); // 把 eraseOverlapIntervals(字符.in) 存入 got
    if (got !== c.want) {
      fail = true;
      console.log(
        'FAIL eraseOverlapIntervals(' +
          JSON.stringify(c.in) +
          ')=' +
          got +
          ' want ' +
          c.want,
      );
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
