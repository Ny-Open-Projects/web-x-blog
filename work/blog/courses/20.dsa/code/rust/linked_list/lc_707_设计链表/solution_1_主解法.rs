// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134120377
// LeetCode 707. 设计链表 — Rust 版（方案1）
#[derive(Clone)]
enum Op707 {
    AddAtHead(i32),
    AddAtTail(i32),
    AddAtIndex(i32, i32),
    Get(i32),
    DeleteAtIndex(i32),
} // 定义类型
fn my_linked_list_run(ops: Vec<Op707>) -> Vec<i32> {
    // 定义函数/方法 my_linked_list_run
    let mut v: Vec<i32> = Vec::new(); // 把 Vec::new(); 写入 let mut v: Vec<i32>
    let mut out = Vec::new(); // 把 Vec::new(); 写入 let mut out
    for op in ops {
        // 逐个取出 ops 的元素（op）
        match op {
            // 按情况匹配处理
            Op707::AddAtHead(x) => v.insert(0, x),
            Op707::AddAtTail(x) => v.push(x),
            Op707::AddAtIndex(i, x) => {
                let idx = i.max(0) as usize; // 把 下标 i.取较大值 0) as usize 存入 idx
                if idx <= v.len() {
                    v.insert(idx, x);
                } // 若 idx 不超过 值.长度() { 值 插入 idx, x); }
            }
            Op707::Get(i) => {
                if i >= 0 && (i as usize) < v.len() {
                    out.push(v[i as usize]);
                } else {
                    out.push(-1);
                }
            }
            Op707::DeleteAtIndex(i) => {
                if i >= 0 && (i as usize) < v.len() {
                    v.remove(i as usize);
                }
            }
        }
    }
    out // out
}
fn main() {
    // 程序入口：跑内嵌自测用例
    // LC 官方：addAtHead(1), addAtTail(3), addAtIndex(1,2)→[1,2,3], get(1)=2, deleteAtIndex(1)→[1,3], get(1)=3
    let ops = vec![
        Op707::AddAtHead(1),
        Op707::AddAtTail(3),
        Op707::AddAtIndex(1, 2),
        Op707::Get(1),
        Op707::DeleteAtIndex(1),
        Op707::Get(1),
    ];
    assert_eq!(my_linked_list_run(ops), vec![2, 3]); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
