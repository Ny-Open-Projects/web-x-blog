// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135004189
// LeetCode 3. 无重复字符的最长子串 — Rust 版（方案6）
use std::collections::HashSet; // 引入依赖
fn length_of_longest_substring(s: &str) -> i32 {
    // 定义函数/方法 length_of_longest_substring
    let chars: Vec<char> = s.chars().collect(); // 把 字符串.chars().collect(); 写入 let chars: Vec<char>
    let mut set: HashSet<char> = HashSet::new(); // 把 HashSet::new(); 写入 let mut set: HashSet<char>
    let (mut left, mut max_len) = (0usize, 0i32); // 把 (0usize, 0i32); 写入 let (mut left, mut max_len)
    for right in 0..chars.len() {
        // 逐个取出 0 的元素（右边界）
        while set.contains(&chars[right]) {
            // while set 是否包含 按位与 chars[右边界]) {
            set.remove(&chars[left]); // set 弹出 按位与 chars[左边界]);
            left += 1; // 左边界累加 1
        }
        set.insert(chars[right]); // set 插入 chars[右边界]);
        let len = (right - left + 1) as i32; // 把 (右边界 减 左边界 加 1) as i32 存入 长度
        if len > max_len {
            max_len = len;
        } // 若 长度 超过 max_len { max_len 赋值为 长度; }
    }
    max_len // max_len
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(length_of_longest_substring("abcabcbb"), 3); // 断言校验
    assert_eq!(length_of_longest_substring("bbbbb"), 1); // 断言校验
    assert_eq!(length_of_longest_substring("pwwkew"), 3); // 断言校验
    assert_eq!(length_of_longest_substring(""), 0); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
