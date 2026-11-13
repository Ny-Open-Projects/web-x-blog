// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134859412
// LeetCode 1494. 并行课程II — Rust 版（方案2）
fn min_number_of_semesters(n: i32, relations: Vec<Vec<i32>>, k: i32) -> i32 {
    // 定义函数/方法 min_number_of_semesters
    let mut prereq = vec![0i32; n as usize]; // 把 vec取反 [0i32; 元素个数 as usize]; 写入 let mut prereq
    for r in &relations {
        // 逐个取出 relations 的元素（右指针）
        prereq[(r[1] - 1) as usize] |= 1 << ((r[0] - 1) as i32);
    }
    use std::collections::HashMap; // 引入依赖
    let mut memo: HashMap<i32, i32> = HashMap::new(); // 把 HashMap::new(); 写入 let mut memo: HashMap<i32, i32>
    fn go(
        done: i32,
        n: i32,
        k: i32,
        prereq: &[i32],
        memo: &mut std::collections::HashMap<i32, i32>,
    ) -> i32 {
        // 定义函数/方法 go
        if done == (1i32 << n) - 1 {
            return 0;
        } // 若 done 等于 (1i32 小于 小于 元素个数) 减 1 { return 0; }
        if let Some(&v) = memo.get(&done) {
            return v;
        } // 若 let Some( 按位与 值) 赋值为 记忆化表 查找 按位与 done) { return 值; }
        let mut avail = 0i32; // 把 0i32; 写入 let mut avail
        for i in 0..n {
            // 逐个取出 0 的元素（下标 i）
            if done & (1 << i) == 0 && (done & prereq[i as usize]) == prereq[i as usize] {
                avail |= 1 << i;
            }
        }
        // 枚举 avail 的所有 k 子集（简化：取最低 k 位）
        let mut cnt = 0; // 把 0; 写入 let mut cnt
        let mut chosen = 0i32; // 把 0i32; 写入 let mut chosen
        let mut a = avail; // 把 avail; 写入 let mut a
        while a != 0 && cnt < k {
            // 把 0 且 计数 小于 下标 k { 写入 while a !
            let low = a & (-a); // 把 数组 按位与 ( 减 数组) 存入 low
            chosen |= low; // 把 low; 写入 chosen |
            a ^= low; // 把 low; 写入 a ^
            cnt += 1; // 计数累加 1
        }
        let r = 1 + go(done | chosen, n, k, prereq, memo); // 把 1 加 go(done 按位或 chosen, 元素个数, 下标 k, prereq, 记忆化表) 存入 右指针
        memo.insert(done, r); // 记忆化表 插入 done, 右指针);
        r // 右指针
    }
    go(0, n, k, &prereq, &mut memo) // go(0, 元素个数, 下标 k, 按位与 prereq, 按位与 mut 记忆化表)
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(
        min_number_of_semesters(4, vec![vec![2, 1], vec![3, 1], vec![1, 4]], 2),
        3
    ); // 断言校验
    assert_eq!(
        min_number_of_semesters(5, vec![vec![2, 1], vec![3, 1], vec![4, 1], vec![1, 5]], 3),
        3
    ); // 断言校验
    assert_eq!(min_number_of_semesters(3, vec![], 2), 2); // 断言校验
    assert_eq!(
        min_number_of_semesters(4, vec![vec![1, 2], vec![2, 3]], 1),
        4
    ); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
