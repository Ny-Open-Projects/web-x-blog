// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130846022
// LeetCode 151. 反转字符串中的单词 — Rust 版（方案3）
fn reverse_words(s: String) -> String {
    // 定义函数/方法 reverse_words
    s.split_whitespace().rev().collect::<Vec<_>>().join(" ") // 拼接为字符串
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(reverse_words("the sky is blue".into()), "blue is sky the"); // 断言校验
    assert_eq!(reverse_words("  hello world  ".into()), "world hello"); // 断言校验
    assert_eq!(reverse_words("a good   example".into()), "example good a"); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
