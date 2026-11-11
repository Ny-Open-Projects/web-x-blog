// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130726302
// LeetCode 150. 逆波兰表达式求值 — Rust 版（方案1）
fn eval_rpn(tokens: Vec<&str>) -> i32 {
    // 定义函数/方法 eval_rpn
    let mut st: Vec<i64> = Vec::new(); // 把 Vec::new(); 写入 let mut st: Vec<i64>
    for t in tokens {
        // 逐个取出 tokens 的元素（另一字符串）
        match t {
            // 按情况匹配处理
            "+" => {
                let b = st.pop().unwrap();
                let a = st.pop().unwrap();
                st.push(a + b);
            }
            "-" => {
                let b = st.pop().unwrap();
                let a = st.pop().unwrap();
                st.push(a - b);
            }
            "*" => {
                let b = st.pop().unwrap();
                let a = st.pop().unwrap();
                st.push(a * b);
            }
            "/" => {
                let b = st.pop().unwrap();
                let a = st.pop().unwrap();
                st.push(a / b);
            }
            _ => st.push(t.parse::<i64>().unwrap()),
        }
    }
    st[0] as i32 // st[0] as i32
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(eval_rpn(vec!["2", "1", "+", "3", "*"]), 9); // 断言校验
    assert_eq!(eval_rpn(vec!["4", "13", "5", "/", "+"]), 6); // 断言校验
    assert_eq!(
        eval_rpn(vec![
            "10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"
        ]),
        22
    ); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
