// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145398097
// LeetCode 2637. 有时间限制的Promise对象 — Rust 版（方案2）
fn promise_with_time_limit(values: &[Option<i32>], t: i32) -> Vec<i32> {
    // 定义函数/方法 promise_with_time_limit
    // TS 语义: 每个 fn resolve(value) 或限时 reject("Time Limit Exceeded")
    // 确定性模拟: Some(v) 按时完成返回 v；None 超时返回 -1
    values
        .iter()
        .map(|&v| if let Some(x) = v { x } else { -1 })
        .collect()
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(
        promise_with_time_limit(&[Some(5), None, Some(9)], 50),
        vec![5, -1, 9]
    ); // 断言校验
    assert_eq!(promise_with_time_limit(&[None], 100), vec![-1]); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
