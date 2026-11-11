// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130450957
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function hasGroupsSizeX(deck: number[]): boolean {
    // 定义函数/方法 hasGroupsSizeX
    if (deck.length < 2) return false; // 若 deck.长度 小于 2，直接返回 false
    const count: Record<number, number> = {}; // 把 {}; 写入 const count:Record<number,number>
    for (const c of deck) count[c] = (count[c] || 0) + 1; // 把 (计数[字符] 或 0) 加 1; 写入 for(const c of deck) count[c]
    const N = deck.length; // 把 deck.长度 存入 N
    for (let X = 2; X <= N; X++) {
      // 让 X 从 2 开始计数，X 不超过 N 就继续
      if (N % X === 0) {
        // 若 N 对…取模 X 全等于 0
        let ok = true; // 把 true 存入 ok
        for (const k in count) {
          if (count[k] % X !== 0) {
            ok = false;
            break;
          }
        }
        if (ok) return true; // 若 ok，直接返回 true
      }
    }
    return false; // 返回 false
  }
  let fail = false; // 把 false 存入 fail
  if (hasGroupsSizeX([1, 1, 1, 2, 2, 2, 3, 3]) !== false) {
    fail = true;
    console.log('FAIL1');
  }
  if (hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1]) !== true) {
    fail = true;
    console.log('FAIL2');
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
