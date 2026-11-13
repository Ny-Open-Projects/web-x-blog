// 来源：https://blog.csdn.net/tyro_java/article/details/107490876
// LeetCode 107490876. 分书和八皇后问题 — Rust 版（方案4：八皇后显式栈迭代）
fn n_queens_stack(n: usize) -> Vec<Vec<i32>> {
    // 定义函数/方法 n_queens_stack
    fn valid(x: i32, a: &[i32]) -> bool {
        // 定义函数/方法 valid
        let y = a.len() as i32 + 1; // 把 数组.长度() as i32 加 1 存入 y
        for i in 1..=a.len() as i32 {
            // 逐个取出 1 的元素（下标 i）
            let prev = a[(i - 1) as usize]; // 把 数组[(下标 i 减 1) as usize] 存入 前一个
            if x == prev || (y - i).abs() == (x - prev).abs() {
                // 若 x 等于 前一个 或 (y 减 下标 i).取绝对值 ) 等于 (x 减 前一个).取绝对值
                return false; // 返回 false
            }
        }
        true // true
    }

    let mut solutions: Vec<Vec<i32>> = vec![]; // 把 vec取反 []; 写入 let mut solutions: Vec<Vec<i32>>
    let mut stack: Vec<Vec<i32>> = vec![vec![]]; // 把 vec取反 [vec取反 []]; 写入 let mut stack: Vec<Vec<i32>>
    while let Some(a) = stack.pop() {
        // 边取边处理，取空即停
        if a.len() == n {
            // 若 数组.长度() 等于 元素个数
            solutions.push(a); // 把 数组 压入栈/数组尾部
        } else {
            // 否则
            for i in 1..=n as i32 {
                // 逐个取出 1 的元素（下标 i）
                if valid(i, &a) {
                    // 定义函数/方法 valid
                    let mut b = a.clone(); // 把 数组.clone(); 写入 let mut b
                    b.push(i); // 把 下标 i 压入栈/数组尾部
                    stack.push(b); // 把 b 压入栈/数组尾部
                }
            }
        }
    }
    solutions // solutions
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let cases: Vec<(usize, usize, Option<Vec<i32>>)> = vec![
        (8, 92, Some(vec![8, 4, 1, 3, 6, 2, 7, 5])),
        (1, 1, Some(vec![1])),
        (2, 0, None),
        (4, 2, Some(vec![3, 1, 4, 2])),
    ];
    for (idx, (n, count, first)) in cases.iter().enumerate() {
        // for (idx, (元素个数, 计数, first)) in cases.iter().enumerate() {
        let sols = n_queens_stack(*n); // 把 n_queens_stack( 乘 元素个数) 存入 sols
        assert_eq!(sols.len(), *count, "case {} count mismatch", idx); // 断言校验
        if let Some(w) = first {
            // 若 let Some(权重) 赋值为 first
            assert_eq!(&sols[0], w, "case {} first mismatch", idx); // 断言校验
        }
    }
    println!("PASS"); // 全部用例通过，输出 PASS
}
