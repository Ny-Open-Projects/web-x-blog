// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107573690
// 抽象思维之对比算法 发现共性 — Rust 版（方案2）
fn climb_stairs_refactored(n: i32) -> i64 {
    // 定义函数/方法 climb_stairs_refactored
    // 变体：每次 1/2/3 阶（对比算法 共性提炼）
    if n < 0 {
        return 0;
    } // 若 元素个数 小于 0 { return 0; }
    if n == 0 {
        return 1;
    } // 若 元素个数 等于 0 { return 1; }
    let mut dp = vec![0i64; (n + 1) as usize]; // 把 vec取反 [0i64; (元素个数 加 1) as usize]; 写入 let mut dp
    dp[0] = 1; // 把 1; 写入 dp[0]
    for i in 1..=n as usize {
        // 逐个取出 1 的元素（下标 i）
        dp[i] = dp[i - 1]; // 把 DP 表[下标 i 减 1]; 写入 dp[i]
        if i >= 2 {
            dp[i] += dp[i - 2];
        } // 若 下标 i 不低于 2 { DP 表[下标 i] 累加 DP 表[下标 i 减 2]; }
        if i >= 3 {
            dp[i] += dp[i - 3];
        } // 若 下标 i 不低于 3 { DP 表[下标 i] 累加 DP 表[下标 i 减 3]; }
    }
    dp[n as usize] // DP 表[元素个数 as usize]
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(climb_stairs_refactored(10), 274); // 断言校验
    assert_eq!(climb_stairs_refactored(3), 4); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
