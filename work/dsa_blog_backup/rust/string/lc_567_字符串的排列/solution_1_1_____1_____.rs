// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135917076
// LeetCode 567. 字符串的排列 — Rust 版（方案1）
fn check_inclusion(s1: String, s2: String) -> bool {
    // 定义判定函数 check_inclusion
    let (a, b) = (s1.as_bytes(), s2.as_bytes()); // 把 (s1.as_bytes(), s2.as_bytes()); 写入 let (a, b)
    let (m, n) = (a.len(), b.len()); // 把 (数组.长度(), b.长度()); 写入 let (m, n)
    if m > n {
        return false;
    } // 若 映射表 超过 元素个数 { return false; }
    let mut s1c = [0i32; 26]; // 把 [0i32; 26]; 写入 let mut s1c
    let mut s2c = [0i32; 26]; // 把 [0i32; 26]; 写入 let mut s2c
    for i in 0..m {
        // 逐个取出 0 的元素（下标 i）
        s1c[(a[i] - b'a') as usize] += 1; // 把 1; 写入 s1c[(a[i] - b'a') as usize] +
        s2c[(b[i] - b'a') as usize] += 1; // 把 1; 写入 s2c[(b[i] - b'a') as usize] +
    }
    if s1c == s2c {
        return true;
    } // 若 s1c 等于 s2c { return true; }
    for i in m..n {
        // 逐个取出 映射表 的元素（下标 i）
        s2c[(b[i] - b'a') as usize] += 1; // 把 1; 写入 s2c[(b[i] - b'a') as usize] +
        s2c[(b[i - m] - b'a') as usize] -= 1; // 把 1; 写入 s2c[(b[i - m] - b'a') as usize] -
        if s1c == s2c {
            return true;
        } // 若 s1c 等于 s2c { return true; }
    }
    false // false
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert!(check_inclusion("ab".into(), "eidbaooo".into())); // 断言校验
    assert!(!check_inclusion("ab".into(), "eidboaoo".into())); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
