// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134859971
// LeetCode 2050. 并行课程III — Rust 版（方案1）
fn minimum_time(n: i32, relations: Vec<Vec<i32>>, time: Vec<i32>) -> i32 {
    // 定义函数/方法 minimum_time
    use std::collections::HashMap; // 引入依赖
    let mut next: HashMap<i32, Vec<i32>> = HashMap::new(); // 把 HashMap::new(); 写入 let mut next: HashMap<i32, Vec<i32>>
    let mut indeg = vec![0i32; (n + 1) as usize]; // 把 vec取反 [0i32; (元素个数 加 1) as usize]; 写入 let mut indeg
    for r in &relations {
        // 逐个取出 relations 的元素（右指针）
        next.entry(r[0]).or_default().push(r[1]); // 把 右指针[1] 压入栈/数组尾部
        indeg[r[1] as usize] += 1; // 把 1; 写入 indeg[r[1] as usize] +
    }
    let mut finish = vec![0i32; (n + 1) as usize]; // 把 vec取反 [0i32; (元素个数 加 1) as usize]; 写入 let mut finish
    let mut queue: Vec<i32> = (1..=n).filter(|&c| indeg[c as usize] == 0).collect();
    let mut total = 0; // 把 0; 写入 let mut total
    while !queue.is_empty() {
        // while 取反 队列 是否为空 {
        let mut nq = Vec::new(); // 把 Vec::new(); 写入 let mut nq
        for &c in &queue {
            // for 按位与 字符 in 按位与 队列 {
            finish[c as usize] += time[(c - 1) as usize]; // 把 time[(字符 减 1) as usize]; 写入 finish[c as usize] +
            total = total.max(finish[c as usize]); // 把 总和.取较大值 finish[字符 as usize]); 写入 总和
            for &nx in next.get(&c).unwrap_or(&vec![]) {
                // for 按位与 nx in 下一个 查找 按位与 字符).unwrap_or( 按位与 vec取反 []) {
                finish[nx as usize] = finish[nx as usize].max(finish[c as usize]);
                indeg[nx as usize] -= 1; // 把 1; 写入 indeg[nx as usize] -
                if indeg[nx as usize] == 0 {
                    nq.push(nx);
                } // 若 indeg[nx as usize] 等于 0 { nq 追加 nx); }
            }
        }
        queue = nq; // 把 nq; 写入 队列
    }
    total // 总和
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(
        minimum_time(3, vec![vec![1, 3], vec![2, 3]], vec![3, 2, 5]),
        8
    ); // 断言校验
    assert_eq!(
        minimum_time(
            5,
            vec![vec![1, 2], vec![2, 3], vec![3, 4], vec![4, 5]],
            vec![1, 2, 3, 4, 5]
        ),
        15
    ); // 断言校验
    assert_eq!(minimum_time(1, vec![], vec![5]), 5); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
