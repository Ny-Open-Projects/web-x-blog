// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114011
// LeetCode 232. 用栈实现队列 — Rust 版（方案1）
#[derive(Clone)]
enum Op232 {
    Push(i32),
    Pop,
    Peek,
    Empty,
} // 定义类型
fn my_queue_run(ops: Vec<Op232>) -> Vec<i32> {
    // 定义函数/方法 my_queue_run
    let mut in_stack: Vec<i32> = Vec::new(); // 把 Vec::new(); 写入 let mut in_stack: Vec<i32>
    let mut out_stack: Vec<i32> = Vec::new(); // 把 Vec::new(); 写入 let mut out_stack: Vec<i32>
    let mut out = Vec::new(); // 把 Vec::new(); 写入 let mut out
    for op in ops {
        // 逐个取出 ops 的元素（op）
        match op {
            // 按情况匹配处理
            Op232::Push(v) => in_stack.push(v),
            Op232::Pop => {
                if out_stack.is_empty() {
                    while let Some(v) = in_stack.pop() {
                        out_stack.push(v);
                    }
                }
                out.push(out_stack.pop().unwrap_or(-1)); // 把 out_stack 弹出 压入栈/数组尾部
            }
            Op232::Peek => {
                if out_stack.is_empty() {
                    while let Some(v) = in_stack.pop() {
                        out_stack.push(v);
                    }
                }
                out.push(*out_stack.last().unwrap_or(&-1)); // 把 乘 out_stack.last( 压入栈/数组尾部
            }
            Op232::Empty => out.push(if in_stack.is_empty() && out_stack.is_empty() {
                1
            } else {
                0
            }),
        }
    }
    out // out
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let ops = vec![
        Op232::Push(1),
        Op232::Push(2),
        Op232::Peek,
        Op232::Pop,
        Op232::Empty,
    ];
    assert_eq!(my_queue_run(ops), vec![1, 1, 0]); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
