// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/112548608
// LeetCode 112548608. 计算思维之经典农夫过河问题C++实现（DFS 求任一可行过河序列）
fn invalid(st: &[i32; 4]) -> bool {
    // 定义函数/方法 invalid
    let (h, w, s, v) = (st[0], st[1], st[2], st[3]); // 把 (st[0], st[1], st[2], st[3]); 写入 let (h, w, s, v)
    if h != s && s == w {
        // 若 h 不等于 字符串 且 字符串 等于 权重
        return true; // 返回 true
    }
    if h != s && s == v {
        // 若 h 不等于 字符串 且 字符串 等于 值
        return true; // 返回 true
    }
    false // false
}

const ROLES: [char; 4] = ['-', 'W', 'S', 'V']; // 把 [' 减 ', 'W', 'S', 'V']; 写入 const ROLES: [char; 4]
const ROLE_IDX: [usize; 4] = [0, 1, 2, 3]; // '-'->0 占位, W->1, S->2, V->3

fn solve_farmer() -> Vec<char> {
    // 定义函数/方法 solve_farmer
    let mut path: Vec<char> = vec![]; // 把 vec取反 []; 写入 let mut path: Vec<char>
    let mut visited: std::collections::HashSet<[i32; 4]> = std::collections::HashSet::new();

    fn go(
        st: [i32; 4],
        visited: &mut std::collections::HashSet<[i32; 4]>,
        path: &mut Vec<char>,
    ) -> bool {
        // 定义函数/方法 go
        if st == [1, 1, 1, 1] {
            // 若 st 等于 [1, 1, 1, 1]
            return true; // 返回 true
        }
        if visited.contains(&st) {
            // 若 已访问集合 是否包含 按位与 st
            return false; // 返回 false
        }
        visited.insert(st); // 已访问集合 插入 st);
        for ri in 0..4usize {
            // 逐个取出 0 的元素（ri）
            let mut ns = st; // 把 st; 写入 let mut ns
            ns[0] = 1 - ns[0]; // 农夫总是过河
            if ri != 0 {
                // 若 ri 不等于 0
                let idx = ROLE_IDX[ri]; // 把 ROLE_IDX[ri] 存入 idx
                                        // 农夫必须与所带物品在出发前同岸
                if st[0] != st[idx] {
                    // 若 st[0] 不等于 st[idx]
                    continue; // 跳过本轮，进入下一次
                }
                ns[idx] = 1 - ns[idx]; // 把 1 减 ns[idx]; 写入 ns[idx]
            }
            if invalid(&ns) {
                // 定义函数/方法 invalid
                continue; // 跳过本轮，进入下一次
            }
            if go(ns, visited, path) {
                // 定义函数/方法 go
                path.push(ROLES[ri]); // 把 ROLES[ri] 压入栈/数组尾部
                return true; // 返回 true
            }
        }
        false // false
    }

    go([0, 0, 0, 0], &mut visited, &mut path); // go([0, 0, 0, 0], 按位与 mut 已访问集合, 按位与 mut 当前路径);
    path.reverse(); // 反转
    path // 当前路径
}

// 模拟走 path，校验每步合法且终点为 (1,1,1,1)
fn simulate(path: &[char]) -> bool {
    // 定义函数/方法 simulate
    let mut st = [0i32; 4]; // 把 [0i32; 4]; 写入 let mut st
    for &role in path {
        // for 按位与 role in 当前路径 {
        let before = st; // 把 st 存入 before
        st[0] = 1 - st[0]; // 把 1 减 st[0]; 写入 st[0]
        if role != '-' {
            // 若 role 不等于 ' 减 '
            let idx = match role {
                // 把 match role { 存入 idx
                'W' => 1,
                'S' => 2,
                'V' => 3,
                _ => 0,
            };
            if before[0] != before[idx] {
                // 若 before[0] 不等于 before[idx]
                return false; // 返回 false
            }
            st[idx] = 1 - st[idx]; // 把 1 减 st[idx]; 写入 st[idx]
        }
        if invalid(&st) {
            // 定义函数/方法 invalid
            return false; // 返回 false
        }
    }
    st == [1, 1, 1, 1] // 把 赋值为 [1, 1, 1, 1] 写入 st
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let want_path = ['S', '-', 'W', 'S', 'V', '-', 'S']; // 把 ['S', ' 减 ', 'W', 'S', 'V', ' 减 ', 'S'] 存入 want_path
    let want_readable = "HS H HW HS HV H HS"; // 把 「HS H HW HS HV H HS」 存入 want_readable

    let got_path = solve_farmer(); // 把 solve_farmer() 存入 got_path

    // case1: 完整路径与参考实现一致
    assert_eq!(got_path.len(), want_path.len(), "path length mismatch"); // 断言校验
    for (i, (g, w)) in got_path.iter().zip(want_path.iter()).enumerate() {
        assert_eq!(g, w, "path[{}] mismatch", i); // 断言校验
    }

    // case2: 可读方案串一致
    let got_readable: String = got_path // 把 got_path 写入 let got_readable: String
        .iter() // iter()
        .map(|&r| {
            // 映射表( 按位或 按位与 右指针 按位或 {
            if r != '-' {
                // 若 右指针 不等于 ' 减 '
                format!("H{}", r) // format取反 (「H{}」, 右指针)
            } else {
                // 否则
                "H".to_string() // 「H」.to_string()
            }
        }) // })
        .collect::<Vec<_>>() // collect:: 小于 Vec 小于 _ 超过 超过 ()
        .join(" "); // 拼接为字符串
    assert_eq!(got_readable, want_readable, "readable mismatch"); // 断言校验

    // case3: 路径 7 步
    assert_eq!(got_path.len(), 7, "steps mismatch"); // 断言校验

    // case4: 模拟校验每步合法且到达终点
    assert!(simulate(&got_path), "simulate failed"); // 断言校验

    println!("PASS"); // 全部用例通过，输出 PASS
}
