// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107431726
// LeetCode 107431726. 最大红矩形分析 — Rust 版（方案D：逐行高度 + 单调栈）
fn max_red_rectangle(matrix: &[&str]) -> i64 {
    // 定义函数/方法 max_red_rectangle
    let n = matrix.len(); // 把 矩阵.长度() 存入 元素个数
    let m = matrix[0].len(); // 把 矩阵[0].长度() 存入 映射表
    let mut ans = 0i64; // 把 0i64; 写入 let mut ans
    let mut height = vec![0i64; m + 2]; // 把 vec取反 [0i64; 映射表 加 2]; 写入 let mut height
    for k in 0..n {
        // 逐个取出 0 的元素（下标 k）
        let row = matrix[k].as_bytes(); // 把 矩阵[下标 k].as_bytes() 存入 row
        for i in 1..=m {
            // 逐个取出 1 的元素（下标 i）
            if row[i - 1] == b'.' {
                // 若 row[下标 i 减 1] 等于 b'.'
                height[i] += 1; // height[i]累加 1
            } else {
                // 否则
                height[i] = 0; // 把 0; 写入 height[i]
            }
        }
        let mut stack: Vec<usize> = vec![0]; // 把 vec取反 [0]; 写入 let mut stack: Vec<usize>
        for i in 1..=m + 1 {
            // 逐个取出 1 的元素（下标 i）
            while height[*stack.last().unwrap()] > height[i] {
                // while height[ 乘 栈.last().unwrap()] 超过 height[下标 i] {
                let top = stack.pop().unwrap(); // 把 栈 弹出 ).unwrap() 存入 top
                let now_h = height[top]; // 把 height[top] 存入 now_h
                let width = i - stack.last().unwrap() - 1; // 把 下标 i 减 栈.last().unwrap() 减 1 存入 width
                let area = now_h * width as i64; // 把 now_h 乘 width as i64 存入 area
                if area > ans {
                    // 若 area 超过 答案
                    ans = area; // 把 area; 写入 答案
                }
            }
            stack.push(i); // 把 下标 i 压入栈/数组尾部
        }
    }
    ans // 答案
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let matrix = [".....", "XXXXX", ".X...", "....."]; // 把 [「.....」, 「.....」, 「.....」, 「.....」] 存入 矩阵
    assert_eq!(max_red_rectangle(&matrix), 6, "mono"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
