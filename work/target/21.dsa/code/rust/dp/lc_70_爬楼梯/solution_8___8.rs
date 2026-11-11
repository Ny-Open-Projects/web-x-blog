// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130506068
// LeetCode 70. 爬楼梯 — Rust 版（方案8）
fn climb_stairs(n: i32) -> i32 {
    if n <= 2 {
        return n;
    }
    let (mut a, mut b) = (1, 2);
    for _ in 3..=n {
        let t = a + b;
        a = b;
        b = t;
    }
    b
} // 定义函数/方法 climb_stairs
fn main() {
    assert_eq!(climb_stairs(2), 2);
    assert_eq!(climb_stairs(3), 3);
    assert_eq!(climb_stairs(10), 89);
    println!("PASS");
} // 程序入口：跑内嵌自测用例
