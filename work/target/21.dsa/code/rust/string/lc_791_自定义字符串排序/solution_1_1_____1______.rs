// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136838836
// LeetCode 791. 自定义字符串排序 — Rust 版（方案1）
fn custom_sort_string(order: String, s: String) -> String {
    // 定义函数/方法 custom_sort_string
    let mut count = [0usize; 26]; // 把 [0usize; 26]; 写入 let mut count
    for b in s.bytes() {
        count[(b - b'a') as usize] += 1;
    } // 逐个取出 字符串 的元素（b）
    let mut out = String::new(); // 把 String::new(); 写入 let mut out
    for b in order.bytes() {
        // 逐个取出 order 的元素（b）
        let idx = (b - b'a') as usize; // 把 (b 减 b'数组') as usize 存入 idx
        for _ in 0..count[idx] {
            out.push(b as char);
        } // 逐个取出 0 的元素（_）
        count[idx] = 0; // 把 0; 写入 count[idx]
    }
    for (i, &c) in count.iter().enumerate() {
        // for (下标 i, 按位与 字符) in 计数.iter().enumerate() {
        for _ in 0..c {
            out.push((b'a' + i as u8) as char);
        } // 逐个取出 0 的元素（_）
    }
    out // out
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(custom_sort_string("cba".into(), "abcd".into()), "cbad"); // 断言校验
    assert_eq!(custom_sort_string("bcafg".into(), "abcd".into()), "bcad"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
