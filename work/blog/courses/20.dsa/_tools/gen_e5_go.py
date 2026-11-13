import os

base337 = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa/go/dp/lc_337_打家劫舍_iii"
base417 = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa/go/graph/lc_417_太平洋大西洋水流问题"
base123 = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa/go/dp/lc_123_买卖股票的最佳时机_iii"

# ---- lc_337 (2 go files) ----
go337 = '''package main

import ("fmt"; "os")

type TreeNode struct {
    val         int
    left, right *TreeNode
}

func rob(root *TreeNode) int {
    st := dfs(root)
    if st[0] > st[1] {
        return st[0]
    }
    return st[1]
}

func dfs(node *TreeNode) [2]int {
    if node == nil {
        return [2]int{0, 0}
    }
    l := dfs(node.left)
    r := dfs(node.right)
    selected := node.val + l[1] + r[1]
    notSelected := max(l[0], l[1]) + max(r[0], r[1])
    return [2]int{selected, notSelected}
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func main() {
    ok := true
    if rob(nil) != 0 {
        ok = false
        fmt.Println("FAIL nil")
    }
    single := &TreeNode{val: 5}
    if rob(single) != 5 {
        ok = false
        fmt.Println("FAIL single")
    }
    root := &TreeNode{val: 3, left: &TreeNode{val: 2, right: &TreeNode{val: 3}}, right: &TreeNode{val: 3, right: &TreeNode{val: 1}}}
    if rob(root) != 7 {
        ok = false
        fmt.Println("FAIL demo")
    }
    if !ok {
        os.Exit(1)
    }
    fmt.Println("PASS")
}
'''

for fn in ["solution_1_1_____1___________.go", "solution_2_2_____2______________.go"]:
    with open(os.path.join(base337, fn), "w") as f:
        f.write(go337)

# ---- lc_417 (3 go files) ----
go417 = '''package main

import ("fmt"; "os"; "reflect")

func pacificAtlantic(matrix [][]int) [][]int {
    if len(matrix) == 0 || len(matrix[0]) == 0 {
        return [][]int{}
    }
    m, n := len(matrix), len(matrix[0])
    pacific := make([][]bool, m)
    atlantic := make([][]bool, m)
    for i := 0; i < m; i++ {
        pacific[i] = make([]bool, n)
        atlantic[i] = make([]bool, n)
    }
    var dfs func(r, c int, flow [][]bool)
    dfs = func(r, c int, flow [][]bool) {
        flow[r][c] = true
        dirs := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
        for _, d := range dirs {
            nr, nc := r+d[0], c+d[1]
            if nr >= 0 && nr < m && nc >= 0 && nc < n && !flow[nr][nc] && matrix[nr][nc] >= matrix[r][c] {
                dfs(nr, nc, flow)
            }
        }
    }
    for r := 0; r < m; r++ {
        dfs(r, 0, pacific)
        dfs(r, n-1, atlantic)
    }
    for c := 0; c < n; c++ {
        dfs(0, c, pacific)
        dfs(m-1, c, atlantic)
    }
    var res [][]int
    for r := 0; r < m; r++ {
        for c := 0; c < n; c++ {
            if pacific[r][c] && atlantic[r][c] {
                res = append(res, []int{r, c})
            }
        }
    }
    return res
}

func main() {
    ok := true
    if got := pacificAtlantic(nil); !reflect.DeepEqual(got, [][]int{}) {
        ok = false
        fmt.Println("FAIL nil", got)
    }
    mat := [][]int{
        {1, 2, 2, 3, 5},
        {3, 2, 3, 4, 4},
        {2, 4, 5, 3, 1},
        {6, 7, 1, 4, 5},
        {5, 1, 1, 2, 4},
    }
    want := [][]int{{0, 4}, {1, 3}, {1, 4}, {2, 2}, {3, 0}, {3, 1}, {4, 0}}
    if got := pacificAtlantic(mat); !reflect.DeepEqual(got, want) {
        ok = false
        fmt.Println("FAIL mat", got)
    }
    if !ok {
        os.Exit(1)
    }
    fmt.Println("PASS")
}
'''

for fn in ["solution_1___1.go", "solution_2___2.go", "solution_3___3.go"]:
    with open(os.path.join(base417, fn), "w") as f:
        f.write(go417)

# ---- lc_123 (2 go files) ----
go123_1 = '''package main

import ("fmt"; "os")

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func maxProfit(prices []int) int {
    n := len(prices)
    dp := [5]int{}
    dp[1] = -prices[0]
    dp[3] = -prices[0]
    for i := 1; i < n; i++ {
        dp[1] = max(dp[1], dp[0]-prices[i])
        dp[2] = max(dp[2], dp[1]+prices[i])
        dp[3] = max(dp[3], dp[2]-prices[i])
        dp[4] = max(dp[4], dp[3]+prices[i])
    }
    return dp[4]
}

func main() {
    ok := true
    cases := []struct {
        in   []int
        want int
    }{
        {[]int{1, 2, 3}, 2},
        {[]int{3, 3, 5, 0, 0, 3, 1, 4}, 6},
        {[]int{1}, 0},
        {[]int{1, 2, 4, 2, 5, 7, 2, 4, 9, 0}, 13},
    }
    for _, c := range cases {
        if got := maxProfit(c.in); got != c.want {
            ok = false
            fmt.Printf("FAIL maxProfit(%v)=%d want %d\\n", c.in, got, c.want)
        }
    }
    if !ok {
        os.Exit(1)
    }
    fmt.Println("PASS")
}
'''

go123_2 = '''package main

import ("fmt"; "os")

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func maxProfit(prices []int) int {
    if len(prices) == 0 {
        return 0
    }
    buy1 := -prices[0]
    sell1 := 0
    buy2 := -prices[0]
    sell2 := 0
    for _, p := range prices[1:] {
        buy1 = max(buy1, -p)
        sell1 = max(sell1, buy1+p)
        buy2 = max(buy2, sell1-p)
        sell2 = max(sell2, buy2+p)
    }
    return sell2
}

func main() {
    ok := true
    cases := []struct {
        in   []int
        want int
    }{
        {[]int{3, 3, 5, 0, 0, 3, 1, 4}, 6},
        {[]int{1, 2, 3}, 2},
        {[]int{1}, 0},
        {[]int{}, 0},
    }
    for _, c := range cases {
        if got := maxProfit(c.in); got != c.want {
            ok = false
            fmt.Printf("FAIL maxProfit(%v)=%d want %d\\n", c.in, got, c.want)
        }
    }
    if !ok {
        os.Exit(1)
    }
    fmt.Println("PASS")
}
'''

with open(os.path.join(base123, "solution_1_1_____1_____.go"), "w") as f:
    f.write(go123_1)
with open(os.path.join(base123, "solution_2_2_____2_________.go"), "w") as f:
    f.write(go123_2)

print("wrote go files")
