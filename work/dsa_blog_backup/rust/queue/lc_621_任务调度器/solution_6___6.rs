// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130482987
// LeetCode 621. 任务调度器 — Rust 版

// 方案6（公式法另一写法：Counter 值列表 + count(freq)）
use std::collections::HashMap; // 引入依赖

fn least_interval(tasks: &[char], n: i32) -> i32 {
    // 定义函数/方法 least_interval
    let mut cnt: HashMap<char, i32> = HashMap::new(); // 把 HashMap::new(); 写入 let mut cnt: HashMap<char, i32>
    for &t in tasks {
        // for 按位与 另一字符串 in tasks {
        *cnt.entry(t).or_insert(0) += 1;
    }
    let list: Vec<i32> = cnt.values().cloned().collect(); // 把 计数.values().cloned().collect(); 写入 let list: Vec<i32>
    let mut freq = 0; // 把 0; 写入 let mut freq
    for &v in list.iter() {
        // for 按位与 值 in 列表.iter() {
        if v > freq {
            // 若 值 超过 频次表
            freq = v; // 把 值; 写入 频次表
        }
    }
    let mut same = 0; // 把 0; 写入 let mut same
    for &v in list.iter() {
        // for 按位与 值 in 列表.iter() {
        if v == freq {
            // 若 值 等于 频次表
            same += 1; // same累加 1
        }
    }
    std::cmp::max((freq - 1) * (n + 1) + same, tasks.len() as i32)
}

fn main() {
    // 程序入口：跑内嵌自测用例
    // 与 TS 事实源内嵌用例一致
    let cases: Vec<(Vec<char>, i32, i32)> = vec![
        (vec!['A', 'A', 'A', 'B', 'B', 'B'], 2, 8),
        (vec!['A', 'A', 'A', 'A'], 2, 10),
        (vec!['A', 'B', 'C', 'D'], 0, 4),
    ];
    for (tasks, n, want) in cases {
        // for (tasks, 元素个数, want) in cases {
        let got = least_interval(&tasks, n); // 把 least_interval( 按位与 tasks, 元素个数) 存入 got
        assert!(
            got == want,
            "FAIL least_interval({:?},{})={} want {}",
            tasks,
            n,
            got,
            want
        ); // 断言校验
    }
    println!("PASS"); // 全部用例通过，输出 PASS
}
