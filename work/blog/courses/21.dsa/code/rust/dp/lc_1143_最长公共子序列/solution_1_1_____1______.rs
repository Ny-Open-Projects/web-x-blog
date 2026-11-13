// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130815631
// LeetCode 1143. 最长公共子序列 — Rust 版（方案1）
fn longest_common_subsequence(t1: String, t2: String) -> i32 {
    // 定义函数/方法 longest_common_subsequence
    let a: Vec<char> = t1.chars().collect(); // 把 t1.chars().collect(); 写入 let a: Vec<char>
    let b: Vec<char> = t2.chars().collect(); // 把 t2.chars().collect(); 写入 let b: Vec<char>
    let (m, n) = (a.len(), b.len()); // 把 (数组.长度(), b.长度()); 写入 let (m, n)
    let mut dp = vec![0i32; n + 1]; // 把 vec取反 [0i32; 元素个数 加 1]; 写入 let mut dp
    for i in 1..=m {
        // 逐个取出 1 的元素（下标 i）
        let mut prev_diag = 0; // 把 0; 写入 let mut prev_diag
        for j in 1..=n {
            // 逐个取出 1 的元素（下标 j）
            let tmp = dp[j]; // 把 DP 表[下标 j] 存入 临时变量
            dp[j] = if a[i - 1] == b[j - 1] {
                prev_diag + 1
            } else {
                dp[j].max(dp[j - 1])
            };
            prev_diag = tmp; // 把 临时变量; 写入 prev_diag
        }
    }
    dp[n] // DP 表[元素个数]
}
fn main() {
    assert_eq!(longest_common_subsequence("abcde".into(), "ace".into()), 3);
    assert_eq!(longest_common_subsequence("abc".into(), "abc".into()), 3);
    assert_eq!(longest_common_subsequence("abc".into(), "def".into()), 0);
    println!("PASS");
} // 程序入口：跑内嵌自测用例
