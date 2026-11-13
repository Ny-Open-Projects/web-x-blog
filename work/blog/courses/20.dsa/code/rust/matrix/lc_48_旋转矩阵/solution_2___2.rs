// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134032039
// LeetCode 48. 旋转矩阵 — Rust 版

// 方案2：先上下翻转行，再沿主对角线转置
fn rotate(matrix: &mut Vec<Vec<i32>>) {
    // 定义函数/方法 rotate
    let n = matrix.len(); // 把 矩阵.长度() 存入 元素个数
    for i in 0..(n / 2) {
        // 逐个取出 0 的元素（下标 i）
        matrix.swap(i, n - 1 - i); // 交换整行（等价于交换行引用）
    }
    for i in 0..n {
        // 逐个取出 0 的元素（下标 i）
        for j in 0..i {
            // 逐个取出 0 的元素（下标 j）
            let tmp = matrix[i][j]; // 把 矩阵[下标 i][下标 j] 存入 临时变量
            matrix[i][j] = matrix[j][i]; // 把 矩阵[下标 j][下标 i]; 写入 matrix[i][j]
            matrix[j][i] = tmp; // 把 临时变量; 写入 matrix[j][i]
        }
    }
}

fn eq_matrix(a: &[Vec<i32>], b: &[Vec<i32>]) -> bool {
    // 定义函数/方法 eq_matrix
    if a.len() != b.len() {
        // 若 数组.长度() 不等于 b.长度(
        return false; // 返回 false
    }
    for i in 0..a.len() {
        // 逐个取出 0 的元素（下标 i）
        if a[i] != b[i] {
            // 若 数组[下标 i] 不等于 b[下标 i]
            return false; // 返回 false
        }
    }
    true // true
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let mut cases: Vec<(Vec<Vec<i32>>, Vec<Vec<i32>>)> = vec![
        (
            vec![vec![1, 2, 3], vec![4, 5, 6], vec![7, 8, 9]],
            vec![vec![7, 4, 1], vec![8, 5, 2], vec![9, 6, 3]],
        ),
        (
            vec![
                vec![5, 1, 9, 11],
                vec![2, 4, 8, 10],
                vec![13, 3, 6, 7],
                vec![15, 14, 12, 16],
            ],
            vec![
                vec![15, 13, 2, 5],
                vec![14, 3, 4, 1],
                vec![12, 6, 8, 9],
                vec![16, 7, 10, 11],
            ],
        ),
    ];
    for (idx, (input, expected)) in cases.iter_mut().enumerate() {
        rotate(input); // rotate(input);
        assert!(eq_matrix(input, expected), "case {} failed", idx); // 断言校验
    }
    println!("PASS"); // 全部用例通过，输出 PASS
}
