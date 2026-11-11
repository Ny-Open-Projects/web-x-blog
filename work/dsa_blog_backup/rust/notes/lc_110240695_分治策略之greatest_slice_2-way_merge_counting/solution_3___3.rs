// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/110240695
// LeetCode 110240695. 分治策略之 greatest slice — Rust 版（方案C：分治 best/prefix/suffix/total）
fn max_sub_array_dc(arr: &[i32]) -> i64 {
    // 定义函数/方法 max_sub_array_dc
    fn helper(arr: &[i32], lo: usize, hi: usize) -> (i64, i64, i64, i64) {
        // 定义函数/方法 helper
        // (best, prefix, suffix, total)
        if hi - lo == 1 {
            // 若 右边界 减 左边界 等于 1
            let v = arr[lo] as i64; // 把 数组[左边界] as i64 存入 值
            return (v, v, v, v); // 返回 (值, 值, 值, 值)
        }
        let mi = (lo + hi) / 2; // 把 (左边界 加 右边界) 除以 2 存入 mi
        let (l_best, l_pre, l_suf, l_sum) = helper(arr, lo, mi); // 把 helper(数组, 左边界, mi); 写入 let (l_best, l_pre, l_suf, l_sum)
        let (r_best, r_pre, r_suf, r_sum) = helper(arr, mi, hi); // 把 helper(数组, mi, 右边界); 写入 let (r_best, r_pre, r_suf, r_sum)
        let crossing = l_suf + r_pre; // 把 l_suf 加 r_pre 存入 crossing
        let best = l_best.max(r_best).max(crossing); // 把 l_best.取较大值 r_best).取较大值 crossing) 存入 当前最优
        let prefix = l_pre.max(l_sum + r_pre); // 把 l_pre.取较大值 l_sum 加 r_pre) 存入 prefix
        let suffix = r_suf.max(r_sum + l_suf); // 把 r_suf.取较大值 r_sum 加 l_suf) 存入 suffix
        let total = l_sum + r_sum; // 把 l_sum 加 r_sum 存入 总和
        (best, prefix, suffix, total) // (当前最优, prefix, suffix, 总和)
    }
    if arr.is_empty() {
        // 若 数组.is_empty(
        return 0; // 返回 0
    }
    helper(arr, 0, arr.len()).0 // helper(数组, 0, 数组.长度()).0
}

fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(max_sub_array_dc(&[-2, 1, -3, 4, -1, 2, 1]), 6, "ms1"); // 断言校验
    assert_eq!(max_sub_array_dc(&[1, 2, 3]), 6, "ms2"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
