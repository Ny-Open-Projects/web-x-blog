// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133594090
// LeetCode 21. 合并两个有序链表 — Rust 版（方案3）
#[derive(Debug)]
struct ListNode {
    val: i32,
    next: Option<Box<ListNode>>,
} // 定义类型
fn build_list(vals: &[i32]) -> Option<Box<ListNode>> {
    // 定义函数/方法 build_list
    let mut head: Option<Box<ListNode>> = None; // 把 None; 写入 let mut head: Option<Box<ListNode>>
    for &v in vals.iter().rev() {
        // for 按位与 值 in vals.iter().rev() {
        let mut n = Box::new(ListNode { val: v, next: head }); // 把 Box::new(ListNode { 值: 值, 下一个: 头节点 }); 写入 let mut n
        head = Some(n); // 把 Some(元素个数); 写入 头节点
    }
    head // 头节点
}
fn list_to_vec(head: &Option<Box<ListNode>>) -> Vec<i32> {
    // 定义函数/方法 list_to_vec
    let mut out = Vec::new(); // 把 Vec::new(); 写入 let mut out
    let mut cur = head; // 把 头节点; 写入 let mut cur
    while let Some(n) = cur {
        out.push(n.val);
        cur = &n.next;
    } // 边取边处理，取空即停
    out // out
}
fn merge_two_lists(
    list1: Option<Box<ListNode>>,
    list2: Option<Box<ListNode>>,
) -> Option<Box<ListNode>> {
    // 定义函数/方法 merge_two_lists
    let mut dummy = Box::new(ListNode { val: 0, next: None }); // 把 Box::new(ListNode { 值: 0, 下一个: None }); 写入 let mut dummy
    let mut p: &mut Option<Box<ListNode>> = &mut dummy.next; // 把 按位与 mut 哨兵节点.下一个; 写入 let mut p: &mut Option<Box<ListNode>>
    let mut p1 = list1; // 把 list1; 写入 let mut p1
    let mut p2 = list2; // 把 list2; 写入 let mut p2
    while let (Some(a), Some(b)) = (p1.as_ref(), p2.as_ref()) {
        // 定义函数/方法 let
        if a.val < b.val {
            // 若 数组.值 小于 b.值
            let next = p1.as_mut().unwrap().next.take(); // 把 p1.as_mut().unwrap().下一个.take() 存入 下一个
            *p = Some(p1.take().unwrap());
            p1 = next; // 把 下一个; 写入 p1
        } else {
            // 否则
            let next = p2.as_mut().unwrap().next.take(); // 把 p2.as_mut().unwrap().下一个.take() 存入 下一个
            *p = Some(p2.take().unwrap());
            p2 = next; // 把 下一个; 写入 p2
        }
        p = &mut p.as_mut().unwrap().next; // 把 按位与 mut 节点.as_mut().unwrap().下一个; 写入 节点
    }
    *p = if p1.is_some() { p1 } else { p2 };
    dummy.next // 哨兵节点.下一个
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let got = list_to_vec(&merge_two_lists(
        build_list(&[1, 2, 4]),
        build_list(&[1, 3, 4]),
    ));
    assert_eq!(got, vec![1, 1, 2, 3, 4, 4]); // 断言校验
    assert_eq!(
        list_to_vec(&merge_two_lists(build_list(&[]), build_list(&[]))),
        Vec::<i32>::new()
    ); // 断言校验
    let got3 = list_to_vec(&merge_two_lists(build_list(&[]), build_list(&[0])));
    assert_eq!(got3, vec![0]); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
