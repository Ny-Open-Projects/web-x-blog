// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145565975
// LeetCode 557. 反转字符串中的单词III — Rust 版（方案9）
fn reverse_words(s: String) -> String {
    // 定义函数/方法 reverse_words
    s.split(' ')
        .map(|w| w.chars().rev().collect::<String>())
        .collect::<Vec<_>>()
        .join(" ") // 拼接为字符串
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(
        reverse_words("Let's take LeetCode contest".into()),
        "s'teL ekat edoCteeL tsetnoc"
    ); // 断言校验
    assert_eq!(reverse_words("God Ding".into()), "doG gniD"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
