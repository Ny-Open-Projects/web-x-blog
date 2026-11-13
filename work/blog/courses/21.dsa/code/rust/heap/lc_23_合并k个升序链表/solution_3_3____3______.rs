// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134283831
// LeetCode 23. 合并K个升序链表 — Rust 版（方案3）
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
fn merge_two(a: Option<Box<ListNode>>, b: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    // 定义函数/方法 merge_two
    match (a, b) {
        // 按情况匹配处理
        (None, x) | (x, None) => x,
        (Some(mut x), Some(mut y)) => {
            if y.val < x.val {
                std::mem::swap(&mut x, &mut y);
            } // 若 y.值 小于 x.值 { std::mem::交换 按位与 mut x, 按位与 mut y); }
            x.next = merge_two(x.next.take(), Some(y)); // 把 merge_two(x.下一个.take(), Some(y)); 写入 下一个
            Some(x) // Some(x)
        }
    }
}
fn merge_k_lists(lists: Vec<Option<Box<ListNode>>>) -> Option<Box<ListNode>> {
    // 定义函数/方法 merge_k_lists
    let mut acc = None; // 把 None; 写入 let mut acc
    for l in lists {
        acc = merge_two(acc, l);
    } // 逐个取出 lists 的元素（左指针）
    acc // 累加器
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
    let lists2 = vec![build_list(&[])]; // 把 vec取反 [build_list( 按位与 [])] 存入 lists2
    assert_eq!(list_to_vec(&merge_k_lists(lists2)), Vec::<i32>::new()); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
