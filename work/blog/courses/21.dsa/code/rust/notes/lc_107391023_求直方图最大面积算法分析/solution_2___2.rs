// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107391023
// 求直方图最大面积算法分析 — Rust 版（方案2）
fn get_result(_n: i32, heights: &[i32]) -> i32 {
    // 定义函数/方法 get_result
    let mut st: Vec<usize> = Vec::new(); // 把 Vec::new(); 写入 let mut st: Vec<usize>
    let mut best = 0; // 把 0; 写入 let mut best
    let h = heights; // 把 heights 存入 h
    let n = h.len(); // 把 h.长度() 存入 元素个数
    for i in 0..=n {
        // 逐个取出 0 的元素（下标 i）
        let cur = if i < n { h[i] } else { 0 }; // 把 if 下标 i 小于 元素个数 { h[下标 i] } else { 0 } 存入 当前值
        while let Some(&top) = st.last() {
            // 边取边处理，取空即停
            if h[top] >= cur {
                // 若 h[top] 不低于 当前值
                st.pop(); // 弹出栈顶元素
                let left = st.last().map(|&x| x as i64).unwrap_or(-1);
                let width = i as i64 - left - 1; // 把 下标 i as i64 减 左边界 减 1 存入 width
                best = best.max((h[top] as i64 * width) as i32); // 把 当前最优.取较大值 (h[top] as i64 乘 width) as i32); 写入 当前最优
            } else {
                break;
            } // 否则
        }
        st.push(i); // 把 下标 i 压入栈/数组尾部
    }
    best // 当前最优
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(get_result(5, &[0, 2, 3, 3, 3, 2, 0]), 10); // 断言校验
    assert_eq!(get_result(6, &[0, 2, 1, 5, 6, 2, 3, 0]), 10); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
