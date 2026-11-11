// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130540333
// LeetCode 72. 编辑距离 — Rust 版（方案1）
fn min_distance(w1: String, w2: String) -> i32 {
    // 定义函数/方法 min_distance
    let a: Vec<char> = w1.chars().collect(); // 把 w1.chars().collect(); 写入 let a: Vec<char>
    let b: Vec<char> = w2.chars().collect(); // 把 w2.chars().collect(); 写入 let b: Vec<char>
    let (m, n) = (a.len(), b.len()); // 把 (数组.长度(), b.长度()); 写入 let (m, n)
    let mut dp = vec![0i32; n + 1]; // 把 vec取反 [0i32; 元素个数 加 1]; 写入 let mut dp
    for j in 0..=n {
        dp[j] = j as i32;
    } // 逐个取出 0 的元素（下标 j）
    for i in 1..=m {
        // 逐个取出 1 的元素（下标 i）
        let mut prev_diag = dp[0]; // 把 DP 表[0]; 写入 let mut prev_diag
        dp[0] = i as i32; // 把 下标 i as i32; 写入 dp[0]
        for j in 1..=n {
            // 逐个取出 1 的元素（下标 j）
            let tmp = dp[j]; // 把 DP 表[下标 j] 存入 临时变量
            dp[j] = if a[i - 1] == b[j - 1] {
                prev_diag
            } else {
                1 + prev_diag.min(dp[j]).min(dp[j - 1])
            };
            prev_diag = tmp; // 把 临时变量; 写入 prev_diag
        }
    }
    dp[n] // DP 表[元素个数]
}
fn main() {
    assert_eq!(min_distance("horse".into(), "ros".into()), 3);
    assert_eq!(min_distance("intention".into(), "execution".into()), 5);
    println!("PASS");
} // 程序入口：跑内嵌自测用例
