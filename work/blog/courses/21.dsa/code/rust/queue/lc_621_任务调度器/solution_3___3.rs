// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130482987
// LeetCode 621. 任务调度器 — Rust 版

// 方案3（贪心模拟，每轮取剩余次数最多的 n+1 个，最后一轮只计实际执行数）
use std::collections::HashMap; // 引入依赖

fn least_interval(tasks: &[char], n: i32) -> i32 {
    // 定义函数/方法 least_interval
    let mut count: HashMap<char, i32> = HashMap::new(); // 把 HashMap::new(); 写入 let mut count: HashMap<char, i32>
    for &t in tasks {
        // for 按位与 另一字符串 in tasks {
        *count.entry(t).or_insert(0) += 1;
    }
    let mut cnt: Vec<i32> = count.values().cloned().collect(); // 把 计数.values().cloned().collect(); 写入 let mut cnt: Vec<i32>
    let mut time = 0; // 把 0; 写入 let mut time
    while !cnt.is_empty() {
        // while 取反 计数 是否为空 {
        cnt.sort_by(|a, b| b.cmp(a)); // 计数.sort_by( 按位或 数组, b 按位或 b.cmp(数组));
        let mut used = 0; // 把 0; 写入 let mut used
        let take = std::cmp::min(n + 1, cnt.len() as i32) as usize; // 把 std::cmp::取较小值 元素个数 加 1, 计数.长度() as i32) as usize 存入 take
        for i in 0..take {
            // 逐个取出 0 的元素（下标 i）
            if cnt[i] > 0 {
                // 若 计数[下标 i] 超过 0
                cnt[i] -= 1; // cnt[i]累减 1
                used += 1; // 已用标记累加 1
            }
        }
        cnt.retain(|&c| c > 0); // 计数.retain( 按位或 按位与 字符 按位或 字符 超过 0);
        time += if !cnt.is_empty() { n + 1 } else { used }; // time累加 if 取反 计数 是否为空 { 元素个数 加 1 } else { 已用标记 }
    }
    time // time
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
