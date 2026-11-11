// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145245934
// LeetCode 155. 最小栈 — Rust 版（方案1）
#[derive(Clone)]
enum Op {
    Push(i32),
    Pop,
    Top,
    GetMin,
} // 定义类型
fn min_stack_run(ops: Vec<Op>) -> Vec<i32> {
    // 定义函数/方法 min_stack_run
    let mut vals: Vec<i32> = Vec::new(); // 把 Vec::new(); 写入 let mut vals: Vec<i32>
    let mut mins: Vec<i32> = Vec::new(); // 把 Vec::new(); 写入 let mut mins: Vec<i32>
    let mut out = Vec::new(); // 把 Vec::new(); 写入 let mut out
    for op in ops {
        // 逐个取出 ops 的元素（op）
        match op {
            // 按情况匹配处理
            Op::Push(v) => {
                vals.push(v); // 把 值 压入栈/数组尾部
                mins.push(if mins.is_empty() {
                    v
                } else {
                    (*mins.last().unwrap()).min(v)
                }); // 把 if mins.is_empty( 压入栈/数组尾部
            }
            Op::Pop => {
                vals.pop();
                mins.pop();
            }
            Op::Top => out.push(*vals.last().unwrap_or(&-1)),
            Op::GetMin => out.push(*mins.last().unwrap_or(&-1)),
        }
    }
    out // out
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let ops = vec![
        Op::Push(-2),
        Op::Push(0),
        Op::Push(-3),
        Op::GetMin,
        Op::Pop,
        Op::Top,
        Op::GetMin,
    ];
    assert_eq!(min_stack_run(ops), vec![-3, 0, -2]); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
