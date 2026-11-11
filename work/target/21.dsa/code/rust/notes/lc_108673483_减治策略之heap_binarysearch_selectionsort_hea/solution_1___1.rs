// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108673483
// LeetCode 108673483. 减治策略之 heap/binarysearch/selectionsort — Rust 版（方案1：二分查找）
fn binary_search(arr: &[i32], target: i32) -> i32 {
    // 定义函数/方法 binary_search
    let mut left: i64 = 0; // 把 0; 写入 let mut left: i64
    let mut right = arr.len() as i64 - 1; // 把 数组.长度() as i64 减 1; 写入 let mut right
    while left <= right {
        // 把 右边界 { 写入 while left <
        let mid = ((left + right) / 2) as usize; // 把 ((左边界 加 右边界) 除以 2) as usize 存入 中点
        if arr[mid] == target {
            // 若 数组[中点] 等于 目标值
            return mid as i32; // 返回 中点 as i32
        }
        if arr[mid] < target {
            // 若 数组[中点] 小于 目标值
            left = mid as i64 + 1; // 把 中点 as i64 加 1; 写入 左边界
        } else {
            // 否则
            right = mid as i64 - 1; // 把 中点 as i64 减 1; 写入 右边界
        }
    }
    -1 // 减 1
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let cases: Vec<(Vec<i32>, i32, i32)> = vec![
        (vec![1, 3, 5, 7, 9], 5, 2),
        (vec![1, 3, 5, 7, 9], 4, -1),
        (vec![], 5, -1),
        (vec![1, 3, 5, 7, 9], 1, 0),
    ];
    for (idx, (a, t, want)) in cases.iter().enumerate() {
        // for (idx, (数组, 另一字符串, want)) in cases.iter().enumerate() {
        let got = binary_search(a, *t); // 把 binary_search(数组, 乘 另一字符串) 存入 got
        assert_eq!(got, *want, "case {} failed", idx); // 断言校验
    }
    println!("PASS"); // 全部用例通过，输出 PASS
}
