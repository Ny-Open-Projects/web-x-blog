// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133874590
// LeetCode 83. 删除排序链表中的重复元素 — Rust 版（方案4）
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
fn delete_duplicates(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    // 定义函数/方法 delete_duplicates
    let mut vals = to_vec(&head); // 把 to_vec( 按位与 头节点); 写入 let mut vals
    vals.dedup(); // vals.dedup();
    let mut out: Option<Box<ListNode>> = None; // 把 None; 写入 let mut out: Option<Box<ListNode>>
    for &v in vals.iter().rev() {
        out = Some(Box::new(ListNode { val: v, next: out }));
    }
    out // out
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(
        to_vec(&delete_duplicates(build_list(&[1, 1, 2]))),
        vec![1, 2]
    ); // 断言校验
    assert_eq!(
        to_vec(&delete_duplicates(build_list(&[1, 1, 2, 3, 3]))),
        vec![1, 2, 3]
    ); // 断言校验
    assert_eq!(to_vec(&delete_duplicates(build_list(&[1, 1, 1]))), vec![1]); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
