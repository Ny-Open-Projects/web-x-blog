// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130444168
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function letterCombinations(digits: string): string[] {
    // 定义函数/方法 letterCombinations
    if (!digits) return []; // 若 取反 digits，直接返回 []
    const mapping: { [k: string]: string } = {
      // 把 { 写入 const mapping: { [k: string]: string }
      '2': 'abc',
      '3': 'def',
      '4': 'ghi',
      '5': 'jkl',
      '6': 'mno',
      '7': 'pqrs',
      '8': 'tuv',
      '9': 'wxyz',
    };
    let combos: string[] = ['']; // 把 [「」]; 写入 let combos: string[]
    for (const d of digits) {
      // for (const d of digits) {
      const chars = mapping[d]; // 把 mapping[d] 存入 chars
      if (!chars) continue; // 若 取反 chars) continue;
      const next: string[] = []; // 把 []; 写入 const next: string[]
      for (const p of combos) {
        // for (const 节点 of combos) {
        for (const c of chars) {
          // for (const 字符 of chars) {
          next.push(p + c); // 把 节点 加 字符 压入栈/数组尾部
        }
      }
      combos = next; // 把 下一个 存入 combos
    }
    return combos; // 返回 combos
  }
  const cases: Array<[string, string[]]> = [
    ['23', ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']],
    ['', []],
    ['2', ['a', 'b', 'c']],
  ];
  let fail = false; // 把 false 存入 fail
  for (const cs of cases) {
    // for (const cs of cases) {
    const got = letterCombinations(cs[0]); // 把 letterCombinations(cs[0]) 存入 got
    if (got.length !== cs[1].length || !cs[1].every((e, i) => e === got[i])) {
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL letterCombinations(' +
          JSON.stringify(cs[0]) +
          ') got ' +
          JSON.stringify(got) +
          ' want ' +
          JSON.stringify(cs[1]),
      ); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
