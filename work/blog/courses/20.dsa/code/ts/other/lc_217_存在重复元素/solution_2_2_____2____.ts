// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145344295
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function containsDuplicate(nums: number[]): boolean {
    // 定义函数/方法 containsDuplicate
    const seen = new Set<number>(); // 把 new Set 小于 number 超过 () 存入 已见集合
    for (const v of nums) {
      if (seen.has(v)) return true;
      seen.add(v);
    }
    return false; // 返回 false
  }
  const cases = [
    { in: [1, 2, 3], want: false },
    { in: [1, 2, 2], want: true },
    { in: [0], want: false },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = containsDuplicate(c.in); // 把 containsDuplicate(字符.in) 存入 got
    if (got !== c.want) {
      fail = true;
      console.log('FAIL ' + got + ' want ' + c.want);
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
