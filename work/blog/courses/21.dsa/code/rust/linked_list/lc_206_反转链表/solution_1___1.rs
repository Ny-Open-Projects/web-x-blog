// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133785568
// LeetCode 206. 反转链表 — Rust 版（方案1）
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
fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    // 定义函数/方法 reverse_list
    let mut prev: Option<Box<ListNode>> = None; // 把 None; 写入 let mut prev: Option<Box<ListNode>>
    let mut cur = head; // 把 头节点; 写入 let mut cur
    while let Some(mut node) = cur {
        // 边取边处理，取空即停
        cur = node.next.take(); // 把 节点.下一个.take(); 写入 当前值
        node.next = prev; // 把 前一个; 写入 下一个
        prev = Some(node); // 把 Some(节点); 写入 前一个
    }
    prev // 前一个
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let got = to_vec(&reverse_list(build_list(&[1, 2, 3, 4, 5])));
    assert_eq!(got, vec![5, 4, 3, 2, 1]); // 断言校验
    assert_eq!(to_vec(&reverse_list(build_list(&[]))), Vec::<i32>::new()); // 断言校验
    assert_eq!(to_vec(&reverse_list(build_list(&[1]))), vec![1]); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
