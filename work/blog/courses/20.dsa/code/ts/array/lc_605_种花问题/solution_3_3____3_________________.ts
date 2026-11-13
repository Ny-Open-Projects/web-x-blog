// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130455100
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function canPlaceFlowers(flowerbed: number[], n: number): boolean {
    // 定义函数/方法 canPlaceFlowers
    const m: number = flowerbed.length; // 把 flowerbed.长度; 写入 const m: number
    let cnt: number = 0; // 把 0; 写入 let cnt: number
    for (let i = 0; i < m; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 映射表 就继续
      if (
        flowerbed[i] === 0 &&
        (i === 0 || flowerbed[i - 1] === 0) &&
        (i === m - 1 || flowerbed[i + 1] === 0) // 把 等于 映射表 减 1 或 flowerbed[下标 i 加 1] 全等于 0) 写入 (i
      ) {
        // ) {
        flowerbed[i] = 1; // 把 1; 写入 flowerbed[i]
        cnt++; // 计数 加一
        if (cnt >= n) return true; // 若 计数 不低于 元素个数，直接返回 true
      }
    }
    return cnt >= n; // 返回 计数 不低于 元素个数
  }
  const cases: Array<[number[], number, boolean]> = [
    [[1, 0, 0, 0, 1], 1, true],
    [[1, 0, 0, 0, 1], 2, false],
    [[0], 1, true],
  ];
  let fail = false; // 把 false 存入 fail
  for (const cs of cases) {
    // for (const cs of cases) {
    const got = canPlaceFlowers(cs[0].slice(), cs[1]); // 把 canPlaceFlowers(cs[0] 截取 ), cs[1]) 存入 got
    if (got !== cs[2]) {
      // 若 got 不等于 cs[2]
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL canPlaceFlowers(' +
          JSON.stringify(cs[0]) +
          ',' +
          cs[1] +
          ') got ' +
          got +
          ' want ' +
          cs[2],
      ); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
