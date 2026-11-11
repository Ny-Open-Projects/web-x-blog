// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/110240695
// LeetCode 110240695. 分治策略之 greatest slice — Rust 版（方案A：暴力枚举所有子段）
fn max_sub_array_bf(arr: &[i32]) -> i64 {
    // 定义函数/方法 max_sub_array_bf
    let mut best = i64::MIN; // 把 i64::MIN; 写入 let mut best
    for i in 0..arr.len() {
        // 逐个取出 0 的元素（下标 i）
        let mut s = 0i64; // 把 0i64; 写入 let mut s
        for j in i..arr.len() {
            // 逐个取出 下标 i 的元素（下标 j）
            s += arr[j] as i64; // 字符串累加 数组[下标 j] as i64
            if s > best {
                // 若 字符串 超过 当前最优
                best = s; // 把 字符串; 写入 当前最优
            }
        }
    }
    best // 当前最优
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let cases: Vec<(Vec<i32>, i64)> = vec![
        (vec![-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        (vec![1], 1),
        (vec![-1, -2, -3], -1),
        (vec![5, 4, -1, 7, 8], 23),
    ];
    for (idx, (arr, want)) in cases.iter().enumerate() {
        // for (idx, (数组, want)) in cases.iter().enumerate() {
        assert_eq!(max_sub_array_bf(arr), *want, "case {} failed", idx); // 断言校验
    }
    println!("PASS"); // 全部用例通过，输出 PASS
}
