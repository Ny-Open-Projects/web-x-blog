// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130734875
// LeetCode 682. 棒球比赛 — Rust 版（方案4）
fn cal_points(ops: Vec<&str>) -> i32 {
    // 定义函数/方法 cal_points
    let mut st: Vec<i32> = Vec::new(); // 把 Vec::new(); 写入 let mut st: Vec<i32>
    for op in ops {
        // 逐个取出 ops 的元素（op）
        match op {
            // 按情况匹配处理
            "+" => {
                let b = *st.last().unwrap();
                let a = st[st.len() - 2];
                st.push(a + b);
            }
            "D" => {
                st.push(2 * st.last().unwrap());
            }
            "C" => {
                st.pop();
            }
            _ => st.push(op.parse().unwrap()),
        }
    }
    st.iter().sum() // st.iter().累计和()
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(cal_points(vec!["5", "2", "C", "D", "+"]), 30); // 断言校验
    assert_eq!(
        cal_points(vec!["5", "-2", "4", "C", "D", "9", "+", "+"]),
        27
    ); // 断言校验
    assert_eq!(cal_points(vec!["1", "C"]), 0); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
