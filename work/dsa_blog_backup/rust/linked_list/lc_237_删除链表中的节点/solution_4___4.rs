// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133886377
// LeetCode 237. 删除链表中的节点 — Rust 版（方案4）
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
fn delete_node_by_val(head: &mut Option<Box<ListNode>>, target: i32) {
    // 定义函数/方法 delete_node_by_val
    // LeetCode 237 语义：复制下一节点值后删除下一节点。
    // Rust 的 Box 所有权模型下等价实现：按值删除首个匹配节点（重建法）。
    let vals = to_vec(head); // 把 to_vec(头节点) 存入 vals
    let mut kept: Vec<i32> = Vec::new(); // 把 Vec::new(); 写入 let mut kept: Vec<i32>
    let mut skipped = false; // 把 false; 写入 let mut skipped
    for &v in &vals {
        // for 按位与 值 in 按位与 vals {
        if !skipped && v == target {
            skipped = true;
            continue;
        } // 若 取反 skipped 且 值 等于 目标值 { skipped 赋值为 true; continue; }
        kept.push(v); // 把 值 压入栈/数组尾部
    }
    let mut out: Option<Box<ListNode>> = None; // 把 None; 写入 let mut out: Option<Box<ListNode>>
    for &v in kept.iter().rev() {
        out = Some(Box::new(ListNode { val: v, next: out }));
    }
    *head = out;
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let mut l = build_list(&[4, 5, 1, 9]); // 把 build_list( 按位与 [4, 5, 1, 9]); 写入 let mut l
    delete_node_by_val(&mut l, 5); // delete_node_by_val( 按位与 mut 左指针, 5);
    assert_eq!(to_vec(&l), vec![4, 1, 9]); // 断言校验
    let mut l2 = build_list(&[1, 2, 3]); // 把 build_list( 按位与 [1, 2, 3]); 写入 let mut l2
    delete_node_by_val(&mut l2, 2); // delete_node_by_val( 按位与 mut l2, 2);
    assert_eq!(to_vec(&l2), vec![1, 3]); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
