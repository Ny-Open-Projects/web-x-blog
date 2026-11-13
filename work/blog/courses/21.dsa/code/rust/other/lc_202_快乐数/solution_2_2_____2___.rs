// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135124945
// LeetCode 202. 快乐数 — Rust 版（方案2）
fn bit_square_sum(mut n: i64) -> i64 {
    // 定义函数/方法 bit_square_sum
    let mut s = 0i64; // 把 0i64; 写入 let mut s
    while n > 0 {
        let d = n % 10;
        s += d * d;
        n /= 10;
    }
    s // 字符串
}
fn is_happy(mut n: i64) -> bool {
    // 定义判定函数 is_happy
    use std::collections::HashSet; // 引入依赖
    let mut seen: HashSet<i64> = HashSet::new(); // 把 HashSet::new(); 写入 let mut seen: HashSet<i64>
    while n != 1 && !seen.contains(&n) {
        // 把 1 且 取反 已见集合 是否包含 按位与 元素个数) { 写入 while n !
        seen.insert(n); // 已见集合 插入 元素个数);
        n = bit_square_sum(n); // 把 bit_square_sum(元素个数); 写入 元素个数
    }
    n == 1 // 把 赋值为 1 写入 元素个数
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(bit_square_sum(1), 1); // 断言校验
    assert_eq!(bit_square_sum(19), 82); // 断言校验
    assert_eq!(bit_square_sum(82), 68); // 断言校验
    assert!(is_happy(19)); // 断言校验
    assert!(is_happy(1)); // 断言校验
    assert!(!is_happy(2)); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
