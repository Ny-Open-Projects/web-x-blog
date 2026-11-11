// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135359346
// LeetCode 326. 3的幂 — Rust 版（方案1）
fn is_power_of_three(mut n: i64) -> bool {
    // 定义判定函数 is_power_of_three
    while n != 0 && n % 3 == 0 {
        n /= 3;
    } // 把 0 且 元素个数 对…取模 3 等于 0 { 元素个数 除以 3; } 写入 while n !
    n == 1 // 把 赋值为 1 写入 元素个数
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert!(is_power_of_three(27)); // 断言校验
    assert!(!is_power_of_three(0)); // 断言校验
    assert!(is_power_of_three(9)); // 断言校验
    assert!(!is_power_of_three(-1)); // 断言校验
    assert!(is_power_of_three(1)); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
