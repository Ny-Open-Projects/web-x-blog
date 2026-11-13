// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/105893757
// 栈排序分析 — Rust 版（方案2）
fn stack_sort(input: &[i32]) -> Vec<i32> {
    // 定义函数/方法 stack_sort
    let mut st: Vec<i32> = Vec::new(); // 把 Vec::new(); 写入 let mut st: Vec<i32>
    for &v in input {
        st.push(v);
    } // 把 值 压入栈/数组尾部
    let mut out = Vec::new(); // 把 Vec::new(); 写入 let mut out
    while let Some(v) = st.pop() {
        out.push(v);
    } // 边取边处理，取空即停
    out // out
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(stack_sort(&[3, 1, 5, 2, 4]), vec![4, 2, 5, 1, 3]); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
