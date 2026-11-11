// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134026430
// LeetCode 54. 螺旋矩阵 — Rust 版

// 方案1：四边界逐层收缩
fn spiral_order(matrix: &[Vec<i32>]) -> Vec<i32> {
    // 定义函数/方法 spiral_order
    if matrix.is_empty() || matrix[0].is_empty() {
        // 若 矩阵 是否为空 或 矩阵[0].is_empty(
        return Vec::new(); // 返回 Vec::new()
    }
    let rows = matrix.len() as isize; // 把 矩阵.长度() as isize 存入 行数
    let cols = matrix[0].len() as isize; // 把 矩阵[0].长度() as isize 存入 列数
    let mut result: Vec<i32> = Vec::new(); // 把 Vec::new(); 写入 let mut result: Vec<i32>
    let mut top: isize = 0; // 把 0; 写入 let mut top: isize
    let mut bottom: isize = rows - 1; // 把 行数 减 1; 写入 let mut bottom: isize
    let mut left: isize = 0; // 把 0; 写入 let mut left: isize
    let mut right: isize = cols - 1; // 把 列数 减 1; 写入 let mut right: isize
    while top <= bottom && left <= right {
        // 把 bottom 且 左边界 不超过 右边界 { 写入 while top <
        let mut i = left; // 把 左边界; 写入 let mut i
        while i <= right {
            // 把 右边界 { 写入 while i <
            result.push(matrix[top as usize][i as usize]); // 把 矩阵[top as usize][下标 i as usize] 压入栈/数组尾部
            i += 1; // 下标 i累加 1
        }
        top += 1; // top累加 1
        i = top; // 把 top; 写入 下标 i
        while i <= bottom {
            // 把 bottom { 写入 while i <
            result.push(matrix[i as usize][right as usize]); // 把 矩阵[下标 i as usize][右边界 as usize] 压入栈/数组尾部
            i += 1; // 下标 i累加 1
        }
        right -= 1; // 右边界累减 1
        if top <= bottom {
            // 若 top 不超过 bottom
            i = right; // 把 右边界; 写入 下标 i
            while i >= left {
                // 把 左边界 { 写入 while i >
                result.push(matrix[bottom as usize][i as usize]); // 把 矩阵[bottom as usize][下标 i as usize] 压入栈/数组尾部
                i -= 1; // 下标 i累减 1
            }
            bottom -= 1; // bottom累减 1
        }
        if left <= right {
            // 若 左边界 不超过 右边界
            i = bottom; // 把 bottom; 写入 下标 i
            while i >= top {
                // 把 top { 写入 while i >
                result.push(matrix[i as usize][left as usize]); // 把 矩阵[下标 i as usize][左边界 as usize] 压入栈/数组尾部
                i -= 1; // 下标 i累减 1
            }
            left += 1; // 左边界累加 1
        }
    }
    result // 结果
}

fn main() {
    // 程序入口：跑内嵌自测用例
    // 与 TS 事实源内嵌用例一致：空矩阵
    let empty: Vec<Vec<i32>> = vec![]; // 把 vec取反 []; 写入 let empty: Vec<Vec<i32>>
    assert!(spiral_order(&empty).is_empty(), "FAILED empty"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
