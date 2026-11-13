// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136236962
// LeetCode 1685. 有序数组中差绝对值之和 — Rust 版（方案1）
fn get_sum_absolute_differences(nums: Vec<i32>) -> Vec<i32> {
    // 定义函数/方法 get_sum_absolute_differences
    let n = nums.len(); // 把 数组.长度() 存入 元素个数
    let total: i64 = nums.iter().map(|&x| x as i64).sum();
    let mut prefix = 0i64; // 把 0i64; 写入 let mut prefix
    let mut out = Vec::with_capacity(n); // 把 Vec::with_capacity(元素个数); 写入 let mut out
    for i in 0..n {
        // 逐个取出 0 的元素（下标 i）
        let v = nums[i] as i64; // 把 数组[下标 i] as i64 存入 值
        let left = (v * i as i64 - prefix) as i64; // 把 (值 乘 下标 i as i64 减 prefix) as i64 存入 左边界
        let right = ((total - prefix - v) - v * (n - 1 - i) as i64) as i64;
        out.push((left + right) as i32); // 把 (左边界 加 右边界 压入栈/数组尾部
        prefix += v; // prefix累加 值
    }
    out // out
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(get_sum_absolute_differences(vec![2, 3, 5]), vec![4, 3, 5]); // 断言校验
    assert_eq!(
        get_sum_absolute_differences(vec![1, 4, 6, 8, 10]),
        vec![24, 15, 13, 15, 21]
    ); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
