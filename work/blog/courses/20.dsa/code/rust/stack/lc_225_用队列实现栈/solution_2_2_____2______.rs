// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145198996
// LeetCode 225. 用队列实现栈 — Rust 版（方案2）
#[derive(Clone)]
enum Op225 {
    Push(i32),
    Pop,
    Top,
    Empty,
} // 定义类型
fn my_stack_run(ops: Vec<Op225>) -> Vec<i32> {
    // 定义函数/方法 my_stack_run
    let mut q1: Vec<i32> = Vec::new(); // 把 Vec::new(); 写入 let mut q1: Vec<i32>
    let mut out = Vec::new(); // 把 Vec::new(); 写入 let mut out
    for op in ops {
        // 逐个取出 ops 的元素（op）
        match op {
            // 按情况匹配处理
            Op225::Push(v) => {
                q1.insert(0, v); // q1 插入 0, 值);
            }
            Op225::Pop => {
                if !q1.is_empty() {
                    out.push(q1.remove(0));
                } else {
                    out.push(-1);
                }
            }
            Op225::Top => out.push(*q1.first().unwrap_or(&-1)),
            Op225::Empty => out.push(if q1.is_empty() { 1 } else { 0 }),
        }
    }
    out // out
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let ops = vec![
        Op225::Push(1),
        Op225::Push(2),
        Op225::Top,
        Op225::Pop,
        Op225::Empty,
    ];
    assert_eq!(my_stack_run(ops), vec![2, 2, 0]); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
