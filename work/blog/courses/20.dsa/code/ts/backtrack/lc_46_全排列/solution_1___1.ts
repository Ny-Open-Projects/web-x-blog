// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134689827
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function permute(nums: number[]): number[][] {
    // 定义函数/方法 permute
    const res: number[][] = []; // 把 []; 写入 const res: number[][]
    function backtrack(path: number[]) {
      // 定义函数/方法 backtrack
      if (path.length === nums.length) {
        res.push(path.slice());
        return;
      } // 若 当前路径.长度 全等于 数组.长度) { 结果 追加 当前路径 截取 )); return; }
      for (let i = 0; i < nums.length; i++) {
        // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
        if (path.indexOf(nums[i]) !== -1) continue; // 若 当前路径 查找 数组[下标 i]) 不等于 减 1) continue;
        backtrack(path.concat([nums[i]])); // 打印输出
      }
    }
    backtrack([]); // backtrack([]);
    return res; // 返回 结果
  }
  function eqSet(a: number[][], b: number[][]): boolean {
    // 定义函数/方法 eqSet
    if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    const key = (x: number[]) =>
      x
        .slice()
        .sort((p, q) => p - q)
        .join(',');
    const sa = new Set(a.map(key)); // 把 new Set(数组.映射表(key)) 存入 sa
    const sb = new Set(b.map(key)); // 把 new Set(b.映射表(key)) 存入 sb
    if (sa.size !== sb.size) return false; // 若 sa.大小 不等于 sb.大小，直接返回 false
    for (const k of sa) if (!sb.has(k)) return false; // for (const 下标 k of sa) if (取反 sb.has(下标 k)) return false;
    return true; // 返回 true
  }
  const want = [
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2],
    [3, 2, 1],
  ];
  const got = permute([1, 2, 3]); // 把 permute([1, 2, 3]) 存入 got
  let fail = false; // 把 false 存入 fail
  if (!eqSet(got, want)) {
    fail = true;
    console.log('FAIL permute got=' + JSON.stringify(got));
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
