// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145299731
// LeetCode 69. x 的平方根 — Rust 版（2 ) 方案2：二分（保留 ans））
fn my_sqrt(x: i64) -> i64 {
    // 定义函数/方法 my_sqrt
    let (mut lo, mut hi, mut ans) = (0i64, x, 0i64); // 把 (0i64, x, 0i64); 写入 let (mut lo, mut hi, mut ans)
    while lo <= hi {
        // 把 右边界 { 写入 while lo <
        let m = lo + (hi - lo) / 2; // 把 左边界 加 (右边界 减 左边界) 除以 2 存入 映射表
        if m * m <= x {
            ans = m;
            lo = m + 1;
        } else {
            hi = m - 1;
        }
    }
    ans // 答案
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
