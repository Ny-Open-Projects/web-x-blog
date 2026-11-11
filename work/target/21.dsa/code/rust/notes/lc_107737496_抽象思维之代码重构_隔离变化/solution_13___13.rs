// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — Rust 版（方案13：微型正则匹配 match/matchhere/matchstar）
fn matchhere(re: &str, text: &str) -> bool {
    // 定义函数/方法 matchhere
    let rb = re.as_bytes(); // 把 re.as_bytes() 存入 rb
    let tb = text.as_bytes(); // 把 text.as_bytes() 存入 tb
    if re.is_empty() {
        // 若 re.is_empty(
        return true; // 返回 true
    }
    if rb.len() >= 2 && rb[1] == b'*' {
        // 若 rb.长度() 不低于 2 且 rb[1] 等于 b' 乘 '
        return matchstar(rb[0], &re[2..], text); // 返回 matchstar(rb[0], 按位与 re[2..], text)
    }
    if rb[0] == b'$' && rb.len() == 1 {
        // 若 rb[0] 等于 b'$' 且 rb.长度() 等于 1
        return text.is_empty(); // 返回 text 是否为空
    }
    if !tb.is_empty() && (rb[0] == b'.' || rb[0] == tb[0]) {
        // 若 取反 tb 是否为空 且 (rb[0] 等于 b'.' 或 rb[0] 等于 tb[0]
        return matchhere(&re[1..], &text[1..]); // 返回 matchhere( 按位与 re[1..], 按位与 text[1..])
    }
    false // false
}

fn matchstar(c: u8, re: &str, text: &str) -> bool {
    // 定义函数/方法 matchstar
    let tb = text.as_bytes(); // 把 text.as_bytes() 存入 tb
    let mut i = 0usize; // 把 0usize; 写入 let mut i
    loop {
        // loop {
        if matchhere(re, &text[i..]) {
            // 定义函数/方法 matchhere
            return true; // 返回 true
        }
        if i >= tb.len() {
            // 若 下标 i 不低于 tb.长度(
            break; // 跳出循环
        }
        if tb[i] != c && c != b'.' {
            // 若 tb[下标 i] 不等于 字符 且 字符 不等于 b'.'
            break; // 跳出循环
        }
        i += 1; // 下标 i累加 1
    }
    false // false
}

fn match_re(re: &str, text: &str) -> bool {
    // 定义函数/方法 match_re
    if !re.is_empty() && re.as_bytes()[0] == b'^' {
        // 若 取反 re 是否为空 且 re.as_bytes()[0] 等于 b' 按位异或 '
        return matchhere(&re[1..], text); // 返回 matchhere( 按位与 re[1..], text)
    }
    let mut i = 0usize; // 把 0usize; 写入 let mut i
    loop {
        // loop {
        if matchhere(re, &text[i..]) {
            // 定义函数/方法 matchhere
            return true; // 返回 true
        }
        if i >= text.len() {
            // 若 下标 i 不低于 text.长度(
            break; // 跳出循环
        }
        i += 1; // 下标 i累加 1
    }
    false // false
}

fn main() {
    // 程序入口：跑内嵌自测用例
    assert!(match_re("abc", "xxabcxx"), "m1"); // 断言校验
    assert!(match_re("a.c", "axc"), "m2"); // 断言校验
    assert!(match_re("a*", "aaaa"), "m3"); // 断言校验
    assert!(!match_re("^a", "ba"), "m4"); // 断言校验
    assert!(match_re("c$", "abc"), "m5"); // 断言校验
    assert!(match_re("a.*c", "aXYZc"), "m6"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
