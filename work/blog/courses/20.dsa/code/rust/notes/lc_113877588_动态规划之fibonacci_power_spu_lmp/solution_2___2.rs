// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113877588
// 动态规划之Fibonacci — Rust 版（方案2）
fn fib_memo(n: i32) -> i64 {
    // 定义函数/方法 fib_memo
    // 动态规划笔记: fibonacci 带记忆化 vs 递归
    let mut memo = std::collections::HashMap::new(); // 把 std::collections::HashMap::new(); 写入 let mut memo
    fn go(n: i32, memo: &mut std::collections::HashMap<i32, i64>) -> i64 {
        // 定义函数/方法 go
        if n <= 1 {
            return n as i64;
        } // 若 元素个数 不超过 1 { return 元素个数 as i64; }
        if let Some(&v) = memo.get(&n) {
            return v;
        } // 若 let Some( 按位与 值) 赋值为 记忆化表 查找 按位与 元素个数) { return 值; }
        let v = go(n - 1, memo) + go(n - 2, memo); // 把 go(元素个数 减 1, 记忆化表) 加 go(元素个数 减 2, 记忆化表) 存入 值
        memo.insert(n, v); // 记忆化表 插入 元素个数, 值);
        v
    }
    go(n, &mut memo) // go(元素个数, 按位与 mut 记忆化表)
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(fib_memo(10), 55); // 断言校验
    assert_eq!(fib_memo(20), 6765); // 断言校验
    assert_eq!(fib_memo(0), 0); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
