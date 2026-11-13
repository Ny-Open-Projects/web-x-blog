// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145299731
// LeetCode 69. x 的平方根 — Rust 版（4 ) 方案4：二分（返回 hi））
fn my_sqrt(x: i64) -> i64 {
    // 定义函数/方法 my_sqrt
    let (mut lo, mut hi) = (1i64, x); // 把 (1i64, x); 写入 let (mut lo, mut hi)
    while lo <= hi {
        // 把 右边界 { 写入 while lo <
        let m = lo + (hi - lo) / 2; // 把 左边界 加 (右边界 减 左边界) 除以 2 存入 映射表
        if m * m == x {
            return m;
        }
        // 若 映射表 乘 映射表 等于 x { return 映射表; }
        else if m * m < x {
            lo = m + 1;
        } else {
            hi = m - 1;
        }
    }
    hi // 右边界
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
