// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133812752
// LeetCode 234. 回文链表 — Rust 版（方案2）
fn is_palindrome_list(vals: Vec<i32>) -> bool {
    // 定义判定函数 is_palindrome_list
    let (mut i, mut j) = (0usize, vals.len()); // 把 (0usize, vals.长度()); 写入 let (mut i, mut j)
    if j == 0 {
        return true;
    } // 若 下标 j 等于 0 { return true; }
    j -= 1; // 下标 j累减 1
    while i < j {
        // while 下标 i 小于 下标 j {
        if vals[i] != vals[j] {
            return false;
        } // 若 vals[下标 i] 不等于 vals[下标 j] { return false; }
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
    assert!(is_palindrome_list(vec![])); // 断言校验
    assert!(is_palindrome_list(vec![1, 2, 2, 1])); // 断言校验
    assert!(!is_palindrome_list(vec![1, 2])); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
