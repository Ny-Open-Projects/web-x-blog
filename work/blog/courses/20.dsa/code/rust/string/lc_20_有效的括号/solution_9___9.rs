// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133759617
// LeetCode 20. 有效的括号 — Rust 版（方案9）
fn is_valid(s: String) -> bool {
    // 定义判定函数 is_valid
    let mut stack: Vec<char> = Vec::new(); // 把 Vec::new(); 写入 let mut stack: Vec<char>
    for ch in s.chars() {
        // 逐个取出 字符串 的元素（字符）
        match ch {
            // 按情况匹配处理
            ')' => {
                if stack.pop() != Some('(') {
                    return false;
                }
            }
            ']' => {
                if stack.pop() != Some('[') {
                    return false;
                }
            }
            '}' => {
                if stack.pop() != Some('{') {
                    return false;
                }
            }
            _ => stack.push(ch),
        }
    }
    stack.is_empty() // 栈 是否为空
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let tests = ["(", "()", "()[]{}", "(]", "([)]", "abc"]; // 把 [「(」, 「(」, 「(」, 「(」, 「(」, 「(」] 存入 tests
    let want = [false, true, true, false, false, false]; // 把 [false, true, true, false, false, false] 存入 want
    for (i, t) in tests.iter().enumerate() {
        // for (下标 i, 另一字符串) in tests.iter().enumerate() {
        assert_eq!(is_valid(t.to_string()), want[i], "case {}", i); // 断言校验
    }
    println!("PASS"); // 全部用例通过，输出 PASS
}
