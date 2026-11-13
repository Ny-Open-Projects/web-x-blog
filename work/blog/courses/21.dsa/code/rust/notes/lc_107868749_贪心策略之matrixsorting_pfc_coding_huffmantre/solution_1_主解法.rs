// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107868749
// LeetCode 107868749. 贪心策略 — Rust 版（贪心策略之 matrixSort / PFC 编码 / Huffman 树）
use std::collections::HashMap; // 引入依赖

// 每列升序排序后每行升序排序
fn matrix_sort(matrix: &mut Vec<Vec<i32>>) {
    // 定义函数/方法 matrix_sort
    if matrix.is_empty() {
        // 若 矩阵.is_empty(
        return; // return;
    }
    let rows = matrix.len(); // 把 矩阵.长度() 存入 行数
    let cols = matrix[0].len(); // 把 矩阵[0].长度() 存入 列数
    for c in 0..cols {
        // 逐个取出 0 的元素（字符）
        let mut col: Vec<i32> = matrix.iter().map(|r| r[c]).collect();
        col.sort(); // 排序
        for r in 0..rows {
            // 逐个取出 0 的元素（右指针）
            matrix[r][c] = col[r]; // 把 col[右指针]; 写入 matrix[r][c]
        }
    }
    for r in 0..rows {
        // 逐个取出 0 的元素（右指针）
        matrix[r].sort(); // 排序
    }
}

#[derive(Clone)]
enum Huff {
    // 定义类型
    Leaf {
        freq: i64,
        sym: String,
    },
    Internal {
        freq: i64,
        left: Box<Huff>,
        right: Box<Huff>,
    },
}

impl Huff {
    // 实现块
    fn freq(&self) -> i64 {
        // 定义函数/方法 freq
        match self {
            // 按情况匹配处理
            Huff::Leaf { freq, .. } => *freq,
            Huff::Internal { freq, .. } => *freq,
        }
    }
}

fn build_huffman(freqs: &[(&str, i64)]) -> Huff {
    // 定义函数/方法 build_huffman
    let mut nodes: Vec<(i64, Huff)> = freqs // 把 freqs 写入 let mut nodes: Vec<(i64, Huff)>
        .iter() // iter()
        .map(|&(k, v)| {
            (
                v,
                Huff::Leaf {
                    freq: v,
                    sym: k.to_string(),
                },
            )
        })
        .collect(); // collect();
    nodes.sort_by_key(|n| n.0); // nodes.sort_by_key( 按位或 元素个数 按位或 元素个数.0);
    while nodes.len() > 1 {
        // while nodes.长度() 超过 1 {
        let a = nodes.remove(0); // 把 nodes 弹出 0) 存入 数组
        let b = nodes.remove(0); // 把 nodes 弹出 0) 存入 b
        let merged = (
            a.0 + b.0,
            Huff::Internal {
                freq: a.0 + b.0,
                left: Box::new(a.1),
                right: Box::new(b.1),
            },
        );
        let mut i = 0; // 把 0; 写入 let mut i
        while i < nodes.len() && nodes[i].0 < merged.0 {
            // while 下标 i 小于 nodes.长度() 且 nodes[下标 i].0 小于 merged.0 {
            i += 1; // 下标 i累加 1
        }
        nodes.insert(i, merged); // nodes 插入 下标 i, merged);
    }
    nodes.remove(0).1 // nodes 弹出 0).1
}

fn huffman_codes(freqs: &[(&str, i64)]) -> HashMap<String, String> {
    // 定义函数/方法 huffman_codes
    let root = build_huffman(freqs); // 把 build_huffman(freqs) 存入 根节点
    let mut codes: HashMap<String, String> = HashMap::new(); // 把 HashMap::new(); 写入 let mut codes: HashMap<String, String>
    fn walk(node: &Huff, prefix: &str, codes: &mut HashMap<String, String>) {
        // 定义函数/方法 walk
        match node {
            // 按情况匹配处理
            Huff::Leaf { sym, .. } => {
                let code = if prefix.is_empty() {
                    "0".to_string()
                } else {
                    prefix.to_string()
                };
                codes.insert(sym.clone(), code); // codes 插入 sym.clone(), code);
            }
            Huff::Internal { left, right, .. } => {
                walk(left, &format!("{}0", prefix), codes); // walk(左边界, 按位与 format取反 (「{}0」, prefix), codes);
                walk(right, &format!("{}1", prefix), codes); // walk(右边界, 按位与 format取反 (「{}1」, prefix), codes);
            }
        }
    }
    walk(&root, "", &mut codes); // walk( 按位与 根节点, 「」, 按位与 mut codes);
    codes // codes
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let freqs = [
        ("A", 5i64),
        ("B", 9),
        ("C", 12),
        ("D", 13),
        ("E", 16),
        ("F", 45),
    ];

    // case1: matrixSort
    let mut mat = vec![vec![5, 3, 4], vec![1, 6, 2], vec![7, 9, 8]];
    matrix_sort(&mut mat); // matrix_sort( 按位与 mut mat);
    let want_mat = vec![vec![1, 2, 3], vec![4, 5, 6], vec![7, 8, 9]];
    assert_eq!(mat, want_mat, "matrixSort mismatch"); // 断言校验

    // case2: WPL
    let codes = huffman_codes(&freqs); // 把 huffman_codes( 按位与 freqs) 存入 codes
    let mut wpl = 0i64; // 把 0i64; 写入 let mut wpl
    let mut code_list: Vec<String> = vec![]; // 把 vec取反 []; 写入 let mut code_list: Vec<String>
    for &(k, v) in &freqs {
        // for 按位与 (下标 k, 值) in 按位与 freqs {
        let c = codes.get(k).unwrap(); // 把 codes 查找 下标 k).unwrap() 存入 字符
        wpl += v * c.len() as i64; // wpl累加 值 乘 字符.长度() as i64
        code_list.push(c.clone()); // 把 字符.clone( 压入栈/数组尾部
    }
    assert_eq!(wpl, 224, "WPL mismatch"); // 断言校验

    // case3: 前缀无关
    let mut prefix_free = true; // 把 true; 写入 let mut prefix_free
    for i in 0..code_list.len() {
        // 逐个取出 0 的元素（下标 i）
        for j in 0..code_list.len() {
            // 逐个取出 0 的元素（下标 j）
            if i != j && code_list[j].starts_with(&code_list[i]) {
                prefix_free = false; // 把 false; 写入 prefix_free
            }
        }
    }
    assert!(prefix_free, "codes not prefix-free"); // 断言校验

    println!("PASS"); // 全部用例通过，输出 PASS
}
