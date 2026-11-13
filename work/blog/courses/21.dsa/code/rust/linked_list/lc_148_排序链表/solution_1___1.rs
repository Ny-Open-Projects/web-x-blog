// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133904873
// LeetCode 148. 排序链表 — Rust 版（方案1）
fn sort_list(vals: Vec<i32>) -> Vec<i32> {
    // 定义函数/方法 sort_list
    let mut v = vals; // 把 vals; 写入 let mut v
    v.sort(); // 排序
    v
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(sort_list(vec![4, 2, 1, 3]), vec![1, 2, 3, 4]); // 断言校验
    assert_eq!(sort_list(vec![-1, 5, 3, 4, 0]), vec![-1, 0, 3, 4, 5]); // 断言校验
    assert!(sort_list(vec![]).is_empty()); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
