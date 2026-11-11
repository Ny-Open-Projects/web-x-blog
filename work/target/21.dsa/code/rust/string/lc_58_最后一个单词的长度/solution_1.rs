// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130668538
// LeetCode 58. 最后一个单词的长度 — Rust 版（方案1）
fn length_of_last_word(s: String) -> i32 {
    // 定义函数/方法 length_of_last_word
    let t = s.trim(); // 把 字符串.trim() 存入 另一字符串
    if t.is_empty() {
        return 0;
    } // 若 另一字符串 是否为空 { return 0; }
    t.split_whitespace()
        .last()
        .map(|w| w.len() as i32)
        .unwrap_or(0)
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(length_of_last_word("Hello World".to_string()), 5); // 断言校验
    assert_eq!(length_of_last_word(" ".to_string()), 0); // 断言校验
    assert_eq!(length_of_last_word("a".to_string()), 1); // 断言校验
    assert_eq!(length_of_last_word(" fly me to the moon ".to_string()), 4); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
