// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134283831
// LeetCode 23. 合并K个升序链表 — Rust 版（方案2）
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
fn merge_k_lists(lists: Vec<Option<Box<ListNode>>>) -> Option<Box<ListNode>> {
    // 定义函数/方法 merge_k_lists
    let mut lists = lists; // 把 lists; 写入 let mut lists
    let mut dummy = Box::new(ListNode { val: 0, next: None }); // 把 Box::new(ListNode { 值: 0, 下一个: None }); 写入 let mut dummy
    let mut tail: &mut Option<Box<ListNode>> = &mut dummy.next;
    loop {
        // loop {
        let mut best: i32 = i32::MAX; // 把 i32::MAX; 写入 let mut best: i32
        let mut any = false; // 把 false; 写入 let mut any
        for l in lists.iter() {
            // 逐个取出 lists 的元素（左指针）
            if let Some(n) = l {
                // 若 let Some(元素个数) 赋值为 左指针
                if n.val < best {
                    best = n.val;
                    any = true;
                } // 若 元素个数.值 小于 当前最优 { 当前最优 赋值为 元素个数.值; any 赋值为 true; }
            }
        }
        if !any {
            break;
        } // 若 取反 any { break; }
        for l in lists.iter_mut() {
            // 逐个取出 lists 的元素（左指针）
            if let Some(n) = l {
                // 若 let Some(元素个数) 赋值为 左指针
                if n.val == best {
                    // 若 元素个数.值 等于 当前最优
                    let next = n.next.take(); // 把 元素个数.下一个.take() 存入 下一个
                    let mut node = l.take().unwrap(); // 把 左指针.take().unwrap(); 写入 let mut node
                    node.next = None; // 把 None; 写入 下一个
                    *tail = Some(node);
                    tail = &mut tail.as_mut().unwrap().next; // 把 按位与 mut 尾节点.as_mut().unwrap().下一个; 写入 尾节点
                    *l = next;
                    break; // 跳出循环
                }
            }
        }
    }
    dummy.next // 哨兵节点.下一个
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let lists = vec![
        build_list(&[1, 4, 5]),
        build_list(&[1, 3, 4]),
        build_list(&[2, 6]),
    ];
    let got = list_to_vec(&merge_k_lists(lists)); // 把 list_to_vec( 按位与 merge_k_lists(lists)) 存入 got
    assert_eq!(got, vec![1, 1, 2, 3, 4, 4, 5, 6]); // 断言校验
    let empty: Vec<Option<Box<ListNode>>> = vec![]; // 把 vec取反 []; 写入 let empty: Vec<Option<Box<ListNode>>>
    assert_eq!(list_to_vec(&merge_k_lists(empty)), Vec::<i32>::new()); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
