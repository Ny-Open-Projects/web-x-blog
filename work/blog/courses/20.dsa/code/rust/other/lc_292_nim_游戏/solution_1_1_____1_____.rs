// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135424151
// LeetCode 292. Nim游戏 — Rust 版（方案1）
fn can_win_nim(n: i64) -> bool {
    n % 4 != 0
} // 定义函数/方法 can_win_nim
fn main() {
    // 程序入口：跑内嵌自测用例
    assert!(!can_win_nim(4)); // 断言校验
    assert!(can_win_nim(1)); // 断言校验
    assert!(can_win_nim(2)); // 断言校验
    assert!(!can_win_nim(8)); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
