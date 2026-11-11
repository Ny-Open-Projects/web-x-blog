// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130510175
// LeetCode 509. 斐波那契数 — Rust 版（方案9）
fn fib(n: i32) -> i32 {
    if n < 2 {
        return n;
    }
    let (mut a, mut b) = (0, 1);
    for _ in 2..=n {
        let t = a + b;
        a = b;
        b = t;
    }
    b
} // 定义函数/方法 fib
fn main() {
    assert_eq!(fib(2), 1);
    assert_eq!(fib(3), 2);
    assert_eq!(fib(4), 3);
    assert_eq!(fib(10), 55);
    println!("PASS");
} // 程序入口：跑内嵌自测用例
