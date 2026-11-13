// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145012016
// LeetCode 496. 下一个更大元素 I — Rust 版（方案1）
use std::collections::HashMap; // 引入依赖
fn next_greater_element(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
    // 定义函数/方法 next_greater_element
    let mut next: HashMap<i32, i32> = HashMap::new(); // 把 HashMap::new(); 写入 let mut next: HashMap<i32, i32>
    let mut st: Vec<i32> = Vec::new(); // 把 Vec::new(); 写入 let mut st: Vec<i32>
    for &v in &nums2 {
        // for 按位与 值 in 按位与 数组2 {
        while let Some(&top) = st.last() {
            // 边取边处理，取空即停
            if top < v {
                next.insert(top, v);
                st.pop();
            } else {
                break;
            } // 若 top 小于 值 { 下一个 插入 top, 值); st 弹出 ); } else { break; }
        }
        st.push(v); // 把 值 压入栈/数组尾部
    }
    nums1
        .iter()
        .map(|&v| *next.get(&v).unwrap_or(&-1))
        .collect()
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(
        next_greater_element(vec![4, 1, 2], vec![1, 3, 4, 2]),
        vec![-1, 3, -1]
    ); // 断言校验
    assert_eq!(
        next_greater_element(vec![2, 4], vec![1, 2, 3, 4]),
        vec![3, -1]
    ); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
