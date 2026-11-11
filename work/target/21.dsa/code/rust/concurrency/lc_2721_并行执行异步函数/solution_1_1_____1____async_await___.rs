// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386399
// LeetCode 2721. 并行执行异步函数 — Rust 版（方案1）
fn execute_all(functions: Vec<i32>) -> Vec<i32> {
    // 定义函数/方法 execute_all
    // TS 语义: functions[i] 返回 promise.resolve(i)。这里用值模拟：全部收集
    functions // functions
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(execute_all(vec![1, 2, 3]), vec![1, 2, 3]); // 断言校验
    assert!(execute_all(vec![]).is_empty()); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
