// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133920771
// LeetCode 65. 有效数字 — Rust 版

// 方案2（线性扫描）
fn is_number(s: &str) -> bool {
    // 定义判定函数 is_number
    let t = s.trim(); // 把 字符串.trim() 存入 另一字符串
    if t.is_empty() {
        // 若 另一字符串.is_empty(
        return false; // 返回 false
    }
    let mut has_dot = false; // 把 false; 写入 let mut has_dot
    let mut has_e = false; // 把 false; 写入 let mut has_e
    let mut has_digit = false; // 把 false; 写入 let mut has_digit
    let chars: Vec<char> = t.chars().collect(); // 把 另一字符串.chars().collect(); 写入 let chars: Vec<char>
    for i in 0..chars.len() {
        // 逐个取出 0 的元素（下标 i）
        let c = chars[i]; // 把 chars[下标 i] 存入 字符
        if c == '.' {
            // 若 字符 等于 '.'
            if has_dot || has_e {
                // 若 has_dot 或 has_e
                return false; // 返回 false
            }
            has_dot = true; // 把 true; 写入 has_dot
        } else if c == 'e' || c == 'E' {
            // 否则，若 字符 等于 'e' 或 字符 等于 'E'
            if has_e || !has_digit {
                // 若 has_e 或 取反 has_digit
                return false; // 返回 false
            }
            has_e = true; // 把 true; 写入 has_e
            has_digit = false; // 把 false; 写入 has_digit
        } else if c == '+' || c == '-' {
            // 否则，若 字符 等于 ' 加 ' 或 字符 等于 ' 减 '
            if i > 0 && chars[i - 1] != 'e' && chars[i - 1] != 'E' {
                return false; // 返回 false
            }
        } else if c.is_ascii_digit() {
            // 否则，若 字符.is_ascii_digit(
            has_digit = true; // 把 true; 写入 has_digit
        } else {
            // 否则
            return false; // 返回 false
        }
    }
    has_digit // has_digit
}

fn main() {
    // 程序入口：跑内嵌自测用例
    assert!(!is_number("abc"), "isNumber('abc') should be false"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
