// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/138481618
// LeetCode 2042. 检查句子中的数字是否递增 — Rust 版（方案2）
fn are_numbers_ascending(s: String) -> bool {
    // 定义函数/方法 are_numbers_ascending
    let mut prev: i64 = 0; // 把 0; 写入 let mut prev: i64
    for tok in s.split_whitespace() {
        // 逐个取出 字符串 的元素（tok）
        if tok
            .chars()
            .next()
            .map(|c| c.is_ascii_digit())
            .unwrap_or(false)
        {
            let num: i64 = tok.parse().unwrap_or(0); // 把 tok.parse().unwrap_or(0); 写入 let num: i64
            if num <= prev {
                return false;
            } // 若 num 不超过 前一个 { return false; }
            prev = num; // 把 num; 写入 前一个
        }
    }
    true // true
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert!(are_numbers_ascending(
        "1 box has 3 blue 4 red 6 green and 12 yellow marbles".to_string()
    )); // 断言校验
    assert!(!are_numbers_ascending("hello world 5 x 5".to_string())); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
