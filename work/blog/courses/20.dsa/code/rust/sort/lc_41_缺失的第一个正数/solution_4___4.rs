// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134066015
// LeetCode 41. 缺失的第一个正数 — Rust 版（方案4）
fn first_missing_positive(nums: Vec<i32>) -> i32 {
    // 定义函数/方法 first_missing_positive
    if nums.is_empty() {
        return 1;
    } // 若 数组 是否为空 { return 1; }
    let mut pos: Vec<i32> = nums.iter().cloned().filter(|&x| x > 0).collect();
    if pos.is_empty() {
        return 1;
    } // 若 pos 是否为空 { return 1; }
    pos.sort(); // 排序
    if pos[0] != 1 {
        return 1;
    } // 若 pos[0] 不等于 1 { return 1; }
    let n = pos.len(); // 把 pos.长度() 存入 元素个数
    for i in 0..n - 1 {
        // 逐个取出 0 的元素（下标 i）
        if pos[i + 1] - pos[i] > 1 {
            return pos[i] + 1;
        } // 若 pos[下标 i 加 1] 减 pos[下标 i] 超过 1 { return pos[下标 i] 加 1; }
    }
    pos[n - 1] + 1 // pos[元素个数 减 1] 加 1
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(first_missing_positive(vec![1, 2, 0]), 3); // 断言校验
    assert_eq!(first_missing_positive(vec![3, 4, -1, 1]), 2); // 断言校验
    assert_eq!(first_missing_positive(vec![7, 8, 9, 11, 12]), 1); // 断言校验
    assert_eq!(first_missing_positive(vec![]), 1); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
