// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135256754
// LeetCode 76. 最小覆盖子串 — Rust 版（方案3）
use std::collections::HashMap; // 引入依赖
fn min_window(s: &str, t: &str) -> String {
    // 定义函数/方法 min_window
    if s.is_empty() || t.is_empty() {
        return String::new();
    } // 若 字符串 是否为空 或 另一字符串 是否为空 { return String::new(); }
    let sc: Vec<char> = s.chars().collect(); // 把 字符串.chars().collect(); 写入 let sc: Vec<char>
    let mut target: HashMap<char, i32> = HashMap::new(); // 把 HashMap::new(); 写入 let mut target: HashMap<char, i32>
    for c in t.chars() {
        *target.entry(c).or_insert(0) += 1;
    } // 逐个取出 另一字符串 的元素（字符）
    let required = target.len() as i32; // 把 目标值.长度() as i32 存入 required
    let (mut left, mut formed) = (0usize, 0i32); // 把 (0usize, 0i32); 写入 let (mut left, mut formed)
    let mut window: HashMap<char, i32> = HashMap::new(); // 把 HashMap::new(); 写入 let mut window: HashMap<char, i32>
    let (mut min_len, mut min_left) = (usize::MAX, 0usize); // 把 (usize::MAX, 0usize); 写入 let (mut min_len, mut min_left)
    for right in 0..sc.len() {
        // 逐个取出 0 的元素（右边界）
        let c = sc[right]; // 把 sc[右边界] 存入 字符
        *window.entry(c).or_insert(0) += 1;
        if let Some(&need) = target.get(&c) {
            // 若 let Some( 按位与 need) 赋值为 目标值 查找 按位与 字符
            if window[&c] == need {
                formed += 1;
            } // 若 window[ 按位与 字符] 等于 need { formed 累加 1; }
        }
        while formed == required {
            // 把 赋值为 required { 写入 while formed
            if right - left + 1 < min_len {
                // 若 右边界 减 左边界 加 1 小于 min_len
                min_len = right - left + 1; // 把 右边界 减 左边界 加 1; 写入 min_len
                min_left = left; // 把 左边界; 写入 min_left
            }
            let lc = sc[left]; // 把 sc[左边界] 存入 lc
            *window.get_mut(&lc).unwrap() -= 1;
            if let Some(&need) = target.get(&lc) {
                // 若 let Some( 按位与 need) 赋值为 目标值 查找 按位与 lc
                if window[&lc] < need {
                    formed -= 1;
                } // 若 window[ 按位与 lc] 小于 need { formed 累减 1; }
            }
            left += 1; // 左边界累加 1
        }
    }
    if min_len == usize::MAX {
        String::new()
    } else {
        sc[min_left..min_left + min_len].iter().collect()
    }
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(min_window("ADOBECODEBANC", "ABC"), "BANC"); // 断言校验
    assert_eq!(min_window("a", "a"), "a"); // 断言校验
    assert_eq!(min_window("a", "aa"), ""); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
