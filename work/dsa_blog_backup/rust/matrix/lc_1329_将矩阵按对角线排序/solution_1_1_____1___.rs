// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145381786
// LeetCode 1329. 将矩阵按对角线排序 — Rust 版
use std::collections::{HashMap, VecDeque}; // 引入依赖

// 方案1：模拟 —— 按 r-c 分组收集对角线，升序排序后按 shift（取队首）写回
fn diagonal_sort(mat: &mut Vec<Vec<i32>>) {
    // 定义函数/方法 diagonal_sort
    let rows = mat.len(); // 把 mat.长度() 存入 行数
    let cols = mat[0].len(); // 把 mat[0].长度() 存入 列数
    let mut diags: HashMap<i32, VecDeque<i32>> = HashMap::new();
    for r in 0..rows {
        // 逐个取出 0 的元素（右指针）
        for c in 0..cols {
            // 逐个取出 0 的元素（字符）
            diags // diags
                .entry(r as i32 - c as i32) // entry(右指针 as i32 减 字符 as i32)
                .or_default() // or_default()
                .push_back(mat[r][c]); // 追加 mat[右指针][字符]);
        }
    }
    for arr in diags.values_mut() {
        // 逐个取出 diags 的元素（数组）
        let mut v: Vec<i32> = arr.drain(..).collect(); // 把 数组.drain(..).collect(); 写入 let mut v: Vec<i32>
        v.sort(); // 排序
        *arr = v.into();
    }
    for r in 0..rows {
        // 逐个取出 0 的元素（右指针）
        for c in 0..cols {
            // 逐个取出 0 的元素（字符）
            mat[r][c] = diags // 把 diags 写入 mat[r][c]
                .get_mut(&(r as i32 - c as i32)) // get_mut( 按位与 (右指针 as i32 减 字符 as i32))
                .unwrap() // unwrap()
                .pop_front() // pop_front()
                .unwrap(); // unwrap();
        }
    }
}

fn main() {
    // 程序入口：跑内嵌自测用例
    // 与 TS 事实源内嵌用例一致
    let mut m = vec![vec![3, 3, 1, 1], vec![2, 2, 1, 2], vec![1, 1, 1, 2]];
    let exp = vec![vec![1, 1, 1, 1], vec![1, 2, 2, 2], vec![1, 2, 3, 3]];
    diagonal_sort(&mut m); // diagonal_sort( 按位与 mut 映射表);
    assert_eq!(m, exp, "FAILED: got {:?}", m); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
