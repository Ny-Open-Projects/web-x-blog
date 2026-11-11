// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134053461
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function gnomeSort(arr: number[]): number[] {
    // 定义函数/方法 gnomeSort
    const length = arr.length; // 把 数组.长度 存入 长度
    let i = 1; // 把 1 存入 下标 i
    while (i < length) {
      // 循环，直到不满足「下标 i 小于 长度」
      if (i < 1 || arr[i - 1] <= arr[i]) {
        // 若 下标 i 小于 1 或 数组[下标 i 减 1] 不超过 数组[下标 i]
        i++; // 下标 i 加一
      } else {
        // 否则
        const tmp = arr[i - 1];
        arr[i - 1] = arr[i];
        arr[i] = tmp;
        i--; // 下标 i 减一
      }
    }
    return arr; // 返回 数组
  }
  const cases: [number[], number[]][] = [
    [
      [5, 4, 3, 2, 1],
      [1, 2, 3, 4, 5],
    ],
    [
      [3, 1, 2],
      [1, 2, 3],
    ],
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const inp = c[0];
    const want = c[1]; // 把 字符[0]; const want 赋值为 字符[1] 存入 inp
    const got = gnomeSort(inp.slice()); // 把 gnomeSort(inp 截取 )) 存入 got
    if (JSON.stringify(got) !== JSON.stringify(want)) {
      fail = true;
      console.log(
        'FAIL gnomeSort(' +
          JSON.stringify(inp) +
          ')=' +
          JSON.stringify(got) +
          ' want ' +
          JSON.stringify(want),
      );
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
