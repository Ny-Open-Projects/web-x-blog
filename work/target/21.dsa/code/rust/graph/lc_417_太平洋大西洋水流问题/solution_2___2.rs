// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133982215
// LeetCode 417. 太平洋大西洋水流问题 — Rust 版

// 方案2（DFS 反向流动，从海洋边界出发）
fn pacific_atlantic(matrix: Option<&Vec<Vec<i32>>>) -> Vec<(usize, usize)> {
    // 定义函数/方法 pacific_atlantic
    let matrix = match matrix {
        // 把 match 矩阵 { 存入 矩阵
        Some(m) if !m.is_empty() && !m[0].is_empty() => m,
        _ => return Vec::new(),
    };
    let m = matrix.len(); // 把 矩阵.长度() 存入 映射表
    let n = matrix[0].len(); // 把 矩阵[0].长度() 存入 元素个数
    let mut pacific = vec![vec![false; n]; m]; // 把 vec取反 [vec取反 [false; 元素个数]; 映射表]; 写入 let mut pacific
    let mut atlantic = vec![vec![false; n]; m]; // 把 vec取反 [vec取反 [false; 元素个数]; 映射表]; 写入 let mut atlantic

    fn dfs(matrix: &Vec<Vec<i32>>, flow: &mut Vec<Vec<bool>>, r: usize, c: usize) {
        // 定义函数/方法 dfs
        let (m, n) = (matrix.len(), matrix[0].len()); // 把 (矩阵.长度(), 矩阵[0].长度()); 写入 let (m, n)
        flow[r][c] = true; // 把 true; 写入 flow[r][c]
        let dirs: [(i64, i64); 4] = [(-1, 0), (1, 0), (0, -1), (0, 1)];
        for (dr, dc) in dirs {
            // for (dr, dc) in dirs {
            let nr = r as i64 + dr; // 把 右指针 as i64 加 dr 存入 nr
            let nc = c as i64 + dc; // 把 字符 as i64 加 dc 存入 nc
            if nr >= 0  // 若 nr 不低于 0
                && (nr as usize) < m  // 且 (nr as usize) 小于 映射表
                && nc >= 0  // 把 0 写入 && nc >
                && (nc as usize) < n  // 且 (nc as usize) 小于 元素个数
                && !flow[nr as usize][nc as usize]  // 且 取反 flow[nr as usize][nc as usize]
                && matrix[nr as usize][nc as usize] >= matrix[r][c]
            // 把 矩阵[右指针][字符] 写入 && matrix[nr as usize][nc as usize] >
            {
                dfs(matrix, flow, nr as usize, nc as usize); // dfs(矩阵, flow, nr as usize, nc as usize);
            }
        }
    }

    for r in 0..m {
        // 逐个取出 0 的元素（右指针）
        dfs(matrix, &mut pacific, r, 0); // dfs(矩阵, 按位与 mut pacific, 右指针, 0);
        dfs(matrix, &mut atlantic, r, n - 1); // dfs(矩阵, 按位与 mut atlantic, 右指针, 元素个数 减 1);
    }
    for c in 0..n {
        // 逐个取出 0 的元素（字符）
        dfs(matrix, &mut pacific, 0, c); // dfs(矩阵, 按位与 mut pacific, 0, 字符);
        dfs(matrix, &mut atlantic, m - 1, c); // dfs(矩阵, 按位与 mut atlantic, 映射表 减 1, 字符);
    }

    let mut res: Vec<(usize, usize)> = Vec::new(); // 把 Vec::new(); 写入 let mut res: Vec<(usize, usize)>
    for r in 0..m {
        // 逐个取出 0 的元素（右指针）
        for c in 0..n {
            // 逐个取出 0 的元素（字符）
            if pacific[r][c] && atlantic[r][c] {
                // 若 pacific[右指针][字符] 且 atlantic[右指针][字符]
                res.push((r, c)); // 把 (右指针, 字符 压入栈/数组尾部
            }
        }
    }
    res // 结果
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let matrix = vec![
        vec![1, 2, 2, 3, 5],
        vec![3, 2, 3, 4, 4],
        vec![2, 4, 5, 3, 1],
        vec![6, 7, 1, 4, 5],
        vec![5, 1, 1, 2, 4],
    ];
    let got = pacific_atlantic(Some(&matrix)); // 把 pacific_atlantic(Some( 按位与 矩阵)) 存入 got
    let expected: [(usize, usize); 7] = [(0, 4), (1, 3), (1, 4), (2, 2), (3, 0), (3, 1), (4, 0)];
    assert_eq!(got.len(), expected.len(), "length mismatch"); // 断言校验
    for (i, (g, e)) in got.iter().zip(expected.iter()).enumerate() {
        assert_eq!(g, e, "cell mismatch at {}", i); // 断言校验
    }
    println!("PASS"); // 全部用例通过，输出 PASS
}
