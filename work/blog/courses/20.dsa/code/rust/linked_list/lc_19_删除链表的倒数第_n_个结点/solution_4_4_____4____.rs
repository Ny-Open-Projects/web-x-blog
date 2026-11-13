// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133746567
// LeetCode 19. 删除链表的倒数第N个结点 — Rust 版（方案4）
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
fn remove_nth_from_end(head: Option<Box<ListNode>>, n: i32) -> Option<Box<ListNode>> {
    // 定义函数/方法 remove_nth_from_end
    let vals = to_vec(&head); // 把 to_vec( 按位与 头节点) 存入 vals
    let len = vals.len(); // 把 vals.长度() 存入 长度
    let idx = len as i32 - n; // 要删除的下标
    let mut out: Option<Box<ListNode>> = None; // 把 None; 写入 let mut out: Option<Box<ListNode>>
    for (i, &v) in vals.iter().enumerate().rev() {
        // for (下标 i, 按位与 值) in vals.iter().enumerate().rev() {
        if i as i32 == idx {
            continue;
        } // 若 下标 i as i32 等于 idx { continue; }
        out = Some(Box::new(ListNode { val: v, next: out })); // 把 Some(Box::new(ListNode { 值: 值, 下一个: out })); 写入 out
    }
    out // out
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(
        to_vec(&remove_nth_from_end(build_list(&[1, 2, 3, 4, 5]), 2)),
        vec![1, 2, 3, 5]
    ); // 断言校验
    assert_eq!(
        to_vec(&remove_nth_from_end(build_list(&[1]), 1)),
        Vec::<i32>::new()
    ); // 断言校验
    assert_eq!(
        to_vec(&remove_nth_from_end(build_list(&[1, 2]), 2)),
        vec![2]
    ); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
