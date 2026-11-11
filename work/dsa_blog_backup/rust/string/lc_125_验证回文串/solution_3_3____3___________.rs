// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130778527
// LeetCode 125. 验证回文串 — Rust 版（方案3）
fn is_palindrome(s: String) -> bool {
    // 定义判定函数 is_palindrome
    let f: Vec<char> = s
        .chars()
        .filter(|c| c.is_ascii_alphanumeric())
        .map(|c| c.to_ascii_lowercase())
        .collect();
    let (mut i, mut j) = (0usize, f.len()); // 把 (0usize, f.长度()); 写入 let (mut i, mut j)
    if j == 0 {
        return true;
    } // 若 下标 j 等于 0 { return true; }
    j -= 1; // 下标 j累减 1
    while i < j {
        // while 下标 i 小于 下标 j {
        if f[i] != f[j] {
            return false;
        } // 若 f[下标 i] 不等于 f[下标 j] { return false; }
        i += 1; // 下标 i累加 1
        if j == 0 {
            break;
        } // 若 下标 j 等于 0 { break; }
        j -= 1; // 下标 j累减 1
    }
    true // true
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert!(is_palindrome("A man, a plan, a canal: Panama".to_string())); // 断言校验
    assert!(!is_palindrome("race a car".to_string())); // 断言校验
    assert!(is_palindrome(" ".to_string())); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
