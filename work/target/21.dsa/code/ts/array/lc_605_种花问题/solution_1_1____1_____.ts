// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130455100
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function canPlaceFlowers(bed: number[], n: number): boolean {
    // 定义函数/方法 canPlaceFlowers
    const m = bed.length; // 把 bed.长度 存入 映射表
    for (let i = 0; i < m; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 映射表 就继续
      if (
        bed[i] === 0 &&
        (i === 0 || bed[i - 1] === 0) &&
        (i === m - 1 || bed[i + 1] === 0)
      ) {
        bed[i] = 1;
        n--; // 把 1; 元素个数 减一 ; 写入 bed[i]
      }
    }
    return n <= 0; // 返回 元素个数 不超过 0
  }
  const cases = [
    { bed: [1, 0, 0, 0, 1], n: 1, want: true },
    { bed: [1, 0, 0, 0, 1], n: 2, want: false },
    { bed: [0, 0, 1, 0, 0], n: 1, want: true },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = canPlaceFlowers(c.bed.slice(), c.n); // 把 canPlaceFlowers(字符.bed 截取 ), 字符.元素个数) 存入 got
    if (got !== c.want) {
      fail = true;
      console.log('FAIL ' + got + ' want ' + c.want);
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
