// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133657416
// LeetCode 92. 反转链表II — Rust 版（方案2）
fn reverse_between(vals: Vec<i32>, left: i32, right: i32) -> Vec<i32> {
    // 定义函数/方法 reverse_between
    let mut v = vals; // 把 vals; 写入 let mut v
    let (l, r) = ((left - 1) as usize, (right - 1) as usize); // 把 ((左边界 减 1) as usize, (右边界 减 1) as usize); 写入 let (l, r)
    let seg: Vec<i32> = v[l..=r].iter().rev().cloned().collect();
    v[l..=r].copy_from_slice(&seg); // 把 右指针].copy_from_slice( 按位与 seg); 写入 v[l
    v
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(
        reverse_between(vec![1, 2, 3, 4, 5], 2, 4),
        vec![1, 4, 3, 2, 5]
    ); // 断言校验
    assert_eq!(
        reverse_between(vec![1, 2, 3, 4, 5], 1, 4),
        vec![4, 3, 2, 1, 5]
    ); // 断言校验
    assert_eq!(reverse_between(vec![5], 1, 1), vec![5]); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
