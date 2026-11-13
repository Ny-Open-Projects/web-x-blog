// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107475776
// 计算思维之下楼梯台阶和象棋跳马问题 — Rust 版（方案5）
fn climb_stairs_variants(n: i32) -> i64 {
    // 定义函数/方法 climb_stairs_variants
    // 下楼梯 + 象棋跳马: 每步 1/2 阶 → fib 计数（方案数）
    if n <= 1 {
        return 1;
    } // 若 元素个数 不超过 1 { return 1; }
    let (mut a, mut b) = (1i64, 1i64); // 把 (1i64, 1i64); 写入 let (mut a, mut b)
    for _ in 2..=n {
        let t = a + b;
        a = b;
        b = t;
    } // 逐个取出 2 的元素（_）
    b
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(climb_stairs_variants(10), 89); // 断言校验
    assert_eq!(climb_stairs_variants(1), 1); // 断言校验
    assert_eq!(climb_stairs_variants(2), 2); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
