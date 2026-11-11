// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134083295
// 数据结构与算法之排序: 归并排序 — Rust 版（方案2）
fn merge_sort(nums: Vec<i32>) -> Vec<i32> {
    // 定义函数/方法 merge_sort
    if nums.len() <= 1 {
        return nums;
    } // 若 数组.长度() 不超过 1 { return 数组; }
    let mid = nums.len() / 2; // 把 数组.长度() 除以 2 存入 中点
    let left = merge_sort(nums[..mid].to_vec()); // 把 merge_sort(数组[..中点].to_vec()) 存入 左边界
    let right = merge_sort(nums[mid..].to_vec()); // 把 merge_sort(数组[中点..].to_vec()) 存入 右边界
    let mut out = Vec::with_capacity(nums.len()); // 把 Vec::with_capacity(数组.长度()); 写入 let mut out
    let (mut i, mut j) = (0usize, 0usize); // 把 (0usize, 0usize); 写入 let (mut i, mut j)
    while i < left.len() && j < right.len() {
        // while 下标 i 小于 左边界.长度() 且 下标 j 小于 右边界.长度() {
        if left[i] <= right[j] {
            out.push(left[i]);
            i += 1;
        } else {
            out.push(right[j]);
            j += 1;
        }
    }
    out.extend_from_slice(&left[i..]); // out.extend_from_slice( 按位与 左边界[下标 i..]);
    out.extend_from_slice(&right[j..]); // out.extend_from_slice( 按位与 右边界[下标 j..]);
    out // out
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(merge_sort(vec![5, 4, 3, 2, 1]), vec![1, 2, 3, 4, 5]); // 断言校验
    assert_eq!(merge_sort(vec![3, 1, 4, 1, 5]), vec![1, 1, 3, 4, 5]); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
