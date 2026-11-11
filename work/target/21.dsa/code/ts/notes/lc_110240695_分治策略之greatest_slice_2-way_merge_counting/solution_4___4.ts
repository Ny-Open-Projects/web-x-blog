// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/110240695

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function max_sub_array_dc(arr: number[]): number {
  // 定义函数/方法 max_sub_array_dc
  function helper(lo: number, hi: number): [number, number, number, number] {
    // 定义函数/方法 helper
    if (hi - lo === 1) {
      const v = arr[lo];
      return [v, v, v, v];
    }
    const mi = Math.floor((lo + hi) / 2); // 把 向下取整((左边界 加 右边界) 除以 2) 存入 mi
    const [l_best, l_pre, l_suf, l_sum] = helper(lo, mi); // 把 helper(左边界, mi); 写入 const [l_best, l_pre, l_suf, l_sum]
    const [r_best, r_pre, r_suf, r_sum] = helper(mi, hi); // 把 helper(mi, 右边界); 写入 const [r_best, r_pre, r_suf, r_sum]
    const crossing = l_suf + r_pre; // 把 l_suf 加 r_pre 存入 crossing
    const best = Math.max(l_best, r_best, crossing); // 把 Math.取较大值 l_best, r_best, crossing) 存入 当前最优
    const prefix = Math.max(l_pre, l_sum + r_pre); // 把 Math.取较大值 l_pre, l_sum 加 r_pre) 存入 prefix
    const suffix = Math.max(r_suf, r_sum + l_suf); // 把 Math.取较大值 r_suf, r_sum 加 l_suf) 存入 suffix
    const total = l_sum + r_sum; // 把 l_sum 加 r_sum 存入 总和
    return [best, prefix, suffix, total]; // 返回 [当前最优, prefix, suffix, 总和]
  }
  if (!arr.length) return 0; // 若 取反 数组.长度，直接返回 0
  return helper(0, arr.length)[0]; // 返回 helper(0, 数组.长度)[0]
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(max_sub_array_dc([-2, 1, -3, 4, -1, 2, 1]), 6, 'ms1'); // 断言校验
  assertEq(max_sub_array_dc([1, 2, 3]), 6, 'ms2'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
