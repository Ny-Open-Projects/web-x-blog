// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130683917
// LeetCode 322. 零钱兑换 — Rust 版（方案1）
fn coin_change(coins: Vec<i32>, amount: i32) -> i32 {
    // 定义函数/方法 coin_change
    let mut dp = vec![i32::MAX; amount as usize + 1]; // 把 vec取反 [i32::MAX; 目标金额 as usize 加 1]; 写入 let mut dp
    dp[0] = 0; // 把 0; 写入 dp[0]
    for a in 1..=amount as usize {
        // 逐个取出 1 的元素（数组）
        for &c in &coins {
            // for 按位与 字符 in 按位与 硬币面额 {
            if c as usize <= a && dp[a - c as usize] != i32::MAX {
                // 若 字符 as usize 不超过 数组 且 DP 表[数组 减 字符 as usize] 不等于 i32::MAX
                dp[a] = dp[a].min(dp[a - c as usize] + 1); // 把 DP 表[数组].取较小值 DP 表[数组 减 字符 as usize] 加 1); 写入 dp[a]
            }
        }
    }
    if dp[amount as usize] == i32::MAX {
        -1
    } else {
        dp[amount as usize]
    }
}
fn main() {
    assert_eq!(coin_change(vec![1, 2, 5], 11), 3);
    assert_eq!(coin_change(vec![2], 3), -1);
    assert_eq!(coin_change(vec![1], 0), 0);
    println!("PASS");
} // 程序入口：跑内嵌自测用例
