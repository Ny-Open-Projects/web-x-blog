// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130641517
// LeetCode 62. 不同路径 — Rust 版（方案2）
fn unique_paths(m: i32, n: i32) -> i32 {
    // 定义函数/方法 unique_paths
    let mut dp = vec![1i32; n as usize]; // 把 vec取反 [1i32; 元素个数 as usize]; 写入 let mut dp
    for _ in 1..m {
        // 逐个取出 1 的元素（_）
        for j in 1..n as usize {
            dp[j] += dp[j - 1];
        } // 逐个取出 1 的元素（下标 j）
    }
    dp[n as usize - 1] // DP 表[元素个数 as usize 减 1]
}
fn main() {
    assert_eq!(unique_paths(3, 7), 28);
    assert_eq!(unique_paths(3, 2), 3);
    assert_eq!(unique_paths(1, 1), 1);
    println!("PASS");
} // 程序入口：跑内嵌自测用例
