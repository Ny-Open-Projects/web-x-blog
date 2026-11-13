// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130687299
// LeetCode 1027. 最长等差数列 — Rust 版（方案1）
use std::collections::HashMap; // 引入依赖
fn longest_arith_seq_length(nums: Vec<i32>) -> i32 {
    // 定义函数/方法 longest_arith_seq_length
    let n = nums.len(); // 把 数组.长度() 存入 元素个数
    let mut dp: Vec<HashMap<i32, i32>> = vec![HashMap::new(); n];
    let mut best = 1; // 把 1; 写入 let mut best
    for i in 0..n {
        // 逐个取出 0 的元素（下标 i）
        for j in 0..i {
            // 逐个取出 0 的元素（下标 j）
            let d = nums[i] - nums[j]; // 把 数组[下标 i] 减 数组[下标 j] 存入 d
            let cur = dp[j].get(&d).copied().unwrap_or(1) + 1; // 把 DP 表[下标 j] 查找 按位与 d).copied().unwrap_or(1) 加 1 存入 当前值
            dp[i].insert(d, cur); // DP 表[下标 i] 插入 d, 当前值);
            if cur > best {
                best = cur;
            } // 若 当前值 超过 当前最优 { 当前最优 赋值为 当前值; }
        }
    }
    best // 当前最优
}
fn main() {
    assert_eq!(longest_arith_seq_length(vec![9, 4, 7, 2, 10]), 3);
    assert_eq!(longest_arith_seq_length(vec![3, 6, 9, 12]), 4);
    println!("PASS");
} // 程序入口：跑内嵌自测用例
