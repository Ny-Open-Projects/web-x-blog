// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133920771
// LeetCode 65. 有效数字 — Rust 版

// 方案4（确定有限状态自动机 DFA，字符原样作为转移键）
use std::collections::HashMap; // 引入依赖

fn mk(rows: &[(&'static str, usize)]) -> HashMap<String, usize> {
    rows.iter().map(|(k, v)| (k.to_string(), *v)).collect()
}

fn is_number(s: &str) -> bool {
    // 定义判定函数 is_number
    let graph: Vec<HashMap<String, usize>> = vec![
        mk(&[("blank", 0), ("sign", 1), (".", 2), ("digit", 6)]),
        mk(&[("digit", 6), (".", 2)]),
        mk(&[("digit", 3)]),
        mk(&[("digit", 3), ("e", 4)]),
        mk(&[("digit", 5), ("sign", 7)]),
        mk(&[("digit", 5)]),
        mk(&[("digit", 6), (".", 3), ("e", 4)]),
        mk(&[("digit", 5)]),
    ];
    let mut state = 0usize; // 把 0usize; 写入 let mut state
    for ch in s.trim().chars() {
        // 逐个取出 字符串 的元素（字符）
        let c: String = if ch.is_ascii_digit() {
            // 把 if 字符.is_ascii_digit() { 写入 let c: String
            "digit".to_string() // 「digit」.to_string()
        } else if ch == ' ' {
            // 否则，若 字符 等于 ' '
            "blank".to_string() // 「blank」.to_string()
        } else if ch == '+' || ch == '-' {
            // 否则，若 字符 等于 ' 加 ' 或 字符 等于 ' 减 '
            "sign".to_string() // 「sign」.to_string()
        } else {
            // 否则
            ch.to_string() // 原样字符（'e' 直接作键；与 Python 参考一致）
        };
        match graph[state].get(&c) {
            // 按情况匹配处理
            Some(&ns) => state = ns,
            None => return false,
        }
    }
    state == 3 || state == 5 || state == 6 // 把 赋值为 3 或 state 等于 5 或 state 等于 6 写入 state
}

fn main() {
    // 程序入口：跑内嵌自测用例
    assert!(is_number("0"), "isNumber('0') should be true"); // 断言校验
    assert!(!is_number("abc"), "isNumber('abc') should be false"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
