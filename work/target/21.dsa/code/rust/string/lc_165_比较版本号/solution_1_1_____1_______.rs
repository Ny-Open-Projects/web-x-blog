// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135004886
// LeetCode 165. 比较版本号 — Rust 版（方案1）
fn compare_version(v1: String, v2: String) -> i32 {
    // 定义函数/方法 compare_version
    let p1: Vec<i64> = v1
        .split('.')
        .map(|x| x.parse::<i64>().unwrap_or(0))
        .collect();
    let p2: Vec<i64> = v2
        .split('.')
        .map(|x| x.parse::<i64>().unwrap_or(0))
        .collect();
    let n = p1.len().max(p2.len()); // 把 p1.长度().取较大值 p2.长度()) 存入 元素个数
    for i in 0..n {
        // 逐个取出 0 的元素（下标 i）
        let a = if i < p1.len() { p1[i] } else { 0 }; // 把 if 下标 i 小于 p1.长度() { p1[下标 i] } else { 0 } 存入 数组
        let b = if i < p2.len() { p2[i] } else { 0 }; // 把 if 下标 i 小于 p2.长度() { p2[下标 i] } else { 0 } 存入 b
        if a < b {
            return -1;
        } // 若 数组 小于 b { return 减 1; }
        if a > b {
            return 1;
        } // 若 数组 超过 b { return 1; }
    }
    0
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(compare_version("1.01".into(), "1.001".into()), 0); // 断言校验
    assert_eq!(compare_version("1.0".into(), "1.0.0".into()), 0); // 断言校验
    assert_eq!(compare_version("0.1".into(), "1.1".into()), -1); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
