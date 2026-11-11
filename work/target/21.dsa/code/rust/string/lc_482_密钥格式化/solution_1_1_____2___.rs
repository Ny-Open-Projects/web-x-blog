// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/138290964
// LeetCode 482. 密钥格式化 — Rust 版（方案1）
fn license_key_formatting(s: String, k: i32) -> String {
    // 定义函数/方法 license_key_formatting
    let cleaned: Vec<u8> = s
        .bytes()
        .filter(|&c| c != b'-')
        .map(|c| c.to_ascii_uppercase())
        .collect();
    let mut out: Vec<u8> = Vec::new(); // 把 Vec::new(); 写入 let mut out: Vec<u8>
    let n = cleaned.len(); // 把 cleaned.长度() 存入 元素个数
    let k = k as usize; // 把 下标 k as usize 存入 下标 k
    if n == 0 {
        return String::new();
    } // 若 元素个数 等于 0 { return String::new(); }
    let first = n % k; // 把 元素个数 对…取模 下标 k 存入 first
    let mut idx = 0usize; // 把 0usize; 写入 let mut idx
    if first > 0 {
        // 若 first 超过 0
        for _ in 0..first {
            out.push(cleaned[idx]);
            idx += 1;
        } // 逐个取出 0 的元素（_）
        if idx < n {
            out.push(b'-');
        } // 若 idx 小于 元素个数 { out 追加 b' 减 '); }
    }
    while idx < n {
        // while idx 小于 元素个数 {
        for _ in 0..k {
            out.push(cleaned[idx]);
            idx += 1;
        } // 逐个取出 0 的元素（_）
        if idx < n {
            out.push(b'-');
        } // 若 idx 小于 元素个数 { out 追加 b' 减 '); }
    }
    String::from_utf8(out).unwrap() // String::from_utf8(out).unwrap()
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(license_key_formatting("5F3Z-2e-9-w".into(), 4), "5F3Z-2E9W"); // 断言校验
    assert_eq!(license_key_formatting("2-5g-3-J".into(), 2), "2-5G-3J"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
