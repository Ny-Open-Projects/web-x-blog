// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133867938
// LeetCode 876. 链表的中间结点 — Rust 版（方案2）
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
fn middle_node(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    // 定义函数/方法 middle_node
    // 快慢指针找中间：返回后半段起点（转移所有权：重建后半段）
    let mut vals = Vec::new(); // 把 Vec::new(); 写入 let mut vals
    let mut cur = &head; // 把 按位与 头节点; 写入 let mut cur
    while let Some(n) = cur {
        vals.push(n.val);
        cur = &n.next;
    } // 边取边处理，取空即停
    let mid = vals.len() / 2; // 把 vals.长度() 除以 2 存入 中点
    let mut out: Option<Box<ListNode>> = None; // 把 None; 写入 let mut out: Option<Box<ListNode>>
    for &v in vals[mid..].iter().rev() {
        out = Some(Box::new(ListNode { val: v, next: out }));
    }
    out // out
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(
        to_vec(&middle_node(build_list(&[1, 2, 3, 4, 5]))),
        vec![3, 4, 5]
    ); // 断言校验
    assert_eq!(
        to_vec(&middle_node(build_list(&[1, 2, 3, 4, 5, 6]))),
        vec![4, 5, 6]
    ); // 断言校验
    assert_eq!(to_vec(&middle_node(build_list(&[1]))), vec![1]); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
