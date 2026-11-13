// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133874671
// LeetCode 142. 环形链表II — Rust 版（方案2）
#[derive(Debug)]
struct ListNode {
    val: i32,
    next: Option<Box<ListNode>>,
} // 定义类型
fn detect_cycle(mut head: Option<&ListNode>) -> Option<i32> {
    // 定义函数/方法 detect_cycle
    let mut slow = head; // 把 头节点; 写入 let mut slow
    let mut fast = head; // 把 头节点; 写入 let mut fast
    while let (Some(s), Some(f)) = (slow, fast) {
        // 定义函数/方法 let
        slow = s.next.as_deref(); // 把 字符串.下一个.as_deref(); 写入 慢指针
        let f2 = f.next.as_deref()?; // 把 f.下一个.as_deref()? 存入 f2
        fast = f2.next.as_deref(); // 把 f2.下一个.as_deref(); 写入 快指针
        if let (Some(a), Some(b)) = (slow, fast) {
            // 定义函数/方法 let
            if std::ptr::eq(a, b) {
                // 若 std::ptr::eq(数组, b
                let mut p1 = head; // 把 头节点; 写入 let mut p1
                let mut p2 = slow; // 把 慢指针; 写入 let mut p2
                loop {
                    // loop {
                    let (x, y) = (p1?, p2?); // 把 (p1?, p2?); 写入 let (x, y)
                    if std::ptr::eq(x, y) {
                        return Some(x.val);
                    } // 若 std::ptr::eq(x, y) { return Some(x.值); }
                    p1 = x.next.as_deref(); // 把 x.下一个.as_deref(); 写入 p1
                    p2 = y.next.as_deref(); // 把 y.下一个.as_deref(); 写入 p2
                }
            }
        }
    }
    None // None
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(detect_cycle(None), None); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
