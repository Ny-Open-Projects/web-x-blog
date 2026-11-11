// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133922762
// LeetCode 160. 相交链表 — Rust 版（方案1）
#[derive(Debug)]
struct ListNode {
    val: i32,
    next: Option<Box<ListNode>>,
} // 定义类型
fn get_intersection_node<'a>(
    a: Option<&'a ListNode>,
    b: Option<&'a ListNode>,
) -> Option<&'a ListNode> {
    let (mut p1, mut p2) = (a, b); // 把 (数组, b); 写入 let (mut p1, mut p2)
    loop {
        // loop {
        match (p1, p2) {
            // 按情况匹配处理
            (None, None) => return None,
            (Some(x), Some(y)) if std::ptr::eq(x, y) => return Some(x),
            _ => {
                p1 = match p1 {
                    Some(x) => x.next.as_deref(),
                    None => b,
                };
                p2 = match p2 {
                    Some(y) => y.next.as_deref(),
                    None => a,
                };
            }
        }
    }
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert!(get_intersection_node(None, None).is_none()); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
