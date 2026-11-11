// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135154838
// LeetCode 242. 有效的字母异位词 — Rust 版（方案2）
fn is_anagram(s: &str, t: &str) -> bool {
    // 定义判定函数 is_anagram
    if s.len() != t.len() {
        return false;
    } // 若 字符串.长度() 不等于 另一字符串.长度() { return false; }
    let mut a: Vec<char> = s.chars().collect(); // 把 字符串.chars().collect(); 写入 let mut a: Vec<char>
    let mut b: Vec<char> = t.chars().collect(); // 把 另一字符串.chars().collect(); 写入 let mut b: Vec<char>
    a.sort(); // 排序
    b.sort(); // 排序
    a == b // 把 赋值为 b 写入 数组
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert!(is_anagram("anagram", "nagaram")); // 断言校验
    assert!(!is_anagram("rat", "car")); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
