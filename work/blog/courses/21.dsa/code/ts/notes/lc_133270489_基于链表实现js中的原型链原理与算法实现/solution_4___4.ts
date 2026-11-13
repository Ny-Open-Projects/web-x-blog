// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function instanceOf(A: any, B: any): boolean {
    // 定义函数/方法 instanceOf
    let p = A; // 把 A 存入 节点
    while (p) {
      // 循环，直到不满足「节点」
      if (p === B.prototype) return true; // 若 节点 全等于 B.prototype，直接返回 true
      p = p.__proto__; // 把 节点.__proto__ 存入 节点
    }
    return false; // 返回 false
  }
  const cases: { got: boolean; want: boolean }[] = [
    { got: instanceOf(null, null), want: false },
    { got: instanceOf(undefined, undefined), want: false },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    if (c.got !== c.want) {
      fail = true;
      console.log('FAIL got', c.got, 'want', c.want);
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
