// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134221939
// LeetCode 704. 二分查找 — Rust 版

fn search(nums: &[i32], target: i32) -> i32 {
    // 定义函数/方法 search
    let mut left: i32 = 0; // 把 0; 写入 let mut left: i32
    let mut right: i32 = nums.len() as i32 - 1; // 把 数组.长度() as i32 减 1; 写入 let mut right: i32
    while left <= right {
        // 把 右边界 { 写入 while left <
        let mid = left + (right - left) / 2; // 把 左边界 加 (右边界 减 左边界) 除以 2 存入 中点
        let v = nums[mid as usize]; // 把 数组[中点 as usize] 存入 值
        if v == target {
            // 若 值 等于 目标值
            return mid; // 返回 中点
        } else if v < target {
            // 否则，若 值 小于 目标值
            left = mid + 1; // 把 中点 加 1; 写入 左边界
        } else {
            // 否则
            right = mid - 1; // 把 中点 减 1; 写入 右边界
        }
    }
    -1 // 减 1
}

fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(search(&[1, 2, 3], 1), 0); // 断言校验
    assert_eq!(search(&[-1, 0, 3, 5, 9, 12], 9), 4); // 断言校验
    assert_eq!(search(&[-1, 0, 3, 5, 9, 12], 2), -1); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
