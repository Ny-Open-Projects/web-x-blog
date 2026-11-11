// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233913
// LeetCode 739. 每日温度 — Rust 版（方案1）
fn daily_temperatures(temps: Vec<i32>) -> Vec<i32> {
    // 定义函数/方法 daily_temperatures
    let n = temps.len(); // 把 temps.长度() 存入 元素个数
    let mut res = vec![0i32; n]; // 把 vec取反 [0i32; 元素个数]; 写入 let mut res
    let mut st: Vec<usize> = Vec::new(); // 把 Vec::new(); 写入 let mut st: Vec<usize>
    for i in 0..n {
        // 逐个取出 0 的元素（下标 i）
        while let Some(&top) = st.last() {
            // 边取边处理，取空即停
            if temps[top] < temps[i] {
                res[top] = (i - top) as i32;
                st.pop();
            } else {
                break;
            }
        }
        st.push(i); // 把 下标 i 压入栈/数组尾部
    }
    res // 结果
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(
        daily_temperatures(vec![73, 74, 75, 71, 69, 72, 76, 73]),
        vec![1, 1, 4, 2, 1, 1, 0, 0]
    ); // 断言校验
    assert_eq!(daily_temperatures(vec![30, 40, 50, 60]), vec![1, 1, 1, 0]); // 断言校验
    assert_eq!(daily_temperatures(vec![30, 60, 90]), vec![1, 1, 0]); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
