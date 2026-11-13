// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/137060905
// LeetCode 451. 根据字符出现频率排序 — Rust 版（方案1）
use std::collections::HashMap; // 引入依赖
fn frequency_sort(s: &str) -> String {
    // 定义函数/方法 frequency_sort
    let mut counts: HashMap<char, i64> = HashMap::new(); // 把 HashMap::new(); 写入 let mut counts: HashMap<char, i64>
    let mut first_idx: HashMap<char, usize> = HashMap::new(); // 把 HashMap::new(); 写入 let mut first_idx: HashMap<char, usize>
    for (i, c) in s.chars().enumerate() {
        // for (下标 i, 字符) in 字符串.chars().enumerate() {
        *counts.entry(c).or_insert(0) += 1;
        first_idx.entry(c).or_insert(i); // first_idx.entry(字符).or_insert(下标 i);
    }
    let mut items: Vec<(char, i64, usize)> = counts
        .iter()
        .map(|(&c, &n)| (c, n, first_idx[&c]))
        .collect();
    items.sort_by(|a, b| b.1.cmp(&a.1).then(a.2.cmp(&b.2)));
    items
        .iter()
        .map(|&(c, n, _)| std::iter::repeat(c).take(n as usize).collect::<String>())
        .collect()
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(frequency_sort("tree"), "eetr"); // 断言校验
    assert_eq!(frequency_sort(""), ""); // 断言校验
    assert_eq!(frequency_sort("cccaaa"), "cccaaa"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
