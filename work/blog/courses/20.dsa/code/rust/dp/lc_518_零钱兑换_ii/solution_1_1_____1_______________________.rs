// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130734179
// LeetCode 518. 零钱兑换II — Rust 版（方案1）
fn change(amount: i32, coins: Vec<i32>) -> i32 {
    // 定义函数/方法 change
    let mut dp = vec![0i64; amount as usize + 1]; // 把 vec取反 [0i64; 目标金额 as usize 加 1]; 写入 let mut dp
    dp[0] = 1; // 把 1; 写入 dp[0]
    for &c in &coins {
        // for 按位与 字符 in 按位与 硬币面额 {
        for a in c as usize..=amount as usize {
            // 逐个取出 字符 的元素（数组）
            dp[a] += dp[a - c as usize]; // dp[a]累加 DP 表[数组 减 字符 as usize]
        }
    }
    dp[amount as usize] as i32 // DP 表[目标金额 as usize] as i32
}
fn main() {
    assert_eq!(change(5, vec![1, 2, 5]), 4);
    assert_eq!(change(3, vec![2]), 0);
    assert_eq!(change(10, vec![1, 2, 5]), 10);
    assert_eq!(change(0, vec![1, 2]), 1);
    println!("PASS");
} // 程序入口：跑内嵌自测用例
