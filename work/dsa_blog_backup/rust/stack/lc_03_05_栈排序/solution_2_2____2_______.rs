// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397311
// LeetCode 面试题 03.05. 栈排序 — Rust 版（方案2）
fn sorted_stack(mut input: Vec<i32>) -> Vec<i32> {
    // 定义函数/方法 sorted_stack
    // 辅助栈法：temp 存降序，最终 output 升序
    let mut temp: Vec<i32> = Vec::new(); // 把 Vec::new(); 写入 let mut temp: Vec<i32>
    let mut output: Vec<i32> = Vec::new(); // 把 Vec::new(); 写入 let mut output: Vec<i32>
    while let Some(v) = input.pop() {
        // 边取边处理，取空即停
        while let Some(&t) = temp.last() {
            // 边取边处理，取空即停
            if t > v {
                output.push(temp.pop().unwrap());
            } else {
                break;
            } // 若 另一字符串 超过 值 { 输出 追加 临时变量 弹出 ).unwrap()); } else { break; }
        }
        temp.push(v); // 把 值 压入栈/数组尾部
    }
    while let Some(v) = temp.pop() {
        output.push(v);
    } // 边取边处理，取空即停
    output.sort(); // 排序
    output // 输出
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let got = sorted_stack(vec![5, 2, 1, 4, 3]); // 把 sorted_stack(vec取反 [5, 2, 1, 4, 3]) 存入 got
    assert_eq!(got, vec![1, 2, 3, 4, 5]); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
