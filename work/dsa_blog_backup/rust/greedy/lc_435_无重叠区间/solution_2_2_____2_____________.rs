// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135941089
// LeetCode 435. 无重叠区间 — Rust 版（方案2）
fn erase_overlap_intervals(intervals: Vec<Vec<i32>>) -> i32 {
    // 定义函数/方法 erase_overlap_intervals
    if intervals.is_empty() {
        return 0;
    } // 若 intervals 是否为空 { return 0; }
    let mut arr = intervals; // 把 intervals; 写入 let mut arr
    arr.sort_by_key(|x| x[1]); // 数组.sort_by_key( 按位或 x 按位或 x[1]);
    let mut count = 1; // 把 1; 写入 let mut count
    let mut end = arr[0][1]; // 把 数组[0][1]; 写入 let mut end
    for iv in arr.iter().skip(1) {
        // 逐个取出 数组 的元素（iv）
        if iv[0] >= end {
            count += 1;
            end = iv[1];
        } // 若 iv[0] 不低于 终点 { 计数 累加 1; 终点 赋值为 iv[1]; }
    }
    arr.len() as i32 - count // 数组.长度() as i32 减 计数
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(
        erase_overlap_intervals(vec![vec![1, 2], vec![2, 3], vec![3, 4], vec![1, 3]]),
        1
    ); // 断言校验
    assert_eq!(erase_overlap_intervals(vec![]), 0); // 断言校验
    assert_eq!(
        erase_overlap_intervals(vec![vec![1, 2], vec![1, 2], vec![1, 2]]),
        2
    ); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
