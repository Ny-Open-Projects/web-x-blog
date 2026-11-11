// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133813394
// LeetCode 203. 移除链表元素 — Rust 版（方案1）
#[derive(Debug)]
struct ListNode {
    val: i32,
    next: Option<Box<ListNode>>,
} // 定义类型
fn build_list(vals: &[i32]) -> Option<Box<ListNode>> {
    // 定义函数/方法 build_list
    let mut head: Option<Box<ListNode>> = None; // 把 None; 写入 let mut head: Option<Box<ListNode>>
    for &v in vals.iter().rev() {
        head = Some(Box::new(ListNode { val: v, next: head }));
    }
    head // 头节点
}
fn to_vec(h: &Option<Box<ListNode>>) -> Vec<i32> {
    // 定义函数/方法 to_vec
    let mut out = Vec::new(); // 把 Vec::new(); 写入 let mut out
    let mut cur = h; // 把 h; 写入 let mut cur
    while let Some(n) = cur {
        out.push(n.val);
        cur = &n.next;
    } // 边取边处理，取空即停
    out // out
}
fn remove_elements(head: Option<Box<ListNode>>, val: i32) -> Option<Box<ListNode>> {
    // 定义函数/方法 remove_elements
    // 重建法（Rust 所有权友好）
    let vals = to_vec(&head); // 把 to_vec( 按位与 头节点) 存入 vals
    let kept: Vec<i32> = vals.into_iter().filter(|&v| v != val).collect();
    let mut out: Option<Box<ListNode>> = None; // 把 None; 写入 let mut out: Option<Box<ListNode>>
    for &v in kept.iter().rev() {
        out = Some(Box::new(ListNode { val: v, next: out }));
    }
    out // out
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(
        to_vec(&remove_elements(build_list(&[1, 2, 3, 4, 5, 6]), 6)),
        vec![1, 2, 3, 4, 5]
    ); // 断言校验
    assert_eq!(
        to_vec(&remove_elements(build_list(&[7, 7, 7, 7]), 7)),
        Vec::<i32>::new()
    ); // 断言校验
    assert_eq!(
        to_vec(&remove_elements(build_list(&[1, 2, 2, 1]), 2)),
        vec![1, 1]
    ); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
