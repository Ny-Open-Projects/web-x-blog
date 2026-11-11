// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133816714
// LeetCode 141. 环形链表 — Rust 版（方案3）
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
        head = Some(Box::new(ListNode { val: v, next: head })); // 把 Some(Box::new(ListNode { 值: 值, 下一个: 头节点 })); 写入 头节点
    }
    head // 头节点
}
fn has_cycle(head: Option<&ListNode>) -> bool {
    // 定义函数/方法 has_cycle
    let mut slow = head; // 把 头节点; 写入 let mut slow
    let mut fast = head; // 把 头节点; 写入 let mut fast
    while let (Some(s), Some(f)) = (slow, fast) {
        // 定义函数/方法 let
        slow = s.next.as_deref(); // 把 字符串.下一个.as_deref(); 写入 慢指针
        let f2 = match f.next.as_deref() {
            Some(x) => x,
            None => return false,
        };
        fast = match f2.next.as_deref() {
            Some(x) => Some(x),
            None => return false,
        };
        if let (Some(a), Some(b)) = (slow, fast) {
            // 定义函数/方法 let
            if std::ptr::eq(a, b) {
                return true;
            } // 若 std::ptr::eq(数组, b) { return true; }
        }
    }
    false // false
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let lst = build_list(&[3, 2, 0, -4]); // 把 build_list( 按位与 [3, 2, 0, 减 4]) 存入 lst
    let head = lst.as_deref(); // 把 lst.as_deref() 存入 头节点
    assert!(!has_cycle(head)); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
