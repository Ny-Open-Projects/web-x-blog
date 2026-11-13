// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130613988
// LeetCode 583. 两个字符串的删除操作 — Rust 版（方案2）
fn min_distance(w1: String, w2: String) -> i32 {
    // 定义函数/方法 min_distance
    // 删除操作 = m + n - 2 * LCS
    let a: Vec<char> = w1.chars().collect(); // 把 w1.chars().collect(); 写入 let a: Vec<char>
    let b: Vec<char> = w2.chars().collect(); // 把 w2.chars().collect(); 写入 let b: Vec<char>
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
    (m + n - 2 * dp[n] as usize) as i32 // (映射表 加 元素个数 减 2 乘 DP 表[元素个数] as usize) as i32
}
fn main() {
    assert_eq!(min_distance("sea".into(), "eat".into()), 2);
    assert_eq!(min_distance("leetcode".into(), "etco".into()), 4);
    println!("PASS");
} // 程序入口：跑内嵌自测用例
