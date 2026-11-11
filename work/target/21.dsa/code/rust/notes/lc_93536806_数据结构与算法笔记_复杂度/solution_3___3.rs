// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
// 数据结构与算法笔记: 复杂度 — Rust 版（方案3）
fn func_calls(n: i32) -> i64 {
    // 定义函数/方法 func_calls
    // func(n) = func(n-1) + func(n-1)，总调用次数 = 2^n - 1（指数复杂度示例）
    if n <= 1 {
        return 1;
    } // 若 元素个数 不超过 1 { return 1; }
    2 * func_calls(n - 1) // 2 乘 func_calls(元素个数 减 1)
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(func_calls(1), 1); // 断言校验
    assert_eq!(func_calls(2), 2); // 断言校验
    assert_eq!(func_calls(5), 16); // 断言校验
    assert_eq!(func_calls(10), 512); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
