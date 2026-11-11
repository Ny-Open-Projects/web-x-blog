// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130590161
// LeetCode 115. 不同的子序列 — Rust 版（方案1）
fn num_distinct(s: String, t: String) -> i32 {
    // 定义函数/方法 num_distinct
    let a: Vec<char> = s.chars().collect(); // 把 字符串.chars().collect(); 写入 let a: Vec<char>
    let b: Vec<char> = t.chars().collect(); // 把 另一字符串.chars().collect(); 写入 let b: Vec<char>
    let (m, n) = (a.len(), b.len()); // 把 (数组.长度(), b.长度()); 写入 let (m, n)
    let mut dp = vec![0i64; n + 1]; // 把 vec取反 [0i64; 元素个数 加 1]; 写入 let mut dp
    dp[0] = 1; // 把 1; 写入 dp[0]
    for i in 1..=m {
        // 逐个取出 1 的元素（下标 i）
        for j in (1..=n).rev() {
            // 把 元素个数).rev() { 写入 for j in (1
            if a[i - 1] == b[j - 1] {
                dp[j] += dp[j - 1];
            }
        }
    }
    dp[n] as i32 // DP 表[元素个数] as i32
}
fn main() {
    assert_eq!(num_distinct("rabbbit".into(), "rabbit".into()), 3);
    assert_eq!(num_distinct("babgbag".into(), "bag".into()), 5);
    println!("PASS");
} // 程序入口：跑内嵌自测用例
