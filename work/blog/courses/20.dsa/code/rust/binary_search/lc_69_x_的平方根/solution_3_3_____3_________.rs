// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145299731
// LeetCode 69. x 的平方根 — Rust 版（3 ) 方案3：牛顿迭代）
fn my_sqrt(x: i64) -> i64 {
    // 定义函数/方法 my_sqrt
    if x < 2 {
        return x;
    } // 若 x 小于 2 { return x; }
    let mut r = x; // 把 x; 写入 let mut r
    while r * r > x {
        // while 右指针 乘 右指针 超过 x {
        r = (r + x / r) / 2; // 把 (右指针 加 x 除以 右指针) 除以 2; 写入 右指针
    }
    r // 右指针
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let cases: [(i64, i64); 4] = [(4, 2), (8, 2), (16, 4), (2147395599, 46339)];
    for (x, want) in cases {
        // for (x, want) in cases {
        assert_eq!(my_sqrt(x), want, "x={}", x); // 断言校验
    }
    println!("PASS"); // 全部用例通过，输出 PASS
}
