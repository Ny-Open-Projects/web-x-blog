// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145568435
// LeetCode 350. 两个数组的交集 II — Rust 版（方案1）
use std::collections::HashMap; // 引入依赖
fn intersect(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
    // 定义函数/方法 intersect
    let (a, b) = if nums1.len() <= nums2.len() {
        (&nums1, &nums2)
    } else {
        (&nums2, &nums1)
    };
    let mut mp: HashMap<i32, i32> = HashMap::new(); // 把 HashMap::new(); 写入 let mut mp: HashMap<i32, i32>
    for &v in a {
        *mp.entry(v).or_insert(0) += 1;
    } // 把 1; } 写入 for &v in a { *mp.entry(v).or_insert(0) +
    let mut res = Vec::new(); // 把 Vec::new(); 写入 let mut res
    for &v in b {
        // for 按位与 值 in b {
        if let Some(c) = mp.get_mut(&v) {
            // 若 let Some(字符) 赋值为 mp.get_mut( 按位与 值
            if *c > 0 {
                res.push(v);
                *c -= 1;
            } // 若 乘 字符 超过 0 { 结果 追加 值); 乘 字符 累减 1; }
        }
    }
    res // 结果
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(intersect(vec![1, 2, 2, 1], vec![2, 2]), vec![2, 2]); // 断言校验
    assert_eq!(intersect(vec![4, 9, 5], vec![9, 4, 9, 8, 4]), vec![9, 4]); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
