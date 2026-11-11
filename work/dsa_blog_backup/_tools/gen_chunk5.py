import json, os, re, subprocess, sys, shutil

BASE = "/Users/Wang/Code/webfault-ai/dsa"
PROGRESS = os.path.join(BASE, "_tools/scale_progress_chunk5.json")

# SOL[lc][lang] = full source text (already a self-asserting, runnable file)
SOL = {}

def add(lc, **kw):
    SOL.setdefault(lc, {})
    for lang, code in kw.items():
        SOL[lc][lang] = code

# ---------------------------------------------------------------------------
# runtimes
GOBIN = "/usr/local/go1.26.5/bin/go"
JAVAC = "/Library/Java/JavaVirtualMachines/jdk-12.jdk/Contents/Home/bin/javac"
JAVA = "/Library/Java/JavaVirtualMachines/jdk-12.jdk/Contents/Home/bin/java"
TS = "/Users/Wang/.workbuddy/binaries/node/versions/22.22.2-6/bin/node --experimental-strip-types"

def run_go(path):
    env = os.environ.copy()
    env["GO111MODULE"] = "off"
    return subprocess.run([GOBIN, "run", path], capture_output=True, text=True, cwd=BASE, env=env)

def run_java(path):
    d = "/tmp/jout_" + str(os.getpid()) + "_" + re.sub(r'[^a-zA-Z0-9]', '', path)[-20:]
    os.makedirs(d, exist_ok=True)
    c = subprocess.run([JAVAC, "-d", d, path], capture_output=True, text=True)
    if c.returncode != 0:
        return c
    cls = "com.webfault.dsa.Main"
    return subprocess.run([JAVA, "-cp", d, cls], capture_output=True, text=True)

def run_ts(path):
    return subprocess.run(TS.split() + [path], capture_output=True, text=True, cwd=BASE)

def verify(path):
    lang = path.split(".")[-1]
    if lang == "go":
        r = run_go(path)
    elif lang == "java":
        r = run_java(path)
    else:
        r = run_ts(path)
    ok = (r.returncode == 0) and ("PASS" in r.stdout)
    return ok, r

def load_progress():
    done = {}
    if os.path.exists(PROGRESS):
        with open(PROGRESS) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                    done[rec["rel"]] = rec["status"]
                except Exception:
                    pass
    return done

def record(rel, status, note):
    with open(PROGRESS, "a") as f:
        f.write(json.dumps({"rel": rel, "status": status, "note": note}) + "\n")

# ============================ BATCH 1 ============================
# lc_509 fib
add("lc_509",
go='''package main
import ("fmt";"os")
func fib(n int) int {
    if n < 2 { return n }
    a, b := 0, 1
    for i := 2; i <= n; i++ { a, b = b, a+b }
    return b
}
func main() {
    cases := []struct{ in int; want int }{{0,0},{1,1},{2,1},{10,55}}
    ok := true
    for _, c := range cases {
        if got := fib(c.in); got != c.want { ok=false; fmt.Printf("FAIL fib(%v)=%v want %v\\n", c.in, got, c.want) }
    }
    if !ok { os.Exit(1) }
    fmt.Println("PASS")
}''',
java='''package com.webfault.dsa;
class Main {
    static int fib(int n) {
        if (n < 2) return n;
        int a = 0, b = 1;
        for (int i = 2; i <= n; i++) { int t = b; b = a + b; a = t; }
        return b;
    }
    public static void main(String[] args) {
        int[] ins = {0,1,2,10}; int[] wants = {0,1,1,55};
        boolean ok = true;
        for (int i = 0; i < ins.length; i++) {
            int got = fib(ins[i]);
            if (got != wants[i]) { ok = false; System.out.println("FAIL fib("+ins[i]+")="+got+" want "+wants[i]); }
        }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}''',
ts='''export function demo(): void {
    function fib(n: number): number {
        if (n < 2) return n;
        let a = 0, b = 1;
        for (let i = 2; i <= n; i++) { const t = b; b = a + b; a = t; }
        return b;
    }
    const cases = [{ in: 0, want: 0 }, { in: 1, want: 1 }, { in: 2, want: 1 }, { in: 10, want: 55 }];
    let fail = false;
    for (const c of cases) {
        const got = fib(c.in);
        if (got !== c.want) { fail = true; console.log("FAIL fib(" + c.in + ")=" + got + " want " + c.want); }
    }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();''')

# lc_674 findLengthOfLCIS
add("lc_674",
java='''package com.webfault.dsa;
class Main {
    static int findLengthOfLCIS(int[] nums) {
        if (nums.length == 0) return 0;
        int best = 1, cur = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[i-1]) cur++; else cur = 1;
            if (cur > best) best = cur;
        }
        return best;
    }
    public static void main(String[] args) {
        int[][] ins = {{1,3,5,4,7},{2,2,2,2,2},{1,3,5}}; int[] wants = {3,1,3};
        boolean ok = true;
        for (int i = 0; i < ins.length; i++) {
            int got = findLengthOfLCIS(ins[i]);
            if (got != wants[i]) { ok = false; System.out.println("FAIL "+got+" want "+wants[i]); }
        }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}''',
ts='''export function demo(): void {
    function findLengthOfLCIS(nums: number[]): number {
        if (nums.length === 0) return 0;
        let best = 1, cur = 1;
        for (let i = 1; i < nums.length; i++) {
            if (nums[i] > nums[i-1]) cur++; else cur = 1;
            if (cur > best) best = cur;
        }
        return best;
    }
    const cases = [{ in: [1,3,5,4,7], want: 3 }, { in: [2,2,2,2,2], want: 1 }, { in: [1,3,5], want: 3 }];
    let fail = false;
    for (const c of cases) {
        const got = findLengthOfLCIS(c.in);
        if (got !== c.want) { fail = true; console.log("FAIL " + got + " want " + c.want); }
    }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();''')

# lc_122 maxProfit (greedy)
add("lc_122",
ts='''export function demo(): void {
    function maxProfit(prices: number[]): number {
        let best = 0;
        for (let i = 1; i < prices.length; i++) {
            if (prices[i] > prices[i-1]) best += prices[i] - prices[i-1];
        }
        return best;
    }
    const cases = [{ in: [7,1,5,3,6,4], want: 7 }, { in: [1,2,3,4,5], want: 4 }, { in: [7,6,4,3,1], want: 0 }];
    let fail = false;
    for (const c of cases) {
        const got = maxProfit(c.in);
        if (got !== c.want) { fail = true; console.log("FAIL " + got + " want " + c.want); }
    }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();''')

# lc_213 rob II
add("lc_213",
go='''package main
import ("fmt";"os")
func rob(nums []int) int {
    n := len(nums)
    if n == 0 { return 0 }
    if n == 1 { return nums[0] }
    return max(helper(nums,0,n-2), helper(nums,1,n-1))
}
func helper(nums []int, l, r int) int {
    prev, cur := 0, 0
    for i := l; i <= r; i++ { prev, cur = cur, max(cur, prev+nums[i]) }
    return cur
}
func max(a, b int) int { if a > b { return a }; return b }
func main() {
    cases := []struct{ in []int; want int }{
        {[]int{2,3,2},3},{[]int{1,2,3,1},4},{[]int{1,2,1,1},3},
    }
    ok := true
    for _, c := range cases {
        if got := rob(c.in); got != c.want { ok=false; fmt.Printf("FAIL rob=%v want %v\\n", got, c.want) }
    }
    if !ok { os.Exit(1) }
    fmt.Println("PASS")
}''',
ts='''export function demo(): void {
    function helper(nums: number[], l: number, r: number): number {
        let prev = 0, cur = 0;
        for (let i = l; i <= r; i++) { const t = cur; cur = Math.max(cur, prev + nums[i]); prev = t; }
        return cur;
    }
    function rob(nums: number[]): number {
        const n = nums.length;
        if (n === 0) return 0;
        if (n === 1) return nums[0];
        return Math.max(helper(nums,0,n-2), helper(nums,1,n-1));
    }
    const cases = [{ in: [2,3,2], want: 3 }, { in: [1,2,3,1], want: 4 }, { in: [1,2,1,1], want: 3 }];
    let fail = false;
    for (const c of cases) {
        const got = rob(c.in);
        if (got !== c.want) { fail = true; console.log("FAIL " + got + " want " + c.want); }
    }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();''')

# lc_877 stoneGame
add("lc_877",
go='''package main
import ("fmt";"os")
func stoneGame(piles []int) bool {
    n := len(piles)
    dp := make([][]int, n)
    for i := range dp { dp[i] = make([]int, n) }
    for i := 0; i < n; i++ { dp[i][i] = piles[i] }
    for l := 2; l <= n; l++ {
        for i := 0; i <= n-l; i++ {
            j := i + l - 1
            a := piles[i] - dp[i+1][j]
            b := piles[j] - dp[i][j-1]
            if a > b { dp[i][j] = a } else { dp[i][j] = b }
        }
    }
    return dp[0][n-1] > 0
}
func main() {
    cases := []struct{ in []int; want bool }{
        {[]int{5,3,4,5},true},{[]int{3,9,1,2},true},{[]int{1,2},true},
    }
    ok := true
    for _, c := range cases {
        if got := stoneGame(c.in); got != c.want { ok=false; fmt.Printf("FAIL stoneGame=%v want %v\\n", got, c.want) }
    }
    if !ok { os.Exit(1) }
    fmt.Println("PASS")
}''')

# lc_605 canPlaceFlowers
add("lc_605",
go='''package main
import ("fmt";"os")
func canPlaceFlowers(bed []int, n int) bool {
    m := len(bed)
    for i := 0; i < m; i++ {
        if bed[i] == 0 && (i == 0 || bed[i-1] == 0) && (i == m-1 || bed[i+1] == 0) {
            bed[i] = 1; n--
        }
    }
    return n <= 0
}
func main() {
    cases := []struct{ bed []int; n int; want bool }{
        {[]int{1,0,0,0,1},1,true},{[]int{1,0,0,0,1},2,false},{[]int{0,0,1,0,0},1,true},
    }
    ok := true
    for _, c := range cases {
        if got := canPlaceFlowers(c.bed, c.n); got != c.want { ok=false; fmt.Printf("FAIL=%v want %v\\n", got, c.want) }
    }
    if !ok { os.Exit(1) }
    fmt.Println("PASS")
}''',
java='''package com.webfault.dsa;
class Main {
    static boolean canPlaceFlowers(int[] bed, int n) {
        int m = bed.length;
        for (int i = 0; i < m; i++) {
            if (bed[i] == 0 && (i == 0 || bed[i-1] == 0) && (i == m-1 || bed[i+1] == 0)) {
                bed[i] = 1; n--;
            }
        }
        return n <= 0;
    }
    public static void main(String[] args) {
        int[][] a = {{1,0,0,0,1},{1,0,0,0,1},{0,0,1,0,0}}; int[] ns = {1,2,1}; boolean[] ws = {true,false,true};
        boolean ok = true;
        for (int i = 0; i < a.length; i++) {
            boolean got = canPlaceFlowers(a[i], ns[i]);
            if (got != ws[i]) { ok = false; System.out.println("FAIL "+got+" want "+ws[i]); }
        }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}''',
ts='''export function demo(): void {
    function canPlaceFlowers(bed: number[], n: number): boolean {
        const m = bed.length;
        for (let i = 0; i < m; i++) {
            if (bed[i] === 0 && (i === 0 || bed[i-1] === 0) && (i === m-1 || bed[i+1] === 0)) {
                bed[i] = 1; n--;
            }
        }
        return n <= 0;
    }
    const cases = [{ bed: [1,0,0,0,1], n: 1, want: true }, { bed: [1,0,0,0,1], n: 2, want: false }, { bed: [0,0,1,0,0], n: 1, want: true }];
    let fail = false;
    for (const c of cases) {
        const got = canPlaceFlowers(c.bed.slice(), c.n);
        if (got !== c.want) { fail = true; console.log("FAIL " + got + " want " + c.want); }
    }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();''')

# lc_860 lemonadeChange
add("lc_860",
ts='''export function demo(): void {
    function lemonadeChange(bills: number[]): boolean {
        let f5 = 0, f10 = 0;
        for (const b of bills) {
            if (b === 5) f5++;
            else if (b === 10) { f10++; f5--; }
            else { if (f10 > 0) { f10--; f5--; } else { f5 -= 3; } }
            if (f5 < 0) return false;
        }
        return true;
    }
    const cases = [{ in: [5,5,5,10,20], want: true }, { in: [5,5,10,10,20], want: false }, { in: [5,5,5,5,20], want: true }];
    let fail = false;
    for (const c of cases) {
        const got = lemonadeChange(c.in);
        if (got !== c.want) { fail = true; console.log("FAIL " + got + " want " + c.want); }
    }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();''')

# lc_455 findContentChildren
add("lc_455",
java='''package com.webfault.dsa;
import java.util.Arrays;
class Main {
    static int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g); Arrays.sort(s);
        int i = 0, j = 0, ans = 0;
        while (i < g.length && j < s.length) {
            if (s[j] >= g[i]) { ans++; i++; j++; } else { j++; }
        }
        return ans;
    }
    public static void main(String[] args) {
        int[][] g = {{1,2,3},{1,2},{1,2,3}}; int[][] s = {{1,1},{1,2,3},{3}}; int[] ws = {1,2,1};
        boolean ok = true;
        for (int i = 0; i < g.length; i++) {
            int got = findContentChildren(g[i], s[i]);
            if (got != ws[i]) { ok = false; System.out.println("FAIL "+got+" want "+ws[i]); }
        }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}''')

# lc_977 sortedSquares
add("lc_977",
java='''package com.webfault.dsa;
import java.util.Arrays;
class Main {
    static int[] sortedSquares(int[] nums) {
        int n = nums.length; int[] res = new int[n]; int i = 0, j = n-1, k = n-1;
        while (i <= j) {
            int a = nums[i]*nums[i], b = nums[j]*nums[j];
            if (a > b) { res[k] = a; i++; } else { res[k] = b; j--; }
            k--;
        }
        return res;
    }
    public static void main(String[] args) {
        int[][] ins = {{-4,-1,0,3,10},{1,2,3},{-7,-3,2,3,11}};
        int[][] ws = {{0,1,9,16,100},{1,4,9},{4,9,9,49,121}};
        boolean ok = true;
        for (int i = 0; i < ins.length; i++) {
            int[] got = sortedSquares(ins[i]);
            if (!Arrays.equals(got, ws[i])) { ok = false; System.out.println("FAIL "+Arrays.toString(got)); }
        }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}''')

# lc_922 sortArrayByParityII
add("lc_922",
go='''package main
import ("fmt";"os")
func sortArrayByParityII(nums []int) []int {
    n := len(nums); res := make([]int, n); e, o := 0, 1
    for _, v := range nums {
        if v%2 == 0 { res[e] = v; e += 2 } else { res[o] = v; o += 2 }
    }
    return res
}
func eqMultiset(a, b []int) bool {
    if len(a) != len(b) { return false }
    ca, cb := map[int]int{}, map[int]int{}
    for _, v := range a { ca[v]++ }
    for _, v := range b { cb[v]++ }
    for k, v := range ca { if cb[k] != v { return false } }
    return true
}
func validParity(a, src []int) bool {
    if len(a) != len(src) { return false }
    if !eqMultiset(a, src) { return false }
    for i, v := range a {
        if i%2 == 0 && v%2 != 0 { return false }
        if i%2 == 1 && v%2 == 0 { return false }
    }
    return true
}
func main() {
    cases := [][]int{{4,2,5,7},{2,3},{1,2,3,4}}
    ok := true
    for _, c := range cases {
        if !validParity(sortArrayByParityII(c), c) { ok=false; fmt.Printf("FAIL parity %v\\n", c) }
    }
    if !ok { os.Exit(1) }
    fmt.Println("PASS")
}''',
java='''package com.webfault.dsa;
import java.util.*;
class Main {
    static int[] sortArrayByParityII(int[] nums) {
        int n = nums.length; int[] res = new int[n]; int e = 0, o = 1;
        for (int v : nums) { if (v%2 == 0) { res[e] = v; e += 2; } else { res[o] = v; o += 2; } }
        return res;
    }
    static boolean validParity(int[] a, int[] src) {
        if (a.length != src.length) return false;
        Map<Integer,Integer> ca = new HashMap<>(), cb = new HashMap<>();
        for (int v : a) ca.put(v, ca.getOrDefault(v,0)+1);
        for (int v : src) cb.put(v, cb.getOrDefault(v,0)+1);
        if (!ca.equals(cb)) return false;
        for (int i = 0; i < a.length; i++) {
            if (i%2 == 0 && a[i]%2 != 0) return false;
            if (i%2 == 1 && a[i]%2 == 0) return false;
        }
        return true;
    }
    public static void main(String[] args) {
        int[][] ins = {{4,2,5,7},{2,3},{1,2,3,4}};
        boolean ok = true;
        for (int[] c : ins) { if (!validParity(sortArrayByParityII(c), c)) { ok = false; System.out.println("FAIL "+Arrays.toString(c)); } }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}''',
ts='''export function demo(): void {
    function sortArrayByParityII(nums: number[]): number[] {
        const n = nums.length; const res = new Array(n); let e = 0, o = 1;
        for (const v of nums) { if (v % 2 === 0) { res[e] = v; e += 2; } else { res[o] = v; o += 2; } }
        return res;
    }
    function validParity(a: number[], src: number[]): boolean {
        if (a.length !== src.length) return false;
        const ca: Record<number, number> = {}, cb: Record<number, number> = {};
        for (const v of a) ca[v] = (ca[v] || 0) + 1;
        for (const v of src) cb[v] = (cb[v] || 0) + 1;
        for (const k in ca) if (ca[k] !== cb[k]) return false;
        for (let i = 0; i < a.length; i++) {
            if (i % 2 === 0 && a[i] % 2 !== 0) return false;
            if (i % 2 === 1 && a[i] % 2 === 0) return false;
        }
        return true;
    }
    const cases = [[4,2,5,7],[2,3],[1,2,3,4]];
    let fail = false;
    for (const c of cases) {
        if (!validParity(sortArrayByParityII(c), c)) { fail = true; console.log("FAIL " + c); }
    }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();''')

# lc_89 grayCode
add("lc_89",
go='''package main
import ("fmt";"os")
func grayCode(n int) []int {
    res := make([]int, 1<<n)
    for i := 0; i < (1<<n); i++ { res[i] = i ^ (i >> 1) }
    return res
}
func main() {
    cases := []struct{ in int; want []int }{
        {0,[]int{0}},{1,[]int{0,1}},{2,[]int{0,1,3,2}},
    }
    ok := true
    for _, c := range cases {
        got := grayCode(c.in)
        if len(got) != len(c.want) { ok=false; fmt.Printf("FAIL len\\n"); continue }
        for i := range got { if got[i] != c.want[i] { ok=false; fmt.Printf("FAIL grayCode(%v)=%v want %v\\n", c.in, got, c.want); break } }
    }
    if !ok { os.Exit(1) }
    fmt.Println("PASS")
}''',
java='''package com.webfault.dsa;
import java.util.Arrays;
class Main {
    static int[] grayCode(int n) {
        int[] res = new int[1<<n];
        for (int i = 0; i < (1<<n); i++) res[i] = i ^ (i >> 1);
        return res;
    }
    public static void main(String[] args) {
        int[] ins = {0,1,2}; int[][] ws = {{0},{0,1},{0,1,3,2}};
        boolean ok = true;
        for (int i = 0; i < ins.length; i++) {
            int[] got = grayCode(ins[i]);
            if (!Arrays.equals(got, ws[i])) { ok = false; System.out.println("FAIL "+Arrays.toString(got)); }
        }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}''',
ts='''export function demo(): void {
    function grayCode(n: number): number[] {
        const res = new Array(1 << n);
        for (let i = 0; i < (1 << n); i++) res[i] = i ^ (i >> 1);
        return res;
    }
    const cases = [{ in: 0, want: [0] }, { in: 1, want: [0,1] }, { in: 2, want: [0,1,3,2] }];
    let fail = false;
    for (const c of cases) {
        const got = grayCode(c.in);
        if (got.length !== c.want.length || got.some((v, i) => v !== c.want[i])) { fail = true; console.log("FAIL " + got); }
    }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();''')

# lc_134217002 seqSearch
add("lc_134217002",
go='''package main
import ("fmt";"os")
func seqSearch(arr []int, target int) int {
    for i, v := range arr { if v == target { return i } }
    return -1
}
func main() {
    cases := []struct{ arr []int; t int; want int }{
        {[]int{1,2,3},1,0},{[]int{1,2,3},3,2},{[]int{1,2,3},5,-1},
    }
    ok := true
    for _, c := range cases {
        if got := seqSearch(c.arr, c.t); got != c.want { ok=false; fmt.Printf("FAIL=%v want %v\\n", got, c.want) }
    }
    if !ok { os.Exit(1) }
    fmt.Println("PASS")
}''',
java='''package com.webfault.dsa;
class Main {
    static int seqSearch(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++) if (arr[i] == target) return i;
        return -1;
    }
    public static void main(String[] args) {
        int[][] a = {{1,2,3},{1,2,3},{1,2,3}}; int[] t = {1,3,5}; int[] ws = {0,2,-1};
        boolean ok = true;
        for (int i = 0; i < a.length; i++) {
            int got = seqSearch(a[i], t[i]);
            if (got != ws[i]) { ok = false; System.out.println("FAIL "+got+" want "+ws[i]); }
        }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}''',
ts='''export function demo(): void {
    function seqSearch(arr: number[], target: number): number {
        for (let i = 0; i < arr.length; i++) if (arr[i] === target) return i;
        return -1;
    }
    const cases = [{ arr: [1,2,3], t: 1, want: 0 }, { arr: [1,2,3], t: 3, want: 2 }, { arr: [1,2,3], t: 5, want: -1 }];
    let fail = false;
    for (const c of cases) {
        const got = seqSearch(c.arr, c.t);
        if (got !== c.want) { fail = true; console.log("FAIL " + got + " want " + c.want); }
    }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();''')

# lc_2042 areNumbersAscending
add("lc_2042",
go='''package main
import ("fmt";"os")
func areNumbersAscending(s string) bool {
    prev := -1
    for i := 0; i < len(s); {
        if s[i] >= '0' && s[i] <= '9' {
            num := 0
            for i < len(s) && s[i] >= '0' && s[i] <= '9' { num = num*10 + int(s[i]-'0'); i++ }
            if prev >= num { return false }
            prev = num
        } else { i++ }
    }
    return true
}
func main() {
    cases := []struct{ in string; want bool }{
        {"a 1 b 2 c 3",true},{"a 3 b 2",false},{"abc",true},
    }
    ok := true
    for _, c := range cases {
        if got := areNumbersAscending(c.in); got != c.want { ok=false; fmt.Printf("FAIL=%v want %v\\n", got, c.want) }
    }
    if !ok { os.Exit(1) }
    fmt.Println("PASS")
}''')

# lc_326 isPowerOfThree
add("lc_326",
go='''package main
import ("fmt";"os")
func isPowerOfThree(n int) bool {
    if n <= 0 { return false }
    for n%3 == 0 { n /= 3 }
    return n == 1
}
func main() {
    cases := []struct{ in int; want bool }{
        {1,true},{0,false},{9,true},{2,false},{27,true},
    }
    ok := true
    for _, c := range cases {
        if got := isPowerOfThree(c.in); got != c.want { ok=false; fmt.Printf("FAIL=%v want %v\\n", got, c.want) }
    }
    if !ok { os.Exit(1) }
    fmt.Println("PASS")
}''')

# lc_217 containsDuplicate
add("lc_217",
ts='''export function demo(): void {
    function containsDuplicate(nums: number[]): boolean {
        const seen = new Set<number>();
        for (const v of nums) { if (seen.has(v)) return true; seen.add(v); }
        return false;
    }
    const cases = [{ in: [1,2,3], want: false }, { in: [1,2,2], want: true }, { in: [0], want: false }];
    let fail = false;
    for (const c of cases) {
        const got = containsDuplicate(c.in);
        if (got !== c.want) { fail = true; console.log("FAIL " + got + " want " + c.want); }
    }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();''')

# lc_165 compareVersion
add("lc_165",
go='''package main
import ("fmt";"os";"strconv";"strings")
func compareVersion(v1, v2 string) int {
    a := strings.Split(v1, ".")
    b := strings.Split(v2, ".")
    n := len(a); if len(b) > n { n = len(b) }
    for i := 0; i < n; i++ {
        x, y := 0, 0
        if i < len(a) { x, _ = strconv.Atoi(a[i]) }
        if i < len(b) { y, _ = strconv.Atoi(b[i]) }
        if x > y { return 1 }
        if x < y { return -1 }
    }
    return 0
}
func main() {
    cases := []struct{ a, b string; want int }{
        {"1.01","1.001",0},{"1.0","1.0.0",0},{"0.1","1.1",-1},{"1.0.1","1",1},
    }
    ok := true
    for _, c := range cases {
        if got := compareVersion(c.a, c.b); got != c.want { ok=false; fmt.Printf("FAIL=%v want %v\\n", got, c.want) }
    }
    if !ok { os.Exit(1) }
    fmt.Println("PASS")
}''',
ts='''export function demo(): void {
    function compareVersion(v1: string, v2: string): number {
        const a = v1.split("."), b = v2.split(".");
        const n = Math.max(a.length, b.length);
        for (let i = 0; i < n; i++) {
            const x = i < a.length ? parseInt(a[i]) : 0;
            const y = i < b.length ? parseInt(b[i]) : 0;
            if (x > y) return 1;
            if (x < y) return -1;
        }
        return 0;
    }
    const cases = [{ a: "1.01", b: "1.001", want: 0 }, { a: "1.0", b: "1.0.0", want: 0 }, { a: "0.1", b: "1.1", want: -1 }, { a: "1.0.1", b: "1", want: 1 }];
    let fail = false;
    for (const c of cases) {
        const got = compareVersion(c.a, c.b);
        if (got !== c.want) { fail = true; console.log("FAIL " + got + " want " + c.want); }
    }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();''')

# lc_209 minSubArrayLen
add("lc_209",
go='''package main
import ("fmt";"os")
func minSubArrayLen(target int, nums []int) int {
    l, best, sum := 0, len(nums)+1, 0
    for r := 0; r < len(nums); r++ {
        sum += nums[r]
        for sum >= target {
            if r-l+1 < best { best = r-l+1 }
            sum -= nums[l]; l++
        }
    }
    if best == len(nums)+1 { return 0 }
    return best
}
func main() {
    cases := []struct{ t int; nums []int; want int }{
        {7,[]int{2,3,1,2,4,3},2},{4,[]int{1,4,4},1},{11,[]int{1,1,1,1,1,1,1,1},0},
    }
    ok := true
    for _, c := range cases {
        if got := minSubArrayLen(c.t, c.nums); got != c.want { ok=false; fmt.Printf("FAIL=%v want %v\\n", got, c.want) }
    }
    if !ok { os.Exit(1) }
    fmt.Println("PASS")
}''',
java='''package com.webfault.dsa;
class Main {
    static int minSubArrayLen(int target, int[] nums) {
        int l = 0, best = nums.length + 1, sum = 0;
        for (int r = 0; r < nums.length; r++) {
            sum += nums[r];
            while (sum >= target) {
                if (r - l + 1 < best) best = r - l + 1;
                sum -= nums[l++];
            }
        }
        return best == nums.length + 1 ? 0 : best;
    }
    public static void main(String[] args) {
        int[] t = {7,4,11}; int[][] n = {{2,3,1,2,4,3},{1,4,4},{1,1,1,1,1,1,1,1}}; int[] ws = {2,1,0};
        boolean ok = true;
        for (int i = 0; i < t.length; i++) {
            int got = minSubArrayLen(t[i], n[i]);
            if (got != ws[i]) { ok = false; System.out.println("FAIL "+got+" want "+ws[i]); }
        }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}''',
ts='''export function demo(): void {
    function minSubArrayLen(target: number, nums: number[]): number {
        let l = 0, best = nums.length + 1, sum = 0;
        for (let r = 0; r < nums.length; r++) {
            sum += nums[r];
            while (sum >= target) {
                if (r - l + 1 < best) best = r - l + 1;
                sum -= nums[l++];
            }
        }
        return best === nums.length + 1 ? 0 : best;
    }
    const cases = [{ t: 7, nums: [2,3,1,2,4,3], want: 2 }, { t: 4, nums: [1,4,4], want: 1 }, { t: 11, nums: [1,1,1,1,1,1,1,1], want: 0 }];
    let fail = false;
    for (const c of cases) {
        const got = minSubArrayLen(c.t, c.nums);
        if (got !== c.want) { fail = true; console.log("FAIL " + got + " want " + c.want); }
    }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();''')

# lc_164 maximumGap
add("lc_164",
go='''package main
import ("fmt";"os")
func maximumGap(nums []int) int {
    if len(nums) < 2 { return 0 }
    minv, maxv := nums[0], nums[0]
    for _, v := range nums { if v < minv { minv = v }; if v > maxv { maxv = v } }
    if minv == maxv { return 0 }
    n := len(nums)
    bucketSize := (maxv - minv) / (n - 1); if bucketSize < 1 { bucketSize = 1 }
    bucketCount := (maxv - minv) / bucketSize + 1
    bMin := make([]int, bucketCount); bMax := make([]int, bucketCount); has := make([]bool, bucketCount)
    for _, v := range nums {
        idx := (v - minv) / bucketSize
        if !has[idx] { bMin[idx] = v; bMax[idx] = v; has[idx] = true } else {
            if v < bMin[idx] { bMin[idx] = v }
            if v > bMax[idx] { bMax[idx] = v }
        }
    }
    ans, prev := 0, minv
    for i := 0; i < bucketCount; i++ {
        if !has[i] { continue }
        if bMin[i] - prev > ans { ans = bMin[i] - prev }
        prev = bMax[i]
    }
    return ans
}
func main() {
    cases := []struct{ in []int; want int }{
        {[]int{3,6,9,1},3},{[]int{10},0},{[]int{1,10000000},9999999},
    }
    ok := true
    for _, c := range cases {
        if got := maximumGap(c.in); got != c.want { ok=false; fmt.Printf("FAIL=%v want %v\\n", got, c.want) }
    }
    if !ok { os.Exit(1) }
    fmt.Println("PASS")
}''',
java='''package com.webfault.dsa;
class Main {
    static int maximumGap(int[] nums) {
        if (nums.length < 2) return 0;
        int minv = nums[0], maxv = nums[0];
        for (int v : nums) { if (v < minv) minv = v; if (v > maxv) maxv = v; }
        if (minv == maxv) return 0;
        int n = nums.length;
        int bs = (maxv - minv) / (n - 1); if (bs < 1) bs = 1;
        int bc = (maxv - minv) / bs + 1;
        int[] bMin = new int[bc]; int[] bMax = new int[bc]; boolean[] has = new boolean[bc];
        for (int v : nums) {
            int idx = (v - minv) / bs;
            if (!has[idx]) { bMin[idx] = v; bMax[idx] = v; has[idx] = true; }
            else { if (v < bMin[idx]) bMin[idx] = v; if (v > bMax[idx]) bMax[idx] = v; }
        }
        int ans = 0, prev = minv;
        for (int i = 0; i < bc; i++) {
            if (!has[i]) continue;
            if (bMin[i] - prev > ans) ans = bMin[i] - prev;
            prev = bMax[i];
        }
        return ans;
    }
    public static void main(String[] args) {
        int[][] ins = {{3,6,9,1},{10},{1,10000000}}; int[] ws = {3,0,9999999};
        boolean ok = true;
        for (int i = 0; i < ins.length; i++) {
            int got = maximumGap(ins[i]);
            if (got != ws[i]) { ok = false; System.out.println("FAIL "+got+" want "+ws[i]); }
        }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}''',
ts='''export function demo(): void {
    function maximumGap(nums: number[]): number {
        if (nums.length < 2) return 0;
        let minv = nums[0], maxv = nums[0];
        for (const v of nums) { if (v < minv) minv = v; if (v > maxv) maxv = v; }
        if (minv === maxv) return 0;
        const n = nums.length;
        let bs = Math.floor((maxv - minv) / (n - 1)); if (bs < 1) bs = 1;
        const bc = Math.floor((maxv - minv) / bs) + 1;
        const bMin = new Array(bc), bMax = new Array(bc); const has = new Array(bc).fill(false);
        for (const v of nums) {
            const idx = Math.floor((v - minv) / bs);
            if (!has[idx]) { bMin[idx] = v; bMax[idx] = v; has[idx] = true; }
            else { if (v < bMin[idx]) bMin[idx] = v; if (v > bMax[idx]) bMax[idx] = v; }
        }
        let ans = 0, prev = minv;
        for (let i = 0; i < bc; i++) {
            if (!has[i]) continue;
            if (bMin[i] - prev > ans) ans = bMin[i] - prev;
            prev = bMax[i];
        }
        return ans;
    }
    const cases = [{ in: [3,6,9,1], want: 3 }, { in: [10], want: 0 }, { in: [1,10000000], want: 9999999 }];
    let fail = false;
    for (const c of cases) {
        const got = maximumGap(c.in);
        if (got !== c.want) { fail = true; console.log("FAIL " + got + " want " + c.want); }
    }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();''')

# lc_72 minDistance
add("lc_72",
go='''package main
import ("fmt";"os")
func minDistance(w1, w2 string) int {
    m, n := len(w1), len(w2)
    dp := make([][]int, m+1)
    for i := range dp { dp[i] = make([]int, n+1) }
    for i := 0; i <= m; i++ { dp[i][0] = i }
    for j := 0; j <= n; j++ { dp[0][j] = j }
    for i := 1; i <= m; i++ {
        for j := 1; j <= n; j++ {
            cost := 1; if w1[i-1] == w2[j-1] { cost = 0 }
            dp[i][j] = min3(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+cost)
        }
    }
    return dp[m][n]
}
func min3(a, b, c int) int { x := a; if b < x { x = b }; if c < x { x = c }; return x }
func main() {
    cases := []struct{ a, b string; want int }{
        {"horse","ros",3},{"intention","execution",5},{"","" ,0},
    }
    ok := true
    for _, c := range cases {
        if got := minDistance(c.a, c.b); got != c.want { ok=false; fmt.Printf("FAIL=%v want %v\\n", got, c.want) }
    }
    if !ok { os.Exit(1) }
    fmt.Println("PASS")
}''',
java='''package com.webfault.dsa;
class Main {
    static int minDistance(String w1, String w2) {
        int m = w1.length(), n = w2.length();
        int[][] dp = new int[m+1][n+1];
        for (int i = 0; i <= m; i++) dp[i][0] = i;
        for (int j = 0; j <= n; j++) dp[0][j] = j;
        for (int i = 1; i <= m; i++)
            for (int j = 1; j <= n; j++) {
                int cost = w1.charAt(i-1) == w2.charAt(j-1) ? 0 : 1;
                dp[i][j] = Math.min(dp[i-1][j]+1, Math.min(dp[i][j-1]+1, dp[i-1][j-1]+cost));
            }
        return dp[m][n];
    }
    public static void main(String[] args) {
        String[] a = {"horse","intention",""}; String[] b = {"ros","execution",""}; int[] ws = {3,5,0};
        boolean ok = true;
        for (int i = 0; i < a.length; i++) {
            int got = minDistance(a[i], b[i]);
            if (got != ws[i]) { ok = false; System.out.println("FAIL "+got+" want "+ws[i]); }
        }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}''')

# lc_1027 longestArithSeqLength
add("lc_1027",
go='''package main
import ("fmt";"os")
func longestArithSeqLength(nums []int) int {
    n := len(nums)
    if n <= 2 { return n }
    best := 2
    dp := make([]map[int]int, n)
    for i := range dp { dp[i] = map[int]int{} }
    for i := 1; i < n; i++ {
        for j := 0; j < i; j++ {
            d := nums[i] - nums[j]
            v := 2
            if dp[j][d] > 0 { v = dp[j][d] + 1 }
            if dp[i][d] < v { dp[i][d] = v }
            if dp[i][d] > best { best = dp[i][d] }
        }
    }
    return best
}
func main() {
    cases := []struct{ in []int; want int }{
        {[]int{9,4,7,2,10},3},{[]int{20,1,15,3,10,5,8},4},{[]int{3,6,9,12},4},
    }
    ok := true
    for _, c := range cases {
        if got := longestArithSeqLength(c.in); got != c.want { ok=false; fmt.Printf("FAIL=%v want %v\\n", got, c.want) }
    }
    if !ok { os.Exit(1) }
    fmt.Println("PASS")
}''')

# ============================ BATCH 2 (linked list) ============================
LL_GO = '''type ListNode struct { Val int; Next *ListNode }
func buildList(vals []int) *ListNode {
    dummy := &ListNode{}; p := dummy
    for _, v := range vals { p.Next = &ListNode{Val: v}; p = p.Next }
    return dummy.Next
}
func toArr(head *ListNode) []int {
    res := []int{}
    for head != nil { res = append(res, head.Val); head = head.Next }
    return res
}'''

add("lc_19",
go='''package main
import ("fmt";"os";"reflect")
''' + LL_GO + '''
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    dummy := &ListNode{Next: head}
    fast, slow := dummy, dummy
    for i := 0; i < n; i++ { fast = fast.Next }
    for fast.Next != nil { fast = fast.Next; slow = slow.Next }
    slow.Next = slow.Next.Next
    return dummy.Next
}
func main() {
    cases := []struct{ in []int; n int; want []int }{
        {[]int{1,2,3,4,5},2,[]int{1,2,3,5}},
        {[]int{1},1,[]int{}},
        {[]int{1,2},2,[]int{2}},
    }
    ok := true
    for _, c := range cases {
        got := toArr(removeNthFromEnd(buildList(c.in), c.n))
        if !reflect.DeepEqual(got, c.want) { ok=false; fmt.Printf("FAIL %v\\n", got) }
    }
    if !ok { os.Exit(1) }
    fmt.Println("PASS")
}''',
java='''package com.webfault.dsa;
import java.util.Arrays;
class ListNode { int val; ListNode next; ListNode() {} ListNode(int v){val=v;} ListNode(int v, ListNode n){val=v;next=n;} }
class Main {
    static ListNode build(int[] vals){ ListNode d=new ListNode(); ListNode p=d; for(int v:vals){p.next=new ListNode(v);p=p.next;} return d.next; }
    static int[] toArr(ListNode h){ int n=0; for(ListNode x=h;x!=null;x=x.next)n++; int[] r=new int[n]; int i=0; for(;h!=null;h=h.next)r[i++]=h.val; return r; }
    static ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy=new ListNode(0); dummy.next=head; ListNode f=dummy,s=dummy;
        for(int i=0;i<n;i++) f=f.next;
        while(f.next!=null){f=f.next;s=s.next;}
        s.next=s.next.next; return dummy.next;
    }
    public static void main(String[] args) {
        int[][] ins={{1,2,3,4,5},{1},{1,2}}; int[] ns={2,1,2}; int[][] ws={{1,2,3,5},{},{2}};
        boolean ok=true;
        for(int i=0;i<ins.length;i++){ int[] got=toArr(removeNthFromEnd(build(ins[i]),ns[i])); if(!Arrays.equals(got,ws[i])){ok=false;System.out.println("FAIL "+Arrays.toString(got));} }
        if(!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}''',
ts='''export function demo(): void {
    class ListNode { val: number; next: ListNode | null; constructor(v=0,n:ListNode|null=null){this.val=v;this.next=n;} }
    function build(vals: number[]): ListNode | null { const d=new ListNode(); let p=d; for(const v of vals){p.next=new ListNode(v);p=p.next;} return d.next; }
    function toArr(h: ListNode|null): number[] { const r:number[]=[]; while(h){r.push(h.val);h=h.next;} return r; }
    function removeNthFromEnd(head: ListNode|null, n: number): ListNode|null {
        const dummy=new ListNode(0); dummy.next=head; let f=dummy,s=dummy;
        for(let i=0;i<n;i++) f=f.next!;
        while(f.next){f=f.next;s=s.next!;}
        s.next=s.next!.next; return dummy.next;
    }
    const cases = [{in:[1,2,3,4,5],n:2,want:[1,2,3,5]},{in:[1],n:1,want:[]},{in:[1,2],n:2,want:[2]}];
    let fail=false;
    for(const c of cases){ const got=toArr(removeNthFromEnd(build(c.in),c.n)); if(JSON.stringify(got)!==JSON.stringify(c.want)){fail=true;console.log("FAIL "+got);} }
    if(fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();''')

add("lc_206",
java='''package com.webfault.dsa;
import java.util.Arrays;
class ListNode { int val; ListNode next; ListNode(){} ListNode(int v){val=v;} ListNode(int v,ListNode n){val=v;next=n;} }
class Main {
    static ListNode build(int[] vals){ ListNode d=new ListNode(); ListNode p=d; for(int v:vals){p.next=new ListNode(v);p=p.next;} return d.next; }
    static int[] toArr(ListNode h){ int n=0; for(ListNode x=h;x!=null;x=x.next)n++; int[] r=new int[n]; int i=0; for(;h!=null;h=h.next)r[i++]=h.val; return r; }
    static ListNode reverseList(ListNode head){ ListNode prev=null,cur=head; while(cur!=null){ListNode nx=cur.next;cur.next=prev;prev=cur;cur=nx;} return prev; }
    public static void main(String[] args) {
        int[][] ins={{1,2,3,4,5},{},{1,2}}; int[][] ws={{5,4,3,2,1},{},{2,1}};
        boolean ok=true;
        for(int i=0;i<ins.length;i++){ int[] got=toArr(reverseList(build(ins[i]))); if(!Arrays.equals(got,ws[i])){ok=false;System.out.println("FAIL "+Arrays.toString(got));} }
        if(!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}''',
ts='''export function demo(): void {
    class ListNode { val: number; next: ListNode | null; constructor(v=0,n:ListNode|null=null){this.val=v;this.next=n;} }
    function build(vals: number[]): ListNode|null { const d=new ListNode(); let p=d; for(const v of vals){p.next=new ListNode(v);p=p.next;} return d.next; }
    function toArr(h: ListNode|null): number[] { const r:number[]=[]; while(h){r.push(h.val);h=h.next;} return r; }
    function reverseList(head: ListNode|null): ListNode|null { let prev:ListNode|null=null,cur=head; while(cur){const nx=cur.next;cur.next=prev;prev=cur;cur=nx;} return prev; }
    const cases = [{in:[1,2,3,4,5],want:[5,4,3,2,1]},{in:[],want:[]},{in:[1,2],want:[2,1]}];
    let fail=false;
    for(const c of cases){ const got=toArr(reverseList(build(c.in))); if(JSON.stringify(got)!==JSON.stringify(c.want)){fail=true;console.log("FAIL "+got);} }
    if(fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();''')

add("lc_2",
go='''package main
import ("fmt";"os")
''' + LL_GO + '''
func addTwoNumbers(l1, l2 *ListNode) *ListNode {
    dummy := &ListNode{}; p := dummy; carry := 0
    for l1 != nil || l2 != nil || carry != 0 {
        s := carry
        if l1 != nil { s += l1.Val; l1 = l1.Next }
        if l2 != nil { s += l2.Val; l2 = l2.Next }
        carry = s / 10
        p.Next = &ListNode{Val: s % 10}; p = p.Next
    }
    return dummy.Next
}
func main() {
    cases := []struct{ a, b, want []int }{
        {[]int{2,4,3},[]int{5,6,4},[]int{7,0,8}},
        {[]int{0},[]int{0},[]int{0}},
        {[]int{9,9,9,9},[]int{9,9,9},[]int{8,9,9,0,1}},
    }
    ok := true
    for _, c := range cases {
        got := toArr(addTwoNumbers(buildList(c.a), buildList(c.b)))
        if !reflect.DeepEqual(got, c.want) { ok=false; fmt.Printf("FAIL %v\\n", got) }
    }
    if !ok { os.Exit(1) }
    fmt.Println("PASS")
}''',
java='''package com.webfault.dsa;
import java.util.Arrays;
class ListNode { int val; ListNode next; ListNode(){} ListNode(int v){val=v;} ListNode(int v,ListNode n){val=v;next=n;} }
class Main {
    static ListNode build(int[] vals){ ListNode d=new ListNode(); ListNode p=d; for(int v:vals){p.next=new ListNode(v);p=p.next;} return d.next; }
    static int[] toArr(ListNode h){ int n=0; for(ListNode x=h;x!=null;x=x.next)n++; int[] r=new int[n]; int i=0; for(;h!=null;h=h.next)r[i++]=h.val; return r; }
    static ListNode addTwoNumbers(ListNode l1, ListNode l2){
        ListNode d=new ListNode(); ListNode p=d; int carry=0;
        while(l1!=null||l2!=null||carry!=0){ int s=carry; if(l1!=null){s+=l1.val;l1=l1.next;} if(l2!=null){s+=l2.val;l2=l2.next;} carry=s/10; p.next=new ListNode(s%10); p=p.next; }
        return d.next;
    }
    public static void main(String[] args) {
        int[][] a={{2,4,3},{0},{9,9,9,9}}; int[][] b={{5,6,4},{0},{9,9,9}}; int[][] w={{7,0,8},{0},{8,9,9,0,1}};
        boolean ok=true;
        for(int i=0;i<a.length;i++){ int[] got=toArr(addTwoNumbers(build(a[i]),build(b[i]))); if(!Arrays.equals(got,w[i])){ok=false;System.out.println("FAIL "+Arrays.toString(got));} }
        if(!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}''')

add("lc_83",
java='''package com.webfault.dsa;
import java.util.Arrays;
class ListNode { int val; ListNode next; ListNode(){} ListNode(int v){val=v;} ListNode(int v,ListNode n){val=v;next=n;} }
class Main {
    static ListNode build(int[] vals){ ListNode d=new ListNode(); ListNode p=d; for(int v:vals){p.next=new ListNode(v);p=p.next;} return d.next; }
    static int[] toArr(ListNode h){ int n=0; for(ListNode x=h;x!=null;x=x.next)n++; int[] r=new int[n]; int i=0; for(;h!=null;h=h.next)r[i++]=h.val; return r; }
    static ListNode deleteDuplicates(ListNode head){ if(head==null)return null; ListNode cur=head; while(cur.next!=null){ if(cur.next.val==cur.val)cur.next=cur.next.next; else cur=cur.next; } return head; }
    public static void main(String[] args) {
        int[][] ins={{1,1,2},{1,1,2,3,3},{1,1,1}}; int[][] ws={{1,2},{1,2,3},{1}};
        boolean ok=true;
        for(int i=0;i<ins.length;i++){ int[] got=toArr(deleteDuplicates(build(ins[i]))); if(!Arrays.equals(got,ws[i])){ok=false;System.out.println("FAIL "+Arrays.toString(got));} }
        if(!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}''',
ts='''export function demo(): void {
    class ListNode { val: number; next: ListNode | null; constructor(v=0,n:ListNode|null=null){this.val=v;this.next=n;} }
    function build(vals: number[]): ListNode|null { const d=new ListNode(); let p=d; for(const v of vals){p.next=new ListNode(v);p=p.next;} return d.next; }
    function toArr(h: ListNode|null): number[] { const r:number[]=[]; while(h){r.push(h.val);h=h.next;} return r; }
    function deleteDuplicates(head: ListNode|null): ListNode|null { if(!head)return null; let cur=head; while(cur.next){ if(cur.next.val===cur.val)cur.next=cur.next.next; else cur=cur.next; } return head; }
    const cases=[{in:[1,1,2],want:[1,2]},{in:[1,1,2,3,3],want:[1,2,3]},{in:[1,1,1],want:[1]}];
    let fail=false;
    for(const c of cases){ const got=toArr(deleteDuplicates(build(c.in))); if(JSON.stringify(got)!==JSON.stringify(c.want)){fail=true;console.log("FAIL "+got);} }
    if(fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();''')

add("lc_21",
go='''package main
import ("fmt";"os")
''' + LL_GO + '''
func mergeTwoLists(l1, l2 *ListNode) *ListNode {
    dummy := &ListNode{}; p := dummy
    for l1 != nil && l2 != nil {
        if l1.Val <= l2.Val { p.Next = l1; l1 = l1.Next } else { p.Next = l2; l2 = l2.Next }
        p = p.Next
    }
    if l1 != nil { p.Next = l1 } else { p.Next = l2 }
    return dummy.Next
}
func main() {
    cases := []struct{ a, b, want []int }{
        {[]int{1,2,4},[]int{1,3,4},[]int{1,1,2,3,4,4}},
        {[]int{},[]int{},[]int{}},
        {[]int{1},[]int{},[]int{1}},
    }
    ok := true
    for _, c := range cases {
        got := toArr(mergeTwoLists(buildList(c.a), buildList(c.b)))
        if !reflect.DeepEqual(got, c.want) { ok=false; fmt.Printf("FAIL %v\\n", got) }
    }
    if !ok { os.Exit(1) }
    fmt.Println("PASS")
}''')

add("lc_148",
go='''package main
import ("fmt";"os")
''' + LL_GO + '''
func sortList(head *ListNode) *ListNode {
    if head == nil || head.Next == nil { return head }
    slow, fast := head, head
    for fast.Next != nil && fast.Next.Next != nil { slow = slow.Next; fast = fast.Next.Next }
    mid := slow.Next; slow.Next = nil
    left := sortList(head); right := sortList(mid)
    dummy := &ListNode{}; p := dummy
    for left != nil && right != nil {
        if left.Val <= right.Val { p.Next = left; left = left.Next } else { p.Next = right; right = right.Next }
        p = p.Next
    }
    if left != nil { p.Next = left } else { p.Next = right }
    return dummy.Next
}
func main() {
    cases := []struct{ in, want []int }{
        {[]int{4,2,1,3},[]int{1,2,3,4}},
        {[]int{},[]int{}},
        {[]int{-1,5,3,4,0},[]int{-1,0,3,4,5}},
    }
    ok := true
    for _, c := range cases {
        got := toArr(sortList(buildList(c.in)))
        if !reflect.DeepEqual(got, c.want) { ok=false; fmt.Printf("FAIL %v\\n", got) }
    }
    if !ok { os.Exit(1) }
    fmt.Println("PASS")
}''',
java='''package com.webfault.dsa;
import java.util.Arrays;
class ListNode { int val; ListNode next; ListNode(){} ListNode(int v){val=v;} ListNode(int v,ListNode n){val=v;next=n;} }
class Main {
    static ListNode build(int[] vals){ ListNode d=new ListNode(); ListNode p=d; for(int v:vals){p.next=new ListNode(v);p=p.next;} return d.next; }
    static int[] toArr(ListNode h){ int n=0; for(ListNode x=h;x!=null;x=x.next)n++; int[] r=new int[n]; int i=0; for(;h!=null;h=h.next)r[i++]=h.val; return r; }
    static ListNode sortList(ListNode head){
        if(head==null||head.next==null)return head;
        ListNode slow=head,fast=head; while(fast.next!=null&&fast.next.next!=null){slow=slow.next;fast=fast.next.next;}
        ListNode mid=slow.next; slow.next=null;
        ListNode l=sortList(head), r=sortList(mid);
        ListNode d=new ListNode(), p=d;
        while(l!=null&&r!=null){ if(l.val<=r.val){p.next=l;l=l.next;}else{p.next=r;r=r.next;} p=p.next; }
        p.next = l!=null?l:r; return d.next;
    }
    public static void main(String[] args) {
        int[][] ins={{4,2,1,3},{},{-1,5,3,4,0}}; int[][] ws={{1,2,3,4},{},{-1,0,3,4,5}};
        boolean ok=true;
        for(int i=0;i<ins.length;i++){ int[] got=toArr(sortList(build(ins[i]))); if(!Arrays.equals(got,ws[i])){ok=false;System.out.println("FAIL "+Arrays.toString(got));} }
        if(!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}''',
ts='''export function demo(): void {
    class ListNode { val: number; next: ListNode | null; constructor(v=0,n:ListNode|null=null){this.val=v;this.next=n;} }
    function build(vals: number[]): ListNode|null { const d=new ListNode(); let p=d; for(const v of vals){p.next=new ListNode(v);p=p.next;} return d.next; }
    function toArr(h: ListNode|null): number[] { const r:number[]=[]; while(h){r.push(h.val);h=h.next;} return r; }
    function sortList(head: ListNode|null): ListNode|null {
        if(!head||!head.next)return head;
        let slow=head,fast=head; while(fast.next&&fast.next.next){slow=slow.next!;fast=fast.next.next;}
        const mid=slow.next; slow.next=null;
        const l=sortList(head), r=sortList(mid);
        const d=new ListNode(); let p=d;
        let a=l,b=r;
        while(a&&b){ if(a.val<=b.val){p.next=a;a=a.next;}else{p.next=b;b=b.next;} p=p.next; }
        p.next=a?a:b; return d.next;
    }
    const cases=[{in:[4,2,1,3],want:[1,2,3,4]},{in:[],want:[]},{in:[-1,5,3,4,0],want:[-1,0,3,4,5]}];
    let fail=false;
    for(const c of cases){ const got=toArr(sortList(build(c.in))); if(JSON.stringify(got)!==JSON.stringify(c.want)){fail=true;console.log("FAIL "+got);} }
    if(fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();''')

add("lc_23",
go='''package main
import ("fmt";"os";"reflect";"container/heap")
''' + LL_GO + '''
type Item struct { node *ListNode; idx int }
type MinHeap []Item
func (h MinHeap) Len() int { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i].node.Val < h[j].node.Val }
func (h MinHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h *MinHeap) Push(x interface{}) { *h = append(*h, x.(Item)) }
func (h *MinHeap) Pop() interface{} { old := *h; n := len(old); x := old[n-1]; *h = old[:n-1]; return x }
func mergeKLists(lists []*ListNode) *ListNode {
    h := &MinHeap{}; heap.Init(h)
    for i, l := range lists { if l != nil { heap.Push(h, Item{node: l, idx: i}) } }
    dummy := &ListNode{}; p := dummy
    for h.Len() > 0 {
        it := heap.Pop(h).(Item); p.Next = it.node; p = p.Next
        if it.node.Next != nil { heap.Push(h, Item{node: it.node.Next, idx: it.idx}) }
    }
    return dummy.Next
}
func main() {
    cases := []struct{ in [][]int; want []int }{
        {[][]int{{1,4,5},{1,3,4},{2,6}},[]int{1,1,2,3,4,4,5,6}},
        {[][]int{{}},[]int{}},
        {[][]int{{1}},[]int{1}},
    }
    ok := true
    for _, c := range cases {
        lists := make([]*ListNode, len(c.in))
        for i := range c.in { lists[i] = buildList(c.in[i]) }
        got := toArr(mergeKLists(lists))
        if !reflect.DeepEqual(got, c.want) { ok=false; fmt.Printf("FAIL %v\\n", got) }
    }
    if !ok { os.Exit(1) }
    fmt.Println("PASS")
}''',
java='''package com.webfault.dsa;
import java.util.*;
class ListNode { int val; ListNode next; ListNode(){} ListNode(int v){val=v;} ListNode(int v,ListNode n){val=v;next=n;} }
class Main {
    static int[] toArr(ListNode h){ int n=0; for(ListNode x=h;x!=null;x=x.next)n++; int[] r=new int[n]; int i=0; for(;h!=null;h=h.next)r[i++]=h.val; return r; }
    static ListNode build(int[] vals){ ListNode d=new ListNode(); ListNode p=d; for(int v:vals){p.next=new ListNode(v);p=p.next;} return d.next; }
    static ListNode mergeKLists(ListNode[] lists){
        PriorityQueue<ListNode> pq = new PriorityQueue<>((a,b)->a.val-b.val);
        for(ListNode l:lists) if(l!=null) pq.offer(l);
        ListNode d=new ListNode(), p=d;
        while(!pq.isEmpty()){ ListNode n=pq.poll(); p.next=n; p=p.next; if(n.next!=null)pq.offer(n.next); }
        return d.next;
    }
    public static void main(String[] args) {
        int[][][] ins={{{1,4,5},{1,3,4},{2,6}},{{}},{{1}}}; int[][] ws={{1,1,2,3,4,4,5,6},{},{1}};
        boolean ok=true;
        for(int i=0;i<ins.length;i++){ ListNode[] ls=new ListNode[ins[i].length]; for(int j=0;j<ins[i].length;j++)ls[j]= ins[i][j].length==0?null:build(ins[i][j]); int[] got=toArr(mergeKLists(ls)); if(!Arrays.equals(got,ws[i])){ok=false;System.out.println("FAIL "+Arrays.toString(got));} }
        if(!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}''',
ts='''export function demo(): void {
    class ListNode { val: number; next: ListNode | null; constructor(v=0,n:ListNode|null=null){this.val=v;this.next=n;} }
    function build(vals: number[]): ListNode|null { const d=new ListNode(); let p=d; for(const v of vals){p.next=new ListNode(v);p=p.next;} return d.next; }
    function toArr(h: ListNode|null): number[] { const r:number[]=[]; while(h){r.push(h.val);h=h.next;} return r; }
    function mergeKLists(lists: (ListNode|null)[]): ListNode|null {
        const pq: ListNode[] = [];
        const push=(n:ListNode)=>{ pq.push(n); pq.sort((a,b)=>a.val-b.val); };
        for(const l of lists) if(l) push(l);
        const d=new ListNode(); let p=d;
        while(pq.length){ const n=pq.shift()!; p.next=n; p=p.next!; if(n.next) push(n.next); }
        return d.next;
    }
    const cases=[{in:[[1,4,5],[1,3,4],[2,6]],want:[1,1,2,3,4,4,5,6]},{in:[[]],want:[]},{in:[[1]],want:[1]}];
    let fail=false;
    for(const c of cases){ const ls=c.in.map(x=>x.length?build(x):null); const got=toArr(mergeKLists(ls)); if(JSON.stringify(got)!==JSON.stringify(c.want)){fail=true;console.log("FAIL "+got);} }
    if(fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();''')

add("lc_141",
go='''package main
import ("fmt";"os")
''' + LL_GO + '''
func hasCycle(head *ListNode) bool {
    slow, fast := head, head
    for fast != nil && fast.Next != nil { slow = slow.Next; fast = fast.Next.Next; if slow == fast { return true } }
    return false
}
func main() {
    // acyclic
    a := buildList([]int{1,2,3}); if hasCycle(a) { fmt.Println("FAIL acyclic"); os.Exit(1) }
    // cycle: tail -> head
    b := buildList([]int{1,2,3}); p := b; for p.Next != nil { p = p.Next }; p.Next = b
    if !hasCycle(b) { fmt.Println("FAIL cycle"); os.Exit(1) }
    fmt.Println("PASS")
}''',
java='''package com.webfault.dsa;
class ListNode { int val; ListNode next; ListNode(){} ListNode(int v){val=v;} ListNode(int v,ListNode n){val=v;next=n;} }
class Main {
    static boolean hasCycle(ListNode head){ ListNode s=head,f=head; while(f!=null&&f.next!=null){s=s.next;f=f.next.next;if(s==f)return true;} return false; }
    public static void main(String[] args) {
        ListNode a=new ListNode(1); a.next=new ListNode(2); a.next.next=new ListNode(3);
        if(hasCycle(a)){System.out.println("FAIL acyclic");throw new RuntimeException("FAILED");}
        ListNode b=new ListNode(1); b.next=new ListNode(2); b.next.next=new ListNode(3); b.next.next.next=b;
        if(!hasCycle(b)){System.out.println("FAIL cycle");throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''')

add("lc_142",
ts='''export function demo(): void {
    class ListNode { val: number; next: ListNode | null; constructor(v=0,n:ListNode|null=null){this.val=v;this.next=n;} }
    function hasCycleAt(head: ListNode|null): number {
        let slow:ListNode|null=head, fast:ListNode|null=head;
        let has=false;
        while(fast&&fast.next){ slow=slow!.next; fast=fast.next.next; if(slow===fast){has=true;break;} }
        if(!has) return -1;
        slow=head; while(slow!==fast){ slow=slow!.next; fast=fast!.next; }
        let idx=0; let cur=head; while(cur!==slow){cur=cur!.next;idx++;}
        return idx;
    }
    // acyclic
    const a=new ListNode(1); a.next=new ListNode(2); a.next.next=new ListNode(3);
    if(hasCycleAt(a)!==-1){console.log("FAIL acyclic");throw new Error("FAILED");}
    // cycle at index 1 (value 2)
    const b=new ListNode(3); b.next=new ListNode(2); b.next.next=new ListNode(0); b.next.next.next=b.next;
    if(hasCycleAt(b)!==1){console.log("FAIL cycle got "+hasCycleAt(b));throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

add("lc_234",
java='''package com.webfault.dsa;
import java.util.*;
class ListNode { int val; ListNode next; ListNode(){} ListNode(int v){val=v;} ListNode(int v,ListNode n){val=v;next=n;} }
class Main {
    static boolean isPalindrome(ListNode head){
        List<Integer> vals=new ArrayList<>(); for(ListNode x=head;x!=null;x=x.next)vals.add(x.val);
        int i=0,j=vals.size()-1; while(i<j){ if(!vals.get(i).equals(vals.get(j)))return false; i++;j--; } return true;
    }
    public static void main(String[] args) {
        int[][][] ins={{{1,2,2,1}},{{1,2}},{{}},{{1}}}; boolean[] ws={true,false,true,true};
        boolean ok=true;
        for(int i=0;i<ins.length;i++){ ListNode d=new ListNode(); ListNode p=d; for(int v:ins[i][0]){p.next=new ListNode(v);p=p.next;} boolean got=isPalindrome(d.next); if(got!=ws[i]){ok=false;System.out.println("FAIL "+got);} }
        if(!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}''')

add("lc_237",
java='''package com.webfault.dsa;
import java.util.Arrays;
class ListNode { int val; ListNode next; ListNode(){} ListNode(int v){val=v;} ListNode(int v,ListNode n){val=v;next=n;} }
class Main {
    static int[] toArr(ListNode h){ int n=0; for(ListNode x=h;x!=null;x=x.next)n++; int[] r=new int[n]; int i=0; for(;h!=null;h=h.next)r[i++]=h.val; return r; }
    static ListNode build(int[] vals){ ListNode d=new ListNode(); ListNode p=d; for(int v:vals){p.next=new ListNode(v);p=p.next;} return d.next; }
    static void deleteNode(ListNode node){ node.val=node.next.val; node.next=node.next.next; }
    public static void main(String[] args) {
        int[] vals={4,5,1,9}; ListNode head=build(vals); ListNode target=head.next; deleteNode(target);
        int[] got=toArr(head); int[] want={4,1,9};
        if(!Arrays.equals(got,want)){System.out.println("FAIL "+Arrays.toString(got));throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''')

add("lc_160",
go='''package main
import ("fmt";"os")
''' + LL_GO + '''
func getIntersectionNode(headA, headB *ListNode) int {
    a, b := headA, headB
    for a != b {
        if a == nil { a = headB } else { a = a.Next }
        if b == nil { b = headA } else { b = b.Next }
    }
    if a == nil { return -1 }
    return a.Val
}
func main() {
    // intersect at value 3
    common := buildList([]int{3,4})
    a := &ListNode{Val:1}; a.Next = &ListNode{Val:2}; a.Next.Next = common
    b := &ListNode{Val:9}; b.Next = common
    if got := getIntersectionNode(a, b); got != 3 { fmt.Println("FAIL", got); os.Exit(1) }
    // disjoint
    d1 := buildList([]int{1,2}); d2 := buildList([]int{3,4})
    if got := getIntersectionNode(d1, d2); got != -1 { fmt.Println("FAIL", got); os.Exit(1) }
    fmt.Println("PASS")
}''')

add("lc_92",
go='''package main
import ("fmt";"os")
''' + LL_GO + '''
func reverseBetween(head *ListNode, left, right int) *ListNode {
    dummy := &ListNode{Next: head}
    pre := dummy
    for i := 1; i < left; i++ { pre = pre.Next }
    start := pre.Next
    then := start.Next
    for i := left; i < right; i++ {
        start.Next = then.Next
        then.Next = pre.Next
        pre.Next = then
        then = start.Next
    }
    return dummy.Next
}
func main() {
    cases := []struct{ in []int; l, r int; want []int }{
        {[]int{1,2,3,4,5},2,4,[]int{1,4,3,2,5}},
        {[]int{5},1,1,[]int{5}},
        {[]int{1,2,3,4,5},1,5,[]int{5,4,3,2,1}},
    }
    ok := true
    for _, c := range cases {
        got := toArr(reverseBetween(buildList(c.in), c.l, c.r))
        if !reflect.DeepEqual(got, c.want) { ok=false; fmt.Printf("FAIL %v\\n", got) }
    }
    if !ok { os.Exit(1) }
    fmt.Println("PASS")
}''',
java='''package com.webfault.dsa;
import java.util.Arrays;
class ListNode { int val; ListNode next; ListNode(){} ListNode(int v){val=v;} ListNode(int v,ListNode n){val=v;next=n;} }
class Main {
    static ListNode build(int[] vals){ ListNode d=new ListNode(); ListNode p=d; for(int v:vals){p.next=new ListNode(v);p=p.next;} return d.next; }
    static int[] toArr(ListNode h){ int n=0; for(ListNode x=h;x!=null;x=x.next)n++; int[] r=new int[n]; int i=0; for(;h!=null;h=h.next)r[i++]=h.val; return r; }
    static ListNode reverseBetween(ListNode head, int left, int right){
        ListNode dummy=new ListNode(0); dummy.next=head; ListNode pre=dummy;
        for(int i=1;i<left;i++) pre=pre.next;
        ListNode start=pre.next, then=start.next;
        for(int i=left;i<right;i++){ start.next=then.next; then.next=pre.next; pre.next=then; then=start.next; }
        return dummy.next;
    }
    public static void main(String[] args) {
        int[][] ins={{1,2,3,4,5},{5},{1,2,3,4,5}}; int[] ls={2,1,1}; int[] rs={4,1,5}; int[][] ws={{1,4,3,2,5},{5},{5,4,3,2,1}};
        boolean ok=true;
        for(int i=0;i<ins.length;i++){ int[] got=toArr(reverseBetween(build(ins[i]),ls[i],rs[i])); if(!Arrays.equals(got,ws[i])){ok=false;System.out.println("FAIL "+Arrays.toString(got));} }
        if(!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}''',
ts='''export function demo(): void {
    class ListNode { val: number; next: ListNode | null; constructor(v=0,n:ListNode|null=null){this.val=v;this.next=n;} }
    function build(vals: number[]): ListNode|null { const d=new ListNode(); let p=d; for(const v of vals){p.next=new ListNode(v);p=p.next;} return d.next; }
    function toArr(h: ListNode|null): number[] { const r:number[]=[]; while(h){r.push(h.val);h=h.next;} return r; }
    function reverseBetween(head: ListNode|null, left: number, right: number): ListNode|null {
        const dummy=new ListNode(0); dummy.next=head; let pre=dummy;
        for(let i=1;i<left;i++) pre=pre.next!;
        let start=pre.next!, then=start.next!;
        for(let i=left;i<right;i++){ start.next=then.next; then.next=pre.next; pre.next=then; then=start.next!; }
        return dummy.next;
    }
    const cases=[{in:[1,2,3,4,5],l:2,r:4,want:[1,4,3,2,5]},{in:[5],l:1,r:1,want:[5]},{in:[1,2,3,4,5],l:1,r:5,want:[5,4,3,2,1]}];
    let fail=false;
    for(const c of cases){ const got=toArr(reverseBetween(build(c.in),c.l,c.r)); if(JSON.stringify(got)!==JSON.stringify(c.want)){fail=true;console.log("FAIL "+got);} }
    if(fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();''')

# ============================ BATCH 3 (trees) ============================
TREE_GO = '''type TreeNode struct { Val int; Left *TreeNode; Right *TreeNode }
const NULL = -1000000000
func buildTree(vals []int) *TreeNode {
    if len(vals) == 0 || vals[0] == NULL { return nil }
    root := &TreeNode{Val: vals[0]}
    q := []*TreeNode{root}; i := 1
    for len(q) > 0 && i < len(vals) {
        node := q[0]; q = q[1:]
        if i < len(vals) && vals[i] != NULL { node.Left = &TreeNode{Val: vals[i]}; q = append(q, node.Left) }; i++
        if i < len(vals) && vals[i] != NULL { node.Right = &TreeNode{Val: vals[i]}; q = append(q, node.Right) }; i++
    }
    return root
}
func levelList(root *TreeNode) [][]int {
    if root == nil { return [][]int{} }
    res := [][]int{}; q := []*TreeNode{root}
    for len(q) > 0 {
        lvl := []int{}; n := len(q)
        for k := 0; k < n; k++ {
            node := q[0]; q = q[1:]
            lvl = append(lvl, node.Val)
            if node.Left != nil { q = append(q, node.Left) }
            if node.Right != nil { q = append(q, node.Right) }
        }
        res = append(res, lvl)
    }
    return res
}
func sameTree(a, b *TreeNode) bool {
    if a == nil && b == nil { return true }
    if a == nil || b == nil { return false }
    if a.Val != b.Val { return false }
    return sameTree(a.Left, b.Left) && sameTree(a.Right, b.Right)
}
func inorderT(root *TreeNode) []int {
    if root == nil { return []int{} }
    return append(append(inorderT(root.Left), root.Val), inorderT(root.Right)...)
}'''

TREE_JAVA = '''static class TreeNode { int val; TreeNode left; TreeNode right; TreeNode(){} TreeNode(int v){val=v;} TreeNode(int v,TreeNode l,TreeNode r){val=v;left=l;right=r;} }
    static TreeNode buildTree(Integer[] vals){
        if(vals.length==0||vals[0]==null) return null;
        TreeNode root=new TreeNode(vals[0]); java.util.LinkedList<TreeNode> q=new java.util.LinkedList<>(); q.add(root); int i=1;
        while(!q.isEmpty()&&i<vals.length){ TreeNode node=q.poll();
            if(i<vals.length&&vals[i]!=null){node.left=new TreeNode(vals[i]);q.add(node.left);} i++;
            if(i<vals.length&&vals[i]!=null){node.right=new TreeNode(vals[i]);q.add(node.right);} i++; }
        return root;
    }
    static boolean sameTree(TreeNode a, TreeNode b){ if(a==null&&b==null)return true; if(a==null||b==null)return false; if(a.val!=b.val)return false; return sameTree(a.left,b.left)&&sameTree(a.right,b.right); }
    static java.util.List<Integer> inorderT(TreeNode r){ java.util.List<Integer> l=new java.util.ArrayList<>(); if(r!=null){ l.addAll(inorderT(r.left)); l.add(r.val); l.addAll(inorderT(r.right)); } return l; }'''

TREE_TS = '''class TreeNode { val: number; left: TreeNode | null; right: TreeNode | null; constructor(v=0,l:TreeNode|null=null,r:TreeNode|null=null){this.val=v;this.left=l;this.right=r;} }
    function buildTree(vals: (number|null)[]): TreeNode | null {
        if(vals.length===0||vals[0]===null) return null;
        const root=new TreeNode(vals[0] as number); const q:TreeNode[]=[root]; let i=1;
        while(q.length&&i<vals.length){ const node=q.shift()!;
            if(i<vals.length&&vals[i]!==null){node.left=new TreeNode(vals[i] as number);q.push(node.left);} i++;
            if(i<vals.length&&vals[i]!==null){node.right=new TreeNode(vals[i] as number);q.push(node.right);} i++; }
        return root;
    }
    function levelList(root: TreeNode|null): number[][] { if(!root)return []; const res:number[][]=[]; let q:TreeNode[]=[root]; while(q.length){ const lvl:number[]=[]; const n=q.length; for(let k=0;k<n;k++){ const node=q.shift()!; lvl.push(node.val); if(node.left)q.push(node.left); if(node.right)q.push(node.right);} res.push(lvl);} return res; }
    function sameTree(a:TreeNode|null,b:TreeNode|null):boolean{ if(!a&&!b)return true; if(!a||!b)return false; if(a.val!==b.val)return false; return sameTree(a.left,b.left)&&sameTree(a.right,b.right); }
    function inorderT(root:TreeNode|null):number[]{ if(!root)return []; return [...inorderT(root.left),root.val,...inorderT(root.right)]; }'''

# ---- lc_104 maxDepth
add("lc_104",
go='''package main
import ("fmt";"os")
''' + TREE_GO + '''
func maxDepth(root *TreeNode) int {
    if root == nil { return 0 }
    return 1 + max(maxDepth(root.Left), maxDepth(root.Right))
}
func max(a, b int) int { if a > b { return a }; return b }
func main() {
    cases := []struct{ in []int; want int }{
        {[]int{3,9,20,NULL,15,7},3},
        {[]int{1,2,3,4,5,NULL,NULL,NULL,6},4},
        {[]int{},0},
    }
    ok := true
    for _, c := range cases {
        if got := maxDepth(buildTree(c.in)); got != c.want { ok=false; fmt.Printf("FAIL %v want %v\\n", got, c.want) }
    }
    if !ok { os.Exit(1) }
    fmt.Println("PASS")
}''',
ts='''export function demo(): void {
''' + TREE_TS + '''
    function maxDepth(root: TreeNode|null): number { if(!root)return 0; return 1+Math.max(maxDepth(root.left),maxDepth(root.right)); }
    const cases=[{in:[3,9,20,null,15,7],want:3},{in:[1,2,3,4,5,null,null,null,6],want:4},{in:[],want:0}];
    let fail=false;
    for(const c of cases){ const got=maxDepth(buildTree(c.in)); if(got!==c.want){fail=true;console.log("FAIL "+got);} }
    if(fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();''')

# ---- lc_111 minDepth
add("lc_111",
go='''package main
import ("fmt";"os")
''' + TREE_GO + '''
func minDepth(root *TreeNode) int {
    if root == nil { return 0 }
    if root.Left == nil { return 1 + minDepth(root.Right) }
    if root.Right == nil { return 1 + minDepth(root.Left) }
    return 1 + min(minDepth(root.Left), minDepth(root.Right))
}
func min(a, b int) int { if a < b { return a }; return b }
func main() {
    cases := []struct{ in []int; want int }{
        {[]int{3,9,20,NULL,15,7},3},
        {[]int{1,2,3,4,5,NULL,NULL,NULL,6},2},
        {[]int{},0},
    }
    ok := true
    for _, c := range cases {
        if got := minDepth(buildTree(c.in)); got != c.want { ok=false; fmt.Printf("FAIL %v want %v\\n", got, c.want) }
    }
    if !ok { os.Exit(1) }
    fmt.Println("PASS")
}''',
java='''package com.webfault.dsa;
class Main {
''' + TREE_JAVA + '''
    static int minDepth(TreeNode root){ if(root==null)return 0; if(root.left==null)return 1+minDepth(root.right); if(root.right==null)return 1+minDepth(root.left); return 1+Math.min(minDepth(root.left),minDepth(root.right)); }
    public static void main(String[] args) {
        Object[][] ins={ {3,9,20,null,15,7}, {1,2,3,4,5,null,null,null,6}, {} };
        int[] ws={2,3,0};
        // use Integer arrays
        Integer[][][] data={{{3,9,20,null,15,7}},{{1,2,3,4,5,null,null,null,6}},{{}}};
        boolean ok=true;
        Integer[] a1={3,9,20,null,15,7}; Integer[] a2={1,2,3,4,5,null,null,null,6}; Integer[] a3={};
        Integer[][] arr={a1,a2,a3}; int[] want={3,2,0};
        for(int i=0;i<arr.length;i++){ int got=minDepth(buildTree(arr[i])); if(got!=want[i]){ok=false;System.out.println("FAIL "+got);} }
        if(!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}''',
ts='''export function demo(): void {
''' + TREE_TS + '''
    function minDepth(root: TreeNode|null): number { if(!root)return 0; if(!root.left)return 1+minDepth(root.right); if(!root.right)return 1+minDepth(root.left); return 1+Math.min(minDepth(root.left),minDepth(root.right)); }
    const cases=[{in:[3,9,20,null,15,7],want:3},{in:[1,2,3,4,5,null,null,null,6],want:2},{in:[],want:0}];
    let fail=false;
    for(const c of cases){ const got=minDepth(buildTree(c.in)); if(got!==c.want){fail=true;console.log("FAIL "+got);} }
    if(fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();''')

# ---- lc_100 isSameTree
add("lc_100",
go='''package main
import ("fmt";"os")
''' + TREE_GO + '''
func isSameTree(p, q *TreeNode) bool { return sameTree(p, q) }
func main() {
    a := buildTree([]int{1,2,3}); b := buildTree([]int{1,2,3}); c := buildTree([]int{1,2,NULL})
    ok := true
    if !isSameTree(a, b) { ok=false; fmt.Println("FAIL same") }
    if isSameTree(a, c) { ok=false; fmt.Println("FAIL diff") }
    if !isSameTree(nil, nil) { ok=false; fmt.Println("FAIL nil") }
    if !ok { os.Exit(1) }
    fmt.Println("PASS")
}''',
java='''package com.webfault.dsa;
class Main {
''' + TREE_JAVA + '''
    static boolean isSameTree(TreeNode p, TreeNode q){ return sameTree(p,q); }
    public static void main(String[] args) {
        Integer[] a1={1,2,3}; Integer[] a2={1,2,3}; Integer[] a3={1,2,null};
        boolean t1=isSameTree(buildTree(a1),buildTree(a2));
        boolean t2=isSameTree(buildTree(a1),buildTree(a3));
        boolean t3=isSameTree(null,null);
        if(!(t1&&!t2&&t3)){System.out.println("FAIL");throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''',
ts='''export function demo(): void {
''' + TREE_TS + '''
    function isSameTree(p:TreeNode|null,q:TreeNode|null):boolean{ return sameTree(p,q); }
    const a=buildTree([1,2,3]), b=buildTree([1,2,3]), c=buildTree([1,2,null]);
    if(!(isSameTree(a,b)&&!isSameTree(a,c)&&isSameTree(null,null))){console.log("FAIL");throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# ---- lc_101 isSymmetric
add("lc_101",
go='''package main
import ("fmt";"os")
''' + TREE_GO + '''
func isSymmetric(root *TreeNode) bool {
    var isM func(a, b *TreeNode) bool
    isM = func(a, b *TreeNode) bool {
        if a == nil && b == nil { return true }
        if a == nil || b == nil { return false }
        return a.Val == b.Val && isM(a.Left, b.Right) && isM(a.Right, b.Left)
    }
    if root == nil { return true }
    return isM(root.Left, root.Right)
}
func main() {
    sym := buildTree([]int{1,2,2,3,4,4,3})
    nosym := buildTree([]int{1,2,2,NULL,3,NULL,3})
    ok := true
    if !isSymmetric(sym) { ok=false; fmt.Println("FAIL sym") }
    if isSymmetric(nosym) { ok=false; fmt.Println("FAIL nosym") }
    if !isSymmetric(nil) { ok=false; fmt.Println("FAIL nil") }
    if !ok { os.Exit(1) }
    fmt.Println("PASS")
}''',
java='''package com.webfault.dsa;
class Main {
''' + TREE_JAVA + '''
    static boolean isMirror(TreeNode a, TreeNode b){ if(a==null&&b==null)return true; if(a==null||b==null)return false; return a.val==b.val&&isMirror(a.left,b.right)&&isMirror(a.right,b.left); }
    static boolean isSymmetric(TreeNode root){ if(root==null)return true; return isMirror(root.left,root.right); }
    public static void main(String[] args) {
        Integer[] s={1,2,2,3,4,4,3}; Integer[] n={1,2,2,null,3,null,3};
        if(!(isSymmetric(buildTree(s))&&!isSymmetric(buildTree(n))&&isSymmetric(null))){System.out.println("FAIL");throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''',
ts='''export function demo(): void {
''' + TREE_TS + '''
    function isMirror(a:TreeNode|null,b:TreeNode|null):boolean{ if(!a&&!b)return true; if(!a||!b)return false; return a.val===b.val&&isMirror(a.left,b.right)&&isMirror(a.right,b.left); }
    function isSymmetric(root:TreeNode|null):boolean{ if(!root)return true; return isMirror(root.left,root.right); }
    const s=buildTree([1,2,2,3,4,4,3]); const n=buildTree([1,2,2,null,3,null,3]);
    if(!(isSymmetric(s)&&!isSymmetric(n)&&isSymmetric(null))){console.log("FAIL");throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# ---- lc_110 isBalanced
add("lc_110",
ts='''export function demo(): void {
''' + TREE_TS + '''
    function height(n:TreeNode|null):number{ if(!n)return 0; return 1+Math.max(height(n.left),height(n.right)); }
    function isBalanced(root:TreeNode|null):boolean{ if(!root)return true; if(Math.abs(height(root.left)-height(root.right))>1)return false; return isBalanced(root.left)&&isBalanced(root.right); }
    const a=buildTree([3,9,20,null,15,7]); const b=buildTree([1,2,2,3,3,null,null,4,4]);
    if(!(isBalanced(a)&&!isBalanced(b))){console.log("FAIL");throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# ---- lc_404 sumOfLeftLeaves
add("lc_404",
go='''package main
import ("fmt";"os")
''' + TREE_GO + '''
func sumOfLeftLeaves(root *TreeNode) int {
    if root == nil { return 0 }
    sum := 0
    if root.Left != nil && root.Left.Left == nil && root.Left.Right == nil { sum += root.Left.Val }
    sum += sumOfLeftLeaves(root.Left) + sumOfLeftLeaves(root.Right)
    return sum
}
func main() {
    // [3,9,20,null,null,15,7] left leaves: 9 + 15 = 24
    if got := sumOfLeftLeaves(buildTree([]int{3,9,20,NULL,NULL,15,7})); got != 24 { fmt.Println("FAIL", got); os.Exit(1) }
    fmt.Println("PASS")
}''')

# ---- lc_226 invertTree
add("lc_226",
java='''package com.webfault.dsa;
import java.util.Arrays;
class Main {
''' + TREE_JAVA + '''
    static TreeNode invertTree(TreeNode root){ if(root==null)return null; TreeNode t=root.left; root.left=invertTree(root.right); root.right=invertTree(t); return root; }
    public static void main(String[] args) {
        Integer[] a={4,2,7,1,3,6,9}; Integer[] w={4,7,2,9,6,3,1};
        TreeNode got=invertTree(buildTree(a)); TreeNode want=buildTree(w);
        if(!sameTree(got,want)){System.out.println("FAIL");throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''')

# ---- lc_543 diameter
add("lc_543",
go='''package main
import ("fmt";"os")
''' + TREE_GO + '''
func diameterOfBinaryTree(root *TreeNode) int {
    ans := 0
    var depth func(*TreeNode) int
    depth = func(n *TreeNode) int {
        if n == nil { return 0 }
        l, r := depth(n.Left), depth(n.Right)
        if l+r > ans { ans = l+r }
        return 1 + max(l, r)
    }
    depth(root)
    return ans
}
func max(a, b int) int { if a > b { return a }; return b }
func main() {
    if got := diameterOfBinaryTree(buildTree([]int{1,2,3,4,5})); got != 3 { fmt.Println("FAIL", got); os.Exit(1) }
    if got := diameterOfBinaryTree(buildTree([]int{})); got != 0 { fmt.Println("FAIL", got); os.Exit(1) }
    fmt.Println("PASS")
}''',
java='''package com.webfault.dsa;
class Main {
''' + TREE_JAVA + '''
    static int ans;
    static int depth(TreeNode n){ if(n==null)return 0; int l=depth(n.left),r=depth(n.right); if(l+r>ans)ans=l+r; return 1+Math.max(l,r); }
    static int diameterOfBinaryTree(TreeNode root){ ans=0; depth(root); return ans; }
    public static void main(String[] args) {
        Integer[] a={1,2,3,4,5}; Integer[] b={};
        if(diameterOfBinaryTree(buildTree(a))!=3){System.out.println("FAIL");throw new RuntimeException("FAILED");}
        if(diameterOfBinaryTree(buildTree(b))!=0){System.out.println("FAIL");throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''',
ts='''export function demo(): void {
''' + TREE_TS + '''
    let ans=0;
    function depth(n:TreeNode|null):number{ if(!n)return 0; const l=depth(n.left),r=depth(n.right); if(l+r>ans)ans=l+r; return 1+Math.max(l,r); }
    function diameterOfBinaryTree(root:TreeNode|null):number{ ans=0; depth(root); return ans; }
    if(diameterOfBinaryTree(buildTree([1,2,3,4,5]))!==3){console.log("FAIL");throw new Error("FAILED");}
    if(diameterOfBinaryTree(buildTree([]))!==0){console.log("FAIL");throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# ---- lc_98 isValidBST
add("lc_98",
go='''package main
import ("fmt";"os";"math")
''' + TREE_GO + '''
func isValidBST(root *TreeNode) bool {
    var check func(*TreeNode, int, int) bool
    check = func(n *TreeNode, lo, hi int) bool {
        if n == nil { return true }
        if n.Val <= lo || n.Val >= hi { return false }
        return check(n.Left, lo, n.Val) && check(n.Right, n.Val, hi)
    }
    return check(root, math.MinInt64, math.MaxInt64)
}
func main() {
    ok := true
    if !isValidBST(buildTree([]int{2,1,3})) { ok=false; fmt.Println("FAIL valid") }
    if isValidBST(buildTree([]int{5,1,4,NULL,NULL,3,6})) { ok=false; fmt.Println("FAIL invalid") }
    if !isValidBST(nil) { ok=false }
    if !ok { os.Exit(1) }
    fmt.Println("PASS")
}''',
ts='''export function demo(): void {
''' + TREE_TS + '''
    function isValidBST(root:TreeNode|null):boolean{
        function check(n:TreeNode|null,lo:number,hi:number):boolean{ if(!n)return true; if(n.val<=lo||n.val>=hi)return false; return check(n.left,lo,n.val)&&check(n.right,n.val,hi); }
        return check(root,-Infinity,Infinity);
    }
    if(!(isValidBST(buildTree([2,1,3]))&&!isValidBST(buildTree([5,1,4,null,null,3,6]))&&isValidBST(null))){console.log("FAIL");throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# ============================ BATCH 3 (part 2: trees) ============================
# lc_102 levelOrder
add("lc_102",
go='''package main
import ("fmt";"os";"reflect")
''' + TREE_GO + '''
func levelOrder(root *TreeNode) [][]int { return levelList(root) }
func main() {
    cases := []struct{ in []int; want [][]int }{
        {[]int{3,9,20,NULL,15,7},[][]int{{3},{9,20},{15,7}}},
        {[]int{},[][]int{}},
        {[]int{1},[][]int{{1}}},
    }
    ok := true
    for _, c := range cases {
        if got := levelOrder(buildTree(c.in)); !reflect.DeepEqual(got, c.want) { ok=false; fmt.Printf("FAIL %v\\n", got) }
    }
    if !ok { os.Exit(1) }
    fmt.Println("PASS")
}''',
java='''package com.webfault.dsa;
import java.util.*;
class Main {
''' + TREE_JAVA + '''
    static List<List<Integer>> levelOrder(TreeNode root){
        List<List<Integer>> res=new ArrayList<>(); if(root==null)return res;
        LinkedList<TreeNode> q=new LinkedList<>(); q.add(root);
        while(!q.isEmpty()){ int n=q.size(); List<Integer> lvl=new ArrayList<>(); for(int k=0;k<n;k++){ TreeNode x=q.poll(); lvl.add(x.val); if(x.left!=null)q.add(x.left); if(x.right!=null)q.add(x.right);} res.add(lvl);} return res;
    }
    public static void main(String[] args) {
        Integer[] a={3,9,20,null,15,7}; Integer[] b={}; Integer[] c={1};
        List<List<Integer>> got1=levelOrder(buildTree(a));
        if(!(got1.equals(Arrays.asList(Arrays.asList(3),Arrays.asList(9,20),Arrays.asList(15,7))))){System.out.println("FAIL "+got1);throw new RuntimeException("FAILED");}
        if(!levelOrder(buildTree(b)).isEmpty()){System.out.println("FAIL empty");throw new RuntimeException("FAILED");}
        if(!levelOrder(buildTree(c)).equals(Arrays.asList(Arrays.asList(1)))){System.out.println("FAIL single");throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''',
ts='''export function demo(): void {
''' + TREE_TS + '''
    function levelOrder(root: TreeNode|null): number[][] { return levelList(root); }
    const c1=levelOrder(buildTree([3,9,20,null,15,7]));
    if(JSON.stringify(c1)!==JSON.stringify([[3],[9,20],[15,7]])){console.log("FAIL "+JSON.stringify(c1));throw new Error("FAILED");}
    if(levelOrder(buildTree([])).length!==0){console.log("FAIL empty");throw new Error("FAILED");}
    if(JSON.stringify(levelOrder(buildTree([1])))!==JSON.stringify([[1]])){console.log("FAIL single");throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# lc_107 levelOrderBottom
add("lc_107",
go='''package main
import ("fmt";"os";"reflect")
''' + TREE_GO + '''
func levelOrderBottom(root *TreeNode) [][]int {
    lo := levelList(root)
    for i, j := 0, len(lo)-1; i < j; i, j = i+1, j-1 { lo[i], lo[j] = lo[j], lo[i] }
    return lo
}
func main() {
    if got := levelOrderBottom(buildTree([]int{3,9,20,NULL,15,7})); !reflect.DeepEqual(got, [][]int{{15,7},{9,20},{3}}) { fmt.Println("FAIL", got); os.Exit(1) }
    fmt.Println("PASS")
}''',
java='''package com.webfault.dsa;
import java.util.*;
class Main {
''' + TREE_JAVA + '''
    static List<List<Integer>> levelOrderBottom(TreeNode root){
        List<List<Integer>> res=new ArrayList<>(); if(root==null)return res;
        LinkedList<TreeNode> q=new LinkedList<>(); q.add(root);
        while(!q.isEmpty()){ int n=q.size(); List<Integer> lvl=new ArrayList<>(); for(int k=0;k<n;k++){ TreeNode x=q.poll(); lvl.add(x.val); if(x.left!=null)q.add(x.left); if(x.right!=null)q.add(x.right);} res.add(0,lvl);} return res;
    }
    public static void main(String[] args) {
        Integer[] a={3,9,20,null,15,7};
        List<List<Integer>> got=levelOrderBottom(buildTree(a));
        if(!got.equals(Arrays.asList(Arrays.asList(15,7),Arrays.asList(9,20),Arrays.asList(3)))){System.out.println("FAIL "+got);throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''')

# lc_108 sortedArrayToBST
add("lc_108",
go='''package main
import ("fmt";"os";"reflect")
''' + TREE_GO + '''
func sortedArrayToBST(nums []int) *TreeNode {
    var build func(int, int) *TreeNode
    build = func(l, r int) *TreeNode {
        if l > r { return nil }
        m := (l + r) / 2
        return &TreeNode{Val: nums[m], Left: build(l, m-1), Right: build(m+1, r)}
    }
    return build(0, len(nums)-1)
}
func main() {
    inorder := inorderT(sortedArrayToBST([]int{1,2,3}))
    if !reflect.DeepEqual(inorder, []int{1,2,3}) { fmt.Println("FAIL", inorder); os.Exit(1) }
    inorder = inorderT(sortedArrayToBST([]int{-10,-3,0,5,9}))
    if !reflect.DeepEqual(inorder, []int{-10,-3,0,5,9}) { fmt.Println("FAIL", inorder); os.Exit(1) }
    fmt.Println("PASS")
}''',
java='''package com.webfault.dsa;
import java.util.*;
class Main {
''' + TREE_JAVA + '''
    static int[] numsArr;
    static TreeNode build(int l,int r){ if(l>r)return null; int m=(l+r)/2; return new TreeNode(numsArr[m],build(l,m-1),build(m+1,r)); }
    static TreeNode sortedArrayToBST(int[] nums){ numsArr=nums; return build(0,nums.length-1); }
    public static void main(String[] args) {
        if(!inorderT(sortedArrayToBST(new int[]{1,2,3})).equals(Arrays.asList(1,2,3))){System.out.println("FAIL");throw new RuntimeException("FAILED");}
        if(!inorderT(sortedArrayToBST(new int[]{-10,-3,0,5,9})).equals(Arrays.asList(-10,-3,0,5,9))){System.out.println("FAIL");throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''')

# lc_112 hasPathSum
add("lc_112",
go='''package main
import ("fmt";"os")
''' + TREE_GO + '''
func hasPathSum(root *TreeNode, sum int) bool {
    if root == nil { return false }
    if root.Left == nil && root.Right == nil { return root.Val == sum }
    return hasPathSum(root.Left, sum-root.Val) || hasPathSum(root.Right, sum-root.Val)
}
func main() {
    t := buildTree([]int{5,4,8,11,NULL,13,4,7,2,NULL,NULL,NULL,1})
    ok := true
    if !hasPathSum(t, 22) { ok=false; fmt.Println("FAIL 22") }
    if hasPathSum(t, 1) { ok=false; fmt.Println("FAIL 1") }
    if hasPathSum(nil, 0) { ok=false }
    if !ok { os.Exit(1) }
    fmt.Println("PASS")
}''',
java='''package com.webfault.dsa;
class Main {
''' + TREE_JAVA + '''
    static boolean hasPathSum(TreeNode root,int sum){ if(root==null)return false; if(root.left==null&&root.right==null)return root.val==sum; return hasPathSum(root.left,sum-root.val)||hasPathSum(root.right,sum-root.val); }
    public static void main(String[] args) {
        Integer[] a={5,4,8,11,null,13,4,7,2,null,null,null,1};
        TreeNode t=buildTree(a);
        if(!(hasPathSum(t,22)&&!hasPathSum(t,1)&&!hasPathSum(null,0))){System.out.println("FAIL");throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''',
ts='''export function demo(): void {
''' + TREE_TS + '''
    function hasPathSum(root:TreeNode|null,sum:number):boolean{ if(!root)return false; if(!root.left&&!root.right)return root.val===sum; return hasPathSum(root.left,sum-root.val)||hasPathSum(root.right,sum-root.val); }
    const t=buildTree([5,4,8,11,null,13,4,7,2,null,null,null,1]);
    if(!(hasPathSum(t,22)&&!hasPathSum(t,1)&&!hasPathSum(null,0))){console.log("FAIL");throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# lc_114 flatten
add("lc_114",
go='''package main
import ("fmt";"os";"reflect")
''' + TREE_GO + '''
func flatten(root *TreeNode) {
    var prev *TreeNode
    var dfs func(*TreeNode)
    dfs = func(n *TreeNode) {
        if n == nil { return }
        dfs(n.Right)
        dfs(n.Left)
        n.Right = prev; n.Left = nil; prev = n
    }
    dfs(root)
}
func rightArr(root *TreeNode) []int {
    res := []int{}
    for root != nil { res = append(res, root.Val); root = root.Right }
    return res
}
func main() {
    t := buildTree([]int{1,2,5,3,4,NULL,6})
    flatten(t)
    if got := rightArr(t); !reflect.DeepEqual(got, []int{1,2,3,4,5,6}) { fmt.Println("FAIL", got); os.Exit(1) }
    fmt.Println("PASS")
}''',
ts='''export function demo(): void {
''' + TREE_TS + '''
    function flatten(root:TreeNode|null):void{ let prev:TreeNode|null=null; function dfs(n:TreeNode|null){ if(!n)return; dfs(n.right); dfs(n.left); n.right=prev; n.left=null; prev=n; } dfs(root); }
    function rightArr(r:TreeNode|null):number[]{ const a:number[]=[]; while(r){a.push(r.val);r=r.right;} return a; }
    const t=buildTree([1,2,5,3,4,null,6]); flatten(t);
    if(JSON.stringify(rightArr(t))!==JSON.stringify([1,2,3,4,5,6])){console.log("FAIL");throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# lc_116 connect (Node with next)
add("lc_116",
java='''package com.webfault.dsa;
import java.util.*;
class Node { int val; Node left; Node right; Node next; Node(){} Node(int v){val=v;} Node(int v,Node l,Node r,Node n){val=v;left=l;right=r;next=n;} }
class Main {
    static Node connect(Node root){
        if(root==null)return null;
        LinkedList<Node> q=new LinkedList<>(); q.add(root);
        while(!q.isEmpty()){ int n=q.size(); Node prev=null;
            for(int k=0;k<n;k++){ Node x=q.poll(); if(prev!=null)prev.next=x; prev=x; if(x.left!=null)q.add(x.left); if(x.right!=null)q.add(x.right); } }
        return root;
    }
    public static void main(String[] args) {
        Node n1=new Node(1); n1.left=new Node(2); n1.right=new Node(3); n1.left.left=new Node(4); n1.left.right=new Node(5); n1.right.left=new Node(6); n1.right.right=new Node(7);
        connect(n1);
        // level2 next chain: 2->3 ; level3: 4->5->6->7
        if(n1.left.next!=n1.right){System.out.println("FAIL lvl2");throw new RuntimeException("FAILED");}
        if(n1.left.left.next!=n1.left.right||n1.left.right.next!=n1.right.left||n1.right.left.next!=n1.right.right){System.out.println("FAIL lvl3");throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''',
ts='''export function demo(): void {
    class Node { val:number; left:Node|null=null; right:Node|null=null; next:Node|null=null; constructor(v:number){this.val=v;} }
    function connect(root:Node|null):Node|null{ if(!root)return null; const q:Node[]=[root]; while(q.length){ const n=q.length; let prev:Node|null=null; for(let k=0;k<n;k++){ const x=q.shift()!; if(prev)prev.next=x; prev=x; if(x.left)q.push(x.left); if(x.right)q.push(x.right);} } return root; }
    const n1=new Node(1); n1.left=new Node(2); n1.right=new Node(3); n1.left.left=new Node(4); n1.left.right=new Node(5); n1.right.left=new Node(6); n1.right.right=new Node(7);
    connect(n1);
    if(n1.left!.next!==n1.right){console.log("FAIL lvl2");throw new Error("FAILED");}
    if(n1.left!.left!.next!==n1.left!.right||n1.left!.right!.next!==n1.right!.left||n1.right!.left!.next!==n1.right!.right){console.log("FAIL lvl3");throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# lc_144 preorder
add("lc_144",
go='''package main
import ("fmt";"os";"reflect")
''' + TREE_GO + '''
func preorderTraversal(root *TreeNode) []int {
    if root == nil { return []int{} }
    return append(append([]int{root.Val}, preorderTraversal(root.Left)...), preorderTraversal(root.Right)...)
}
func main() {
    if got := preorderTraversal(buildTree([]int{1,2,3,NULL,4,5})); !reflect.DeepEqual(got, []int{1,2,4,3,5}) { fmt.Println("FAIL", got); os.Exit(1) }
    if got := preorderTraversal(nil); len(got) != 0 { fmt.Println("FAIL nil"); os.Exit(1) }
    fmt.Println("PASS")
}''',
ts='''export function demo(): void {
''' + TREE_TS + '''
    function preorderTraversal(root:TreeNode|null):number[]{ if(!root)return []; return [root.val,...preorderTraversal(root.left),...preorderTraversal(root.right)]; }
    if(JSON.stringify(preorderTraversal(buildTree([1,2,3,null,4,5])))!==JSON.stringify([1,2,4,3,5])){console.log("FAIL");throw new Error("FAILED");}
    if(preorderTraversal(null).length!==0){console.log("FAIL nil");throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# lc_145 postorder
add("lc_145",
go='''package main
import ("fmt";"os";"reflect")
''' + TREE_GO + '''
func postorderTraversal(root *TreeNode) []int {
    if root == nil { return []int{} }
    return append(append(postorderTraversal(root.Left), postorderTraversal(root.Right)...), root.Val)
}
func main() {
    if got := postorderTraversal(buildTree([]int{1,2,3,NULL,4,5})); !reflect.DeepEqual(got, []int{4,2,5,3,1}) { fmt.Println("FAIL", got); os.Exit(1) }
    fmt.Println("PASS")
}''',
ts='''export function demo(): void {
''' + TREE_TS + '''
    function postorderTraversal(root:TreeNode|null):number[]{ if(!root)return []; return [...postorderTraversal(root.left),...postorderTraversal(root.right),root.val]; }
    if(JSON.stringify(postorderTraversal(buildTree([1,2,3,null,4,5])))!==JSON.stringify([4,2,5,3,1])){console.log("FAIL");throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# lc_94 inorder
add("lc_94",
go='''package main
import ("fmt";"os";"reflect")
''' + TREE_GO + '''
func inorderTraversal(root *TreeNode) []int { return inorderT(root) }
func main() {
    if got := inorderTraversal(buildTree([]int{1,2,3,NULL,4,5})); !reflect.DeepEqual(got, []int{2,4,1,5,3}) { fmt.Println("FAIL", got); os.Exit(1) }
    fmt.Println("PASS")
}''',
ts='''export function demo(): void {
''' + TREE_TS + '''
    function inorderTraversal(root:TreeNode|null):number[]{ return inorderT(root); }
    if(JSON.stringify(inorderTraversal(buildTree([1,2,3,null,4,5])))!==JSON.stringify([2,4,1,5,3])){console.log("FAIL");throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# lc_222 countNodes
add("lc_222",
ts='''export function demo(): void {
''' + TREE_TS + '''
    function countNodes(root:TreeNode|null):number{ if(!root)return 0; return 1+countNodes(root.left)+countNodes(root.right); }
    if(countNodes(buildTree([1,2,3,4,5,6]))!==6){console.log("FAIL");throw new Error("FAILED");}
    if(countNodes(null)!==0){console.log("FAIL nil");throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# lc_230 kthSmallest
add("lc_230",
ts='''export function demo(): void {
''' + TREE_TS + '''
    function kthSmallest(root:TreeNode|null,k:number):number{ const arr=inorderT(root); return arr[k-1]; }
    const t=buildTree([3,1,4,null,2]);
    if(kthSmallest(t,1)!==1||kthSmallest(t,2)!==2||kthSmallest(t,3)!==3||kthSmallest(t,4)!==4){console.log("FAIL");throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# lc_236 lowestCommonAncestor
add("lc_236",
go='''package main
import ("fmt";"os")
''' + TREE_GO + '''
func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
    if root == nil || root == p || root == q { return root }
    left := lowestCommonAncestor(root.Left, p, q)
    right := lowestCommonAncestor(root.Right, p, q)
    if left != nil && right != nil { return root }
    if left != nil { return left }
    return right
}
func find(root *TreeNode, v int) *TreeNode {
    if root == nil { return nil }
    if root.Val == v { return root }
    if l := find(root.Left, v); l != nil { return l }
    return find(root.Right, v)
}
func main() {
    root := buildTree([]int{3,5,1,6,2,0,8,NULL,NULL,7,4})
    p := find(root, 5); q := find(root, 1)
    if lca := lowestCommonAncestor(root, p, q); lca == nil || lca.Val != 3 { fmt.Println("FAIL", lca); os.Exit(1) }
    fmt.Println("PASS")
}''',
java='''package com.webfault.dsa;
class Main {
''' + TREE_JAVA + '''
    static TreeNode lowestCommonAncestor(TreeNode root,TreeNode p,TreeNode q){ if(root==null||root==p||root==q)return root; TreeNode l=lowestCommonAncestor(root.left,p,q); TreeNode r=lowestCommonAncestor(root.right,p,q); if(l!=null&&r!=null)return root; return l!=null?l:r; }
    static TreeNode find(TreeNode root,int v){ if(root==null)return null; if(root.val==v)return root; TreeNode l=find(root.left,v); if(l!=null)return l; return find(root.right,v); }
    public static void main(String[] args) {
        Integer[] a={3,5,1,6,2,0,8,null,null,7,4}; TreeNode root=buildTree(a);
        TreeNode lca=lowestCommonAncestor(root,find(root,5),find(root,1));
        if(lca==null||lca.val!=3){System.out.println("FAIL");throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''')

# lc_257 binaryTreePaths
add("lc_257",
ts='''export function demo(): void {
''' + TREE_TS + '''
    function binaryTreePaths(root:TreeNode|null):string[]{ const res:string[]=[]; function dfs(n:TreeNode|null,path:string){ if(!n)return; const p=path+(path===""?"":"->")+n.val; if(!n.left&&!n.right){res.push(p);return;} dfs(n.left,p); dfs(n.right,p);} dfs(root,""); return res; }
    const paths=binaryTreePaths(buildTree([1,2,3,null,5]));
    const want=JSON.stringify(["1->2->5","1->3"]);
    if(JSON.stringify(paths)!==want){console.log("FAIL "+JSON.stringify(paths));throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# lc_513 findBottomLeftValue
add("lc_513",
java='''package com.webfault.dsa;
class Main {
''' + TREE_JAVA + '''
    static int findBottomLeftValue(TreeNode root){ java.util.LinkedList<TreeNode> q=new java.util.LinkedList<>(); q.add(root); int leftmost=root.val; while(!q.isEmpty()){ int n=q.size(); leftmost=q.peek().val; for(int k=0;k<n;k++){ TreeNode x=q.poll(); if(x.left!=null)q.add(x.left); if(x.right!=null)q.add(x.right);} } return leftmost; }
    public static void main(String[] args) {
        if(findBottomLeftValue(buildTree(new Integer[]{1,2,3,4,5,6,7}))!=4){System.out.println("FAIL");throw new RuntimeException("FAILED");}
        if(findBottomLeftValue(buildTree(new Integer[]{2,1,3}))!=1){System.out.println("FAIL2");throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''',
ts='''export function demo(): void {
''' + TREE_TS + '''
    function findBottomLeftValue(root:TreeNode|null):number{ const q:TreeNode[]=[root!]; let leftmost=root!.val; while(q.length){ const n=q.length; leftmost=q[0].val; for(let k=0;k<n;k++){ const x=q.shift()!; if(x.left)q.push(x.left); if(x.right)q.push(x.right);} } return leftmost; }
    if(findBottomLeftValue(buildTree([1,2,3,4,5,6,7]))!==4){console.log("FAIL");throw new Error("FAILED");}
    if(findBottomLeftValue(buildTree([2,1,3]))!==1){console.log("FAIL2");throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# lc_515 largestValues
add("lc_515",
go='''package main
import ("fmt";"os";"reflect")
''' + TREE_GO + '''
func largestValues(root *TreeNode) []int {
    res := []int{}
    if root == nil { return res }
    q := []*TreeNode{root}
    for len(q) > 0 {
        mx := -1000000000; n := len(q)
        for k := 0; k < n; k++ {
            node := q[0]; q = q[1:]
            if node.Val > mx { mx = node.Val }
            if node.Left != nil { q = append(q, node.Left) }
            if node.Right != nil { q = append(q, node.Right) }
        }
        res = append(res, mx)
    }
    return res
}
func main() {
    if got := largestValues(buildTree([]int{1,3,2,5,3,NULL,9})); !reflect.DeepEqual(got, []int{1,3,9}) { fmt.Println("FAIL", got); os.Exit(1) }
    fmt.Println("PASS")
}''',
ts='''export function demo(): void {
''' + TREE_TS + '''
    function largestValues(root:TreeNode|null):number[]{ const res:number[]=[]; if(!root)return res; let q:TreeNode[]=[root]; while(q.length){ let mx=-Infinity; const n=q.length; for(let k=0;k<n;k++){ const x=q.shift()!; if(x.val>mx)mx=x.val; if(x.left)q.push(x.left); if(x.right)q.push(x.right);} res.push(mx);} return res; }
    if(JSON.stringify(largestValues(buildTree([1,3,2,5,3,null,9])))!==JSON.stringify([1,3,9])){console.log("FAIL");throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# lc_617 mergeTrees
add("lc_617",
go='''package main
import ("fmt";"os";"reflect")
''' + TREE_GO + '''
func mergeTrees(t1, t2 *TreeNode) *TreeNode {
    if t1 == nil { return t2 }
    if t2 == nil { return t1 }
    return &TreeNode{Val: t1.Val + t2.Val, Left: mergeTrees(t1.Left, t2.Left), Right: mergeTrees(t1.Right, t2.Right)}
}
func main() {
    a := buildTree([]int{1,3,2,5})
    b := buildTree([]int{2,1,3,NULL,4,NULL,7})
    got := levelList(mergeTrees(a, b))
    if !reflect.DeepEqual(got, [][]int{{3},{4,5},{5,4,NULL,7}}) && !reflect.DeepEqual(got, [][]int{{3},{4,5},{5,4,7}}) {
        fmt.Println("FAIL", got); os.Exit(1)
    }
    fmt.Println("PASS")
}''',
java='''package com.webfault.dsa;
import java.util.*;
class Main {
''' + TREE_JAVA + '''
    static TreeNode mergeTrees(TreeNode t1,TreeNode t2){ if(t1==null)return t2; if(t2==null)return t1; return new TreeNode(t1.val+t2.val,mergeTrees(t1.left,t2.left),mergeTrees(t1.right,t2.right)); }
    static List<List<Integer>> levelList(TreeNode root){ List<List<Integer>> res=new ArrayList<>(); if(root==null)return res; LinkedList<TreeNode> q=new LinkedList<>(); q.add(root); while(!q.isEmpty()){ int n=q.size(); List<Integer> lvl=new ArrayList<>(); for(int k=0;k<n;k++){ TreeNode x=q.poll(); lvl.add(x.val); if(x.left!=null)q.add(x.left); if(x.right!=null)q.add(x.right);} res.add(lvl);} return res; }
    public static void main(String[] args) {
        TreeNode a=buildTree(new Integer[]{1,3,2,5}); TreeNode b=buildTree(new Integer[]{2,1,3,null,4,null,7});
        List<List<Integer>> got=levelList(mergeTrees(a,b));
        List<List<Integer>> want=Arrays.asList(Arrays.asList(3),Arrays.asList(4,5),Arrays.asList(5,4,7));
        if(!got.equals(want)){System.out.println("FAIL "+got);throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''',
ts='''export function demo(): void {
''' + TREE_TS + '''
    function mergeTrees(t1:TreeNode|null,t2:TreeNode|null):TreeNode|null{ if(!t1)return t2; if(!t2)return t1; return new TreeNode(t1.val+t2.val,mergeTrees(t1.left,t2.left),mergeTrees(t1.right,t2.right)); }
    const a=buildTree([1,3,2,5]); const b=buildTree([2,1,3,null,4,null,7]);
    const got=levelList(mergeTrees(a,b));
    if(JSON.stringify(got)!==JSON.stringify([[3],[4,5],[5,4,7]])){console.log("FAIL "+JSON.stringify(got));throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# lc_700 searchBST
add("lc_700",
java='''package com.webfault.dsa;
class Main {
''' + TREE_JAVA + '''
    static TreeNode searchBST(TreeNode root,int v){ while(root!=null){ if(root.val==v)return root; root= v<root.val?root.left:root.right;} return null; }
    public static void main(String[] args) {
        TreeNode root=buildTree(new Integer[]{4,2,7,1,3});
        if(searchBST(root,2)==null||searchBST(root,2).val!=2){System.out.println("FAIL2");throw new RuntimeException("FAILED");}
        if(searchBST(root,5)!=null){System.out.println("FAIL5");throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''')

# lc_701 insertIntoBST
add("lc_701",
go='''package main
import ("fmt";"os";"reflect")
''' + TREE_GO + '''
func insertIntoBST(root *TreeNode, val int) *TreeNode {
    if root == nil { return &TreeNode{Val: val} }
    if val < root.Val { root.Left = insertIntoBST(root.Left, val) } else { root.Right = insertIntoBST(root.Right, val) }
    return root
}
func main() {
    t := insertIntoBST(buildTree([]int{4,2,7,1,3}), 5)
    if got := inorderT(t); !reflect.DeepEqual(got, []int{1,2,3,4,5,7}) { fmt.Println("FAIL", got); os.Exit(1) }
    fmt.Println("PASS")
}''')

# lc_572 isSubtree
add("lc_572",
java='''package com.webfault.dsa;
class Main {
''' + TREE_JAVA + '''
    static boolean same(TreeNode a,TreeNode b){ if(a==null&&b==null)return true; if(a==null||b==null)return false; if(a.val!=b.val)return false; return same(a.left,b.left)&&same(a.right,b.right); }
    static boolean isSubtree(TreeNode root,TreeNode sub){ if(root==null)return false; if(same(root,sub))return true; return isSubtree(root.left,sub)||isSubtree(root.right,sub); }
    public static void main(String[] args) {
        TreeNode root=buildTree(new Integer[]{3,4,5,1,2}); TreeNode sub1=buildTree(new Integer[]{4,1,2}); TreeNode sub2=buildTree(new Integer[]{4,1,3});
        if(!(isSubtree(root,sub1)&&!isSubtree(root,sub2))){System.out.println("FAIL");throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''')

# lc_429 NAry levelOrder
add("lc_429",
go='''package main
import ("fmt";"os";"reflect")
type Node struct { Val int; Children []*Node }
func levelOrder(root *Node) [][]int {
    if root == nil { return [][]int{} }
    res := [][]int{}; q := []*Node{root}
    for len(q) > 0 {
        lvl := []int{}; n := len(q)
        for k := 0; k < n; k++ {
            node := q[0]; q = q[1:]; lvl = append(lvl, node.Val)
            for _, ch := range node.Children { q = append(q, ch) }
        }
        res = append(res, lvl)
    }
    return res
}
func main() {
    c5 := &Node{Val: 5}; c6 := &Node{Val: 6}
    c3 := &Node{Val: 3, Children: []*Node{c5, c6}}; c2 := &Node{Val: 2}; c4 := &Node{Val: 4}
    root := &Node{Val: 1, Children: []*Node{c3, c2, c4}}
    if got := levelOrder(root); !reflect.DeepEqual(got, [][]int{{1},{3,2,4},{5,6}}) { fmt.Println("FAIL", got); os.Exit(1) }
    fmt.Println("PASS")
}''',
ts='''export function demo(): void {
    class Node { val:number; children:Node[]=[]; constructor(v:number){this.val=v;} }
    function levelOrder(root:Node|null):number[][]{ if(!root)return []; const res:number[][]=[]; let q:Node[]=[root]; while(q.length){ const lvl:number[]=[]; const n=q.length; for(let k=0;k<n;k++){ const x=q.shift()!; lvl.push(x.val); for(const c of x.children)q.push(c);} res.push(lvl);} return res; }
    const c5=new Node(5),c6=new Node(6); const c3=new Node(3); c3.children=[c5,c6]; const c2=new Node(2),c4=new Node(4); const root=new Node(1); root.children=[c3,c2,c4];
    if(JSON.stringify(levelOrder(root))!==JSON.stringify([[1],[3,2,4],[5,6]])){console.log("FAIL");throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# ============================ BATCH 4 (classic arrays/strings) ============================
# lc_20 isValid
add("lc_20",
go='''package main
import ("fmt";"os")
func isValid(s string) bool {
    st := []rune{}
    for _, c := range s {
        if c == '(' || c == '[' || c == '{' { st = append(st, c) }
        else {
            if len(st) == 0 { return false }
            top := st[len(st)-1]; st = st[:len(st)-1]
            if (c == ')' && top != '(') || (c == ']' && top != '[') || (c == '}' && top != '{') { return false }
        }
    }
    return len(st) == 0
}
func main() {
    ok := true
    if !isValid("()") { ok=false; fmt.Println("FAIL ()") }
    if !isValid("()[]{}") { ok=false; fmt.Println("FAIL ()[]{}") }
    if isValid("(]") { ok=false; fmt.Println("FAIL (]") }
    if !ok { os.Exit(1) }
    fmt.Println("PASS")
}''',
java='''package com.webfault.dsa;
import java.util.Stack;
class Main {
    static boolean isValid(String s){ Stack<Character> st=new Stack<>(); for(char c:s.toCharArray()){ if(c=='('||c=='['||c=='{')st.push(c); else { if(st.isEmpty())return false; char t=st.pop(); if((c==')'&&t!='(')||(c==']'&&t!='[')||(c=='}'&&t!='{'))return false; } } return st.isEmpty(); }
    public static void main(String[] args) {
        if(!(isValid("()")&&isValid("()[]{}")&&!isValid("(]"))){System.out.println("FAIL");throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''',
ts='''export function demo(): void {
    function isValid(s: string): boolean {
        const st: string[] = [];
        for (const c of s) {
            if (c==='('||c==='['||c==='{') st.push(c);
            else { if(st.length===0) return false; const t=st.pop()!; if((c===')'&&t!=='(')||(c===']'&&t!=='[')||(c==='}'&&t!=='{'))return false; }
        }
        return st.length===0;
    }
    if(!(isValid("()")&&isValid("()[]{}")&&!isValid("(]"))){console.log("FAIL");throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# lc_15 threeSum
add("lc_15",
java='''package com.webfault.dsa;
import java.util.*;
class Main {
    static List<List<Integer>> threeSum(int[] nums){
        Arrays.sort(nums); List<List<Integer>> res=new ArrayList<>();
        for(int i=0;i<nums.length-2;i++){ if(i>0&&nums[i]==nums[i-1])continue; int l=i+1,r=nums.length-1;
            while(l<r){ int s=nums[i]+nums[l]+nums[r]; if(s==0){ res.add(Arrays.asList(nums[i],nums[l],nums[r])); while(l<r&&nums[l]==nums[l+1])l++; while(l<r&&nums[r]==nums[r-1])r--; l++;r--; } else if(s<0)l++; else r--; } }
        return res;
    }
    public static void main(String[] args) {
        List<List<Integer>> got=threeSum(new int[]{-1,0,1,2,-1,-4});
        if(got.size()!=2){System.out.println("FAIL size "+got.size());throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''',
ts='''export function demo(): void {
    function threeSum(nums: number[]): number[][] {
        nums.sort((a,b)=>a-b); const res:number[][]=[];
        for(let i=0;i<nums.length-2;i++){ if(i>0&&nums[i]===nums[i-1])continue; let l=i+1,r=nums.length-1;
            while(l<r){ const s=nums[i]+nums[l]+nums[r]; if(s===0){ res.push([nums[i],nums[l],nums[r]]); while(l<r&&nums[l]===nums[l+1])l++; while(l<r&&nums[r]===nums[r-1])r--; l++;r--; } else if(s<0)l++; else r--; } }
        return res;
    }
    const got=threeSum([-1,0,1,2,-1,-4]); if(got.length!==2){console.log("FAIL "+got.length);throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# lc_78 subsets
add("lc_78",
go='''package main
import ("fmt";"os";"sort")
func subsets(nums []int) [][]int {
    sort.Ints(nums)
    res := [][]int{{}}
    for _, v := range nums {
        for _, sub := range res {
            ns := make([]int, len(sub)+1); copy(ns, sub); ns[len(sub)] = v
            res = append(res, ns)
        }
    }
    return res
}
func main() {
    got := subsets([]int{1,2,3})
    if len(got) != 8 { fmt.Println("FAIL", len(got)); os.Exit(1) }
    fmt.Println("PASS")
}''',
java='''package com.webfault.dsa;
import java.util.*;
class Main {
    static List<List<Integer>> subsets(int[] nums){ Arrays.sort(nums); List<List<Integer>> res=new ArrayList<>(); res.add(new ArrayList<>()); for(int v:nums){ int n=res.size(); for(int i=0;i<n;i++){ List<Integer> ns=new ArrayList<>(res.get(i)); ns.add(v); res.add(ns);} } return res; }
    public static void main(String[] args) {
        if(subsets(new int[]{1,2,3}).size()!=8){System.out.println("FAIL");throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''')

# lc_77 combine
add("lc_77",
java='''package com.webfault.dsa;
import java.util.*;
class Main {
    static List<List<Integer>> combine(int n,int k){ List<List<Integer>> res=new ArrayList<>(); List<Integer> cur=new ArrayList<>(); combineH(1,n,k,cur,res); return res; }
    static void combineH(int s,int n,int k,List<Integer> cur,List<List<Integer>> res){ if(cur.size()==k){res.add(new ArrayList<>(cur));return;} for(int i=s;i<=n-(k-cur.size())+1;i++){cur.add(i);combineH(i+1,n,k,cur,res);cur.remove(cur.size()-1);} }
    public static void main(String[] args) {
        if(combine(4,2).size()!=6){System.out.println("FAIL");throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''',
ts='''export function demo(): void {
    function combine(n:number,k:number):number[][]{ const res:number[][]=[]; const cur:number[]=[]; function h(s:number){ if(cur.length===k){res.push([...cur]);return;} for(let i=s;i<=n-(k-cur.length)+1;i++){cur.push(i);h(i+1);cur.pop();} } h(1); return res; }
    if(combine(4,2).length!==6){console.log("FAIL");throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# lc_46 permute
add("lc_46",
go='''package main
import ("fmt";"os")
func permute(nums []int) [][]int {
    res := [][]int{}
    var bt func(int)
    bt = func(i int) {
        if i == len(nums) { ns := make([]int, len(nums)); copy(ns, nums); res = append(res, ns); return }
        for j := i; j < len(nums); j++ { nums[i], nums[j] = nums[j], nums[i]; bt(i+1); nums[i], nums[j] = nums[j], nums[i] }
    }
    bt(0)
    return res
}
func main() {
    if got := permute([]int{1,2,3}); len(got) != 6 { fmt.Println("FAIL", len(got)); os.Exit(1) }
    fmt.Println("PASS")
}''')

# lc_47 permuteUnique
add("lc_47",
ts='''export function demo(): void {
    function permuteUnique(nums:number[]):number[][]{ const res:number[][]=[]; nums.sort((a,b)=>a-b); const used=new Array(nums.length).fill(false); function bt(cur:number[]){ if(cur.length===nums.length){res.push([...cur]);return;} for(let i=0;i<nums.length;i++){ if(used[i]||(i>0&&nums[i]===nums[i-1]&&!used[i-1]))continue; used[i]=true; cur.push(nums[i]); bt(cur); cur.pop(); used[i]=false; } } bt([]); return res; }
    if(permuteUnique([1,1,2]).length!==3){console.log("FAIL");throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# lc_39 combinationSum
add("lc_39",
go='''package main
import ("fmt";"os")
func combinationSum(candidates []int, target int) [][]int {
    res := [][]int{}; cur := []int{}
    var bt func(int, int)
    bt = func(i, s int) {
        if s == target { ns := make([]int, len(cur)); copy(ns, cur); res = append(res, ns); return }
        if s > target { return }
        for j := i; j < len(candidates); j++ { cur = append(cur, candidates[j]); bt(j, s+candidates[j]); cur = cur[:len(cur)-1] }
    }
    bt(0, 0)
    return res
}
func main() {
    got := combinationSum([]int{2,3,6,7}, 7)
    if len(got) != 2 { fmt.Println("FAIL", len(got)); os.Exit(1) }
    fmt.Println("PASS")
}''')

# lc_93 restoreIpAddresses
add("lc_93",
java='''package com.webfault.dsa;
import java.util.*;
class Main {
    static List<String> restoreIpAddresses(String s){ List<String> res=new ArrayList<>(); bt(s,0,new ArrayList<>(),res); return res; }
    static void bt(String s,int i,List<String> cur,List<String> res){ if(cur.size()==4){ if(i==s.length()){ res.add(String.join(".",cur)); } return; } if(i==s.length())return;
        for(int j=1;j<=3&&i+j<=s.length();j++){ String seg=s.substring(i,i+j); if((seg.length()>1&&seg.charAt(0)=='0')||Integer.parseInt(seg)>255)continue; cur.add(seg); bt(s,i+j,cur,res); cur.remove(cur.size()-1); } }
    public static void main(String[] args) {
        if(restoreIpAddresses("25525511135").size()!=4){System.out.println("FAIL");throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''')

# lc_17 letterCombinations
add("lc_17",
go='''package main
import ("fmt";"os")
func letterCombinations(digits string) []string {
    if digits == "" { return []string{} }
    m := map[byte]string{'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
    res := []string{""}
    for i := 0; i < len(digits); i++ {
        letters := m[digits[i]]; n := len(res); ns := []string{}
        for _, pre := range res { for _, c := range letters { ns = append(ns, pre+string(c)) } }
        res = ns; _ = n
    }
    return res
}
func main() {
    got := letterCombinations("23")
    if len(got) != 9 { fmt.Println("FAIL", len(got)); os.Exit(1) }
    fmt.Println("PASS")
}''',
ts='''export function demo(): void {
    function letterCombinations(digits:string):string[]{ if(digits==="")return []; const m:Record<string,string>={}; m['2']="abc";m['3']="def";m['4']="ghi";m['5']="jkl";m['6']="mno";m['7']="pqrs";m['8']="tuv";m['9']="wxyz"; let res=[""]; for(const d of digits){ let ns:string[]=[]; for(const pre of res)for(const c of m[d])ns.push(pre+c); res=ns; } return res; }
    if(letterCombinations("23").length!==9){console.log("FAIL");throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# lc_45 jump
add("lc_45",
java='''package com.webfault.dsa;
class Main {
    static int jump(int[] nums){ int pos=0,steps=0,end=0; for(int i=0;i<nums.length-1;i++){ end=Math.max(end,i+nums[i]); if(i==pos){ pos=end; steps++; } } return steps; }
    public static void main(String[] args) {
        if(jump(new int[]{2,3,1,1,4})!=2){System.out.println("FAIL");throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''',
ts='''export function demo(): void {
    function jump(nums:number[]):number{ let pos=0,steps=0,end=0; for(let i=0;i<nums.length-1;i++){ end=Math.max(end,i+nums[i]); if(i===pos){pos=end;steps++;} } return steps; }
    if(jump([2,3,1,1,4])!==2){console.log("FAIL");throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# lc_621 leastInterval
add("lc_621",
java='''package com.webfault.dsa;
import java.util.*;
class Main {
    static int leastInterval(char[] tasks,int n){ int[] cnt=new int[26]; for(char c:tasks)cnt[c-'A']++; Arrays.sort(cnt); int max=0; for(int v:cnt)max=Math.max(max,v); int maxc=0; for(int v:cnt)if(v==max)maxc++; return Math.max(tasks.length,(max-1)*(n+1)+maxc); }
    public static void main(String[] args) {
        if(leastInterval("AAABBB".toCharArray(),2)!=8){System.out.println("FAIL");throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''')

# lc_622 designCircularQueue
add("lc_622",
go='''package main
import ("fmt";"os")
type MyCircularQueue struct { buf []int; front, rear, size, cap int }
func Constructor(k int) *MyCircularQueue { return &MyCircularQueue{buf: make([]int, k), cap: k} }
func (q *MyCircularQueue) EnQueue(v int) bool { if q.size==q.cap { return false }; q.buf[q.rear]=v; q.rear=(q.rear+1)%q.cap; q.size++; return true }
func (q *MyCircularQueue) DeQueue() bool { if q.size==0 { return false }; q.front=(q.front+1)%q.cap; q.size--; return true }
func (q *MyCircularQueue) Front() int { if q.size==0 { return -1 }; return q.buf[q.front] }
func (q *MyCircularQueue) Rear() int { if q.size==0 { return -1 }; return q.buf[(q.rear-1+q.cap)%q.cap] }
func (q *MyCircularQueue) IsEmpty() bool { return q.size==0 }
func (q *MyCircularQueue) IsFull() bool { return q.size==q.cap }
func main() {
    q := Constructor(3)
    if !q.EnQueue(1)||!q.EnQueue(2)||!q.EnQueue(3)||q.EnQueue(4) { fmt.Println("FAIL enqueue"); os.Exit(1) }
    if !q.IsFull() { fmt.Println("FAIL full"); os.Exit(1) }
    if q.Rear()!=3||q.Front()!=1 { fmt.Println("FAIL front/rear"); os.Exit(1) }
    if !q.DeQueue()||q.Front()!=2 { fmt.Println("FAIL dequeue"); os.Exit(1) }
    fmt.Println("PASS")
}''',
ts='''export function demo(): void {
    class MyCircularQueue { buf:number[];front=0;rear=0;size=0;cap:number; constructor(k:number){this.buf=new Array(k);this.cap=k;} EnQueue(v:number):boolean{if(this.size===this.cap)return false;this.buf[this.rear]=v;this.rear=(this.rear+1)%this.cap;this.size++;return true;} DeQueue():boolean{if(this.size===0)return false;this.front=(this.front+1)%this.cap;this.size--;return true;} Front():number{if(this.size===0)return -1;return this.buf[this.front];} Rear():number{if(this.size===0)return -1;return this.buf[(this.rear-1+this.cap)%this.cap];} IsEmpty():boolean{return this.size===0;} IsFull():boolean{return this.size===this.cap;} }
    const q=new MyCircularQueue(3);
    if(!(q.EnQueue(1)&&q.EnQueue(2)&&q.EnQueue(3)&&!q.EnQueue(4))){console.log("FAIL enqueue");throw new Error("FAILED");}
    if(!q.IsFull()||q.Rear()!==3||q.Front()!==1){console.log("FAIL full");throw new Error("FAILED");}
    if(!(q.DeQueue()&&q.Front()===2)){console.log("FAIL dequeue");throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# lc_26 removeDuplicates
add("lc_26",
ts='''export function demo(): void {
    function removeDuplicates(nums:number[]):number{ if(nums.length===0)return 0; let k=1; for(let i=1;i<nums.length;i++){ if(nums[i]!==nums[i-1]){nums[k++]=nums[i];} } return k; }
    const a=[1,1,2]; const k=removeDuplicates(a); if(k!==2||a[0]!==1||a[1]!==2){console.log("FAIL "+k);throw new Error("FAILED");}
    const b=[0,0,1,1,1,2,2,3,3,4]; const k2=removeDuplicates(b); if(k2!==5){console.log("FAIL2 "+k2);throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# lc_384 shuffle
add("lc_384",
go='''package main
import ("fmt";"os";"math/rand")
type Solution struct { orig []int; cur []int }
func Constructor(nums []int) *Solution { c := make([]int, len(nums)); copy(c, nums); return &Solution{orig: nums, cur: c} }
func (s *Solution) Reset() []int { copy(s.cur, s.orig); return s.cur }
func (s *Solution) Shuffle() []int { perm := make([]int, len(s.orig)); for i := range perm { perm[i] = i }; for i := len(perm)-1; i>0; i-- { j := rand.Intn(i+1); perm[i],perm[j]=perm[j],perm[i] }; for i,v := range perm { s.cur[i]=s.orig[v] }; return s.cur }
func same(a, b []int) bool { for i := range a { if a[i]!=b[i] { return false } }; return true }
func main() {
    s := Constructor([]int{1,2,3})
    r := s.Reset(); if !same(r, []int{1,2,3}) { fmt.Println("FAIL reset"); os.Exit(1) }
    sh := s.Shuffle(); if len(sh) != 3 { fmt.Println("FAIL shuffle"); os.Exit(1) }
    fmt.Println("PASS")
}''',
java='''package com.webfault.dsa;
import java.util.*;
class Main {
    static class Solution { int[] orig; int[] cur; Solution(int[] n){orig=n;cur=n.clone();} int[] reset(){cur=orig.clone();return cur;} int[] shuffle(){ Integer[] idx=new Integer[orig.length]; for(int i=0;i<idx.length;i++)idx[i]=i; Collections.shuffle(Arrays.asList(idx)); int[] r=new int[orig.length]; for(int i=0;i<orig.length;i++)r[i]=orig[idx[i]]; cur=r; return r; } }
    public static void main(String[] args) {
        Solution s=new Solution(new int[]{1,2,3}); if(!Arrays.equals(s.reset(),new int[]{1,2,3})){System.out.println("FAIL reset");throw new RuntimeException("FAILED");}
        if(s.shuffle().length!=3){System.out.println("FAIL");throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''',
ts='''export function demo(): void {
    class Solution { orig:number[]; cur:number[]; constructor(n:number[]){this.orig=n;this.cur=[...n];} reset():number[]{this.cur=[...this.orig];return this.cur;} shuffle():number[]{ const idx=[...this.orig.keys()]; for(let i=idx.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[idx[i],idx[j]]=[idx[j],idx[i]];} this.cur=idx.map(k=>this.orig[k]); return this.cur; } }
    const s=new Solution([1,2,3]); if(JSON.stringify(s.reset())!==JSON.stringify([1,2,3])){console.log("FAIL reset");throw new Error("FAILED");}
    if(s.shuffle().length!==3){console.log("FAIL");throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# lc_374 guessNumber
add("lc_374",
go='''package main
import ("fmt";"os")
var pick = 6
func guess(num int) int { if num > pick { return -1 }; if num < pick { return 1 }; return 0 }
func guessNumber(n int) int {
    l, r := 1, n
    for l <= r { mid := (l+r)/2; g := guess(mid); if g==0 { return mid }; if g<0 { r=mid-1 } else { l=mid+1 } }
    return -1
}
func main() {
    if guessNumber(10) != 6 { fmt.Println("FAIL"); os.Exit(1) }
    fmt.Println("PASS")
}''',
java='''package com.webfault.dsa;
class Main {
    static int pick=6;
    static int guess(int num){ if(num>pick)return -1; if(num<pick)return 1; return 0; }
    static int guessNumber(int n){ int l=1,r=n; while(l<=r){ int m=(l+r)/2; int g=guess(m); if(g==0)return m; if(g<0)r=m-1; else l=m+1; } return -1; }
    public static void main(String[] args) {
        if(guessNumber(10)!=6){System.out.println("FAIL");throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''')

# lc_704 search
add("lc_704",
java='''package com.webfault.dsa;
class Main {
    static int search(int[] nums,int t){ int l=0,r=nums.length-1; while(l<=r){ int m=(l+r)/2; if(nums[m]==t)return m; if(nums[m]<t)l=m+1; else r=m-1; } return -1; }
    public static void main(String[] args) {
        if(search(new int[]{1,2,3,4,5},3)!=2){System.out.println("FAIL");throw new RuntimeException("FAILED");}
        if(search(new int[]{1,2,3,4,5},6)!=-1){System.out.println("FAIL2");throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''')

# lc_202 happy bitSquareSum
add("lc_202",
ts='''export function demo(): void {
    function bitSquareSum(n:number):number{ let s=0; while(n>0){ const d=n%10; s+=d*d; n=Math.floor(n/10); } return s; }
    if(bitSquareSum(1)!==1){console.log("FAIL");throw new Error("FAILED");}
    if(bitSquareSum(19)!==82){console.log("FAIL2 "+bitSquareSum(19));throw new Error("FAILED");}
    if(bitSquareSum(2)!==4){console.log("FAIL3");throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# lc_3 lengthOfLongestSubstring
add("lc_3",
java='''package com.webfault.dsa;
import java.util.*;
class Main {
    static int lengthOfLongestSubstring(String s){ int[] last=new int[128]; Arrays.fill(last,-1); int l=0,best=0; for(int i=0;i<s.length();i++){ int c=s.charAt(i); if(last[c]>=l)l=last[c]+1; last[c]=i; best=Math.max(best,i-l+1); } return best; }
    public static void main(String[] args) {
        if(lengthOfLongestSubstring("abcabcbb")!=3){System.out.println("FAIL");throw new RuntimeException("FAILED");}
        if(lengthOfLongestSubstring("bbbbb")!=1){System.out.println("FAIL2");throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''')

# lc_76 minWindow
add("lc_76",
ts='''export function demo(): void {
    function minWindow(s:string,t:string):string{ const need:Record<string,number>={}; let needCnt=t.length; for(const c of t)need[c]=(need[c]||0)+1; let l=0,best=""; for(let r=0;r<s.length;r++){ const c=s[r]; if(need[c]>0)needCnt--; need[c]--; while(needCnt===0){ const w=s.substring(l,r+1); if(best===""||w.length<best.length)best=w; const lc=s[l]; need[lc]++; if(need[lc]>0)needCnt++; l++; } } return best; }
    if(minWindow("ADOBECODEBANC","ABC")!=="BANC"){console.log("FAIL "+minWindow("ADOBECODEBANC","ABC"));throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# lc_567 checkInclusion
add("lc_567",
go='''package main
import ("fmt";"os")
func checkInclusion(s1, s2 string) bool {
    if len(s1) > len(s2) { return false }
    cnt := [26]int{}
    for i := 0; i < len(s1); i++ { cnt[s1[i]-'a']++; cnt[s2[i]-'a']-- }
    if allZero(cnt) { return true }
    for i := len(s1); i < len(s2); i++ {
        cnt[s2[i]-'a']--; cnt[s2[i-len(s1)]-'a']++
        if allZero(cnt) { return true }
    }
    return false
}
func allZero(c [26]int) bool { for _, v := range c { if v != 0 { return false } }; return true }
func main() {
    ok := true
    if !checkInclusion("ab","eidbaooo") { ok=false; fmt.Println("FAIL1") }
    if checkInclusion("ab","eidboaoo") { ok=false; fmt.Println("FAIL2") }
    if !ok { os.Exit(1) }
    fmt.Println("PASS")
}''')

# lc_350 intersect
add("lc_350",
java='''package com.webfault.dsa;
import java.util.*;
class Main {
    static int[] intersect(int[] a,int[] b){ Map<Integer,Integer> m=new HashMap<>(); for(int v:a)m.put(v,m.getOrDefault(v,0)+1); List<Integer> res=new ArrayList<>(); for(int v:b){ if(m.getOrDefault(v,0)>0){res.add(v);m.put(v,m.get(v)-1);} } int[] r=new int[res.size()]; for(int i=0;i<r.length;i++)r[i]=res.get(i); return r; }
    public static void main(String[] args) {
        int[] got=intersect(new int[]{1,2,2,1},new int[]{2,2});
        if(!(got.length==2&&got[0]==2&&got[1]==2)){System.out.println("FAIL");throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''')

# lc_215 findKthLargest
add("lc_215",
go='''package main
import ("fmt";"os")
func findKthLargest(nums []int, k int) int {
    for i := len(nums)/2-1; i>=0; i-- { heapify(nums, i, len(nums)) }
    for i := len(nums)-1; i>=len(nums)-k+1; i-- { nums[0],nums[i]=nums[i],nums[0]; heapify(nums,0,i) }
    return nums[0]
}
func heapify(a []int, i, n int) { l:=2*i+1; r:=2*i+2; m:=i; if l<n&&a[l]>a[m]{m=l}; if r<n&&a[r]>a[m]{m=r}; if m!=i{a[i],a[m]=a[m],a[i];heapify(a,m,n)} }
func main() {
    if got := findKthLargest([]int{3,2,1,5,6,4}, 2); got != 5 { fmt.Println("FAIL", got); os.Exit(1) }
    fmt.Println("PASS")
}''',
java='''package com.webfault.dsa;
class Main {
    static int findKthLargest(int[] nums,int k){ int n=nums.length; for(int i=n/2-1;i>=0;i--)heapify(nums,i,n); for(int i=n-1;i>=n-k+1;i--){int t=nums[0];nums[0]=nums[i];nums[i]=t;heapify(nums,0,i);} return nums[0]; }
    static void heapify(int[] a,int i,int n){ int l=2*i+1,r=2*i+2,m=i; if(l<n&&a[l]>a[m])m=l; if(r<n&&a[r]>a[m])m=r; if(m!=i){int t=a[i];a[i]=a[m];a[m]=t;heapify(a,m,n);} }
    public static void main(String[] args) {
        if(findKthLargest(new int[]{3,2,1,5,6,4},2)!=5){System.out.println("FAIL");throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''',
ts='''export function demo(): void {
    function findKthLargest(nums:number[],k:number):number{ const n=nums.length; for(let i=Math.floor(n/2)-1;i>=0;i--)heapify(nums,i,n); for(let i=n-1;i>=n-k+1;i--){const t=nums[0];nums[0]=nums[i];nums[i]=t;heapify(nums,0,i);} return nums[0]; }
    function heapify(a:number[],i:number,n:number){ let l=2*i+1,r=2*i+2,m=i; if(l<n&&a[l]>a[m])m=l; if(r<n&&a[r]>a[m])m=r; if(m!==i){const t=a[i];a[i]=a[m];a[m]=t;heapify(a,m,n);} }
    if(findKthLargest([3,2,1,5,6,4],2)!==5){console.log("FAIL");throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# lc_313 superUglyNumber
add("lc_313",
go='''package main
import ("fmt";"os")
func nthSuperUglyNumber(n int, primes []int) int {
    dp := make([]int, n+1); dp[1]=1
    idx := make([]int, len(primes))
    for i := 2; i <= n; i++ {
        min := 1<<31-1
        for j := range primes { v := dp[idx[j]+1]*primes[j]; if v < min { min = v } }
        dp[i] = min
        for j := range primes { if dp[idx[j]+1]*primes[j]==min { idx[j]++ } }
    }
    return dp[n]
}
func main() {
    if got := nthSuperUglyNumber(12, []int{2,7,13,19}); got != 32 { fmt.Println("FAIL", got); os.Exit(1) }
    fmt.Println("PASS")
}''',
ts='''export function demo(): void {
    function nthSuperUglyNumber(n:number,primes:number[]):number{ const dp=new Array(n+1); dp[1]=1; const idx=new Array(primes.length).fill(0); for(let i=2;i<=n;i++){ let min=Infinity; for(let j=0;j<primes.length;j++){ const v=dp[idx[j]+1]*primes[j]; if(v<min)min=v; } dp[i]=min; for(let j=0;j<primes.length;j++){ if(dp[idx[j]+1]*primes[j]===min)idx[j]++; } } return dp[n]; }
    if(nthSuperUglyNumber(12,[2,7,13,19])!==32){console.log("FAIL");throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# lc_347 topKFrequent
add("lc_347",
java='''package com.webfault.dsa;
import java.util.*;
class Main {
    static List<Integer> topKFrequent(int[] nums,int k){ Map<Integer,Integer> m=new HashMap<>(); for(int v:nums)m.put(v,m.getOrDefault(v,0)+1); List<Integer>[] bucket=new List[nums.length+1]; for(int key:m.keySet()){ int f=m.get(key); if(bucket[f]==null)bucket[f]=new ArrayList<>(); bucket[f].add(key); } List<Integer> res=new ArrayList<>(); for(int f=bucket.length-1;f>=1&&res.size()<k;f--){ if(bucket[f]!=null)res.addAll(bucket[f]); } return res; }
    public static void main(String[] args) {
        List<Integer> got=topKFrequent(new int[]{1,1,1,2,2,3},2);
        if(got.size()!=2){System.out.println("FAIL");throw new RuntimeException("FAILED");}
        java.util.Set<Integer> s=new HashSet<>(got); if(!s.contains(1)||!s.contains(2)){System.out.println("FAIL2");throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''',
ts='''export function demo(): void {
    function topKFrequent(nums:number[],k:number):number[]{ const m:Record<number,number>={}; for(const v of nums)m[v]=(m[v]||0)+1; const bucket:number[][]=[]; for(const key in m){ const f=m[key]; (bucket[f]=bucket[f]||[]).push(Number(key)); } const res:number[]=[]; for(let f=bucket.length-1;f>=1&&res.length<k;f--){ if(bucket[f])res.push(...bucket[f]); } return res; }
    const got=topKFrequent([1,1,1,2,2,3],2); if(got.length!==2||!(got.includes(1)&&got.includes(2))){console.log("FAIL");throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# lc_496 nextGreaterElement
add("lc_496",
java='''package com.webfault.dsa;
import java.util.*;
class Main {
    static int[] nextGreaterElement(int[] nums1,int[] nums2){ Map<Integer,Integer> m=new HashMap<>(); Stack<Integer> st=new Stack<>(); for(int v:nums2){ while(!st.isEmpty()&&st.peek()<v)m.put(st.pop(),v); st.push(v); } int[] r=new int[nums1.length]; for(int i=0;i<nums1.length;i++)r[i]=m.getOrDefault(nums1[i],-1); return r; }
    public static void main(String[] args) {
        int[] got=nextGreaterElement(new int[]{4,1,2},new int[]{1,3,4,2});
        if(!(got[0]==-1&&got[1]==3&&got[2]==-1)){System.out.println("FAIL "+Arrays.toString(got));throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''',
ts='''export function demo(): void {
    function nextGreaterElement(nums1:number[],nums2:number[]):number[]{ const m:Record<number,number>={}; const st:number[]=[]; for(const v of nums2){ while(st.length&&st[st.length-1]<v)m[st.pop()!]=v; st.push(v); } return nums1.map(x=>m[x]??-1); }
    const got=nextGreaterElement([4,1,2],[1,3,4,2]); if(!(got[0]===-1&&got[1]===3&&got[2]===-1)){console.log("FAIL "+got);throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# lc_150 evalRPN
add("lc_150",
go='''package main
import ("fmt";"os";"strconv")
func evalRPN(tokens []string) int {
    st := []int{}
    for _, t := range tokens {
        v, err := strconv.Atoi(t)
        if err == nil { st = append(st, v); continue }
        b := st[len(st)-1]; st = st[:len(st)-1]; a := st[len(st)-1]; st = st[:len(st)-1]
        switch t { case "+": st = append(st, a+b); case "-": st = append(st, a-b); case "*": st = append(st, a*b); case "/": st = append(st, a/b) }
    }
    return st[0]
}
func main() {
    if evalRPN([]string{"2","1","+","3","*"}) != 9 { fmt.Println("FAIL1"); os.Exit(1) }
    if evalRPN([]string{"4","13","5","/","+"}) != 6 { fmt.Println("FAIL2"); os.Exit(1) }
    fmt.Println("PASS")
}''',
java='''package com.webfault.dsa;
import java.util.*;
class Main {
    static int evalRPN(String[] t){ Stack<Integer> st=new Stack<>(); for(String s:t){ try{ st.push(Integer.parseInt(s)); }catch(Exception e){ int b=st.pop(),a=st.pop(); switch(s){case "+":st.push(a+b);break;case "-":st.push(a-b);break;case "*":st.push(a*b);break;case "/":st.push(a/b);break;} } } return st.pop(); }
    public static void main(String[] args) {
        if(evalRPN(new String[]{"2","1","+","3","*"})!=9){System.out.println("FAIL1");throw new RuntimeException("FAILED");}
        if(evalRPN(new String[]{"4","13","5","/","+"})!=6){System.out.println("FAIL2");throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''')

# lc_556 nextGreaterElement(n)
add("lc_556",
java='''package com.webfault.dsa;
class Main {
    static int nextGreaterElement(int n){ char[] d=String.valueOf(n).toCharArray(); int i=d.length-2; while(i>=0&&d[i]>=d[i+1])i--; if(i<0)return -1; int j=d.length-1; while(d[j]<=d[i])j--; char t=d[i];d[i]=d[j];d[j]=t; for(int l=i+1,r=d.length-1;l<r;l++,r--){ t=d[l];d[l]=d[r];d[r]=t;} long v=Long.parseLong(new String(d)); return v>Integer.MAX_VALUE?(int)-1:(int)v; }
    public static void main(String[] args) {
        if(nextGreaterElement(12)!=21){System.out.println("FAIL");throw new RuntimeException("FAILED");}
        if(nextGreaterElement(21)!=-1){System.out.println("FAIL2");throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''')

# lc_54 spiralOrder
add("lc_54",
go='''package main
import ("fmt";"os")
func spiralOrder(matrix [][]int) []int {
    if len(matrix)==0 { return []int{} }
    r0,c0,r1,c1 := 0,0,len(matrix)-1,len(matrix[0])-1
    res := []int{}
    for r0<=r1 && c0<=c1 {
        for c:=c0;c<=c1;c++ { res=append(res,matrix[r0][c]) }
        for r:=r0+1;r<=r1;r++ { res=append(res,matrix[r][c1]) }
        if r0<r1 { for c:=c1-1;c>=c0;c-- { res=append(res,matrix[r1][c]) } }
        if c0<c1 { for r:=r1-1;r>r0;r-- { res=append(res,matrix[r][c0]) } }
        r0++;r1--;c0++;c1--
    }
    return res
}
func main() {
    m := [][]int{{1,2,3},{4,5,6},{7,8,9}}
    if got := spiralOrder(m); len(got)!=9 || got[0]!=1 || got[8]!=5 { fmt.Println("FAIL", got); os.Exit(1) }
    fmt.Println("PASS")
}''')

# lc_937 reorderLogFiles
add("lc_937",
go='''package main
import ("fmt";"os";"sort";"strings")
func reorderLogFiles(logs []string) []string {
    digits := []string{}; letters := []string{}
    for _, l := range logs {
        sp := strings.Index(l, " ")
        if l[sp+1]>='0' && l[sp+1]<='9' { digits = append(digits, l) } else { letters = append(letters, l) }
    }
    sort.Slice(letters, func(i, j int) bool {
        a := letters[i]; b := letters[j]
        sa, sb := strings.Index(a," "), strings.Index(b," ")
        if a[sa+1:] != b[sb+1:] { return a[sa+1:] < b[sb+1:] }
        return a[:sa] < b[:sb]
    })
    return append(letters, digits...)
}
func main() {
    in := []string{"dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"}
    got := reorderLogFiles(in)
    if got[0] != "let1 art can" || got[1] != "let3 art zero" || got[2] != "let2 own kit dig" { fmt.Println("FAIL", got); os.Exit(1) }
    fmt.Println("PASS")
}''')

# lc_696 countBinarySubstrings
add("lc_696",
java='''package com.webfault.dsa;
class Main {
    static int countBinarySubstrings(String s){ int prev=0,cur=1,res=0; for(int i=1;i<s.length();i++){ if(s.charAt(i)==s.charAt(i-1))cur++; else {prev=cur;cur=1;} if(prev>=cur)res++; } return res; }
    public static void main(String[] args) {
        if(countBinarySubstrings("00110011")!=6){System.out.println("FAIL");throw new RuntimeException("FAILED");}
        if(countBinarySubstrings("10101")!=4){System.out.println("FAIL2");throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''',
ts='''export function demo(): void {
    function countBinarySubstrings(s:string):number{ let prev=0,cur=1,res=0; for(let i=1;i<s.length;i++){ if(s[i]===s[i-1])cur++; else {prev=cur;cur=1;} if(prev>=cur)res++; } return res; }
    if(countBinarySubstrings("00110011")!==6){console.log("FAIL");throw new Error("FAILED");}
    if(countBinarySubstrings("10101")!==4){console.log("FAIL2");throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# lc_791 customSortString
add("lc_791",
ts='''export function demo(): void {
    function customSortString(order:string,s:string):string{ const rank:Record<string,number>={}; for(let i=0;i<order.length;i++)rank[order[i]]=i; return s.split("").sort((a,b)=>(rank[a]??100)-(rank[b]??100)).join(""); }
    if(customSortString("cba","abcd")!=="cbad"){console.log("FAIL "+customSortString("cba","abcd"));throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# lc_557 reverseWords
add("lc_557",
go='''package main
import ("fmt";"os";"strings")
func reverseWords(s string) string {
    words := strings.Fields(s); for i, w := range words { runes := []rune(w); for j:=0;j<len(runes)/2;j++ { runes[j],runes[len(runes)-1-j]=runes[len(runes)-1-j],runes[j] }; words[i]=string(runes) }
    return strings.Join(words, " ")
}
func main() {
    if got := reverseWords("Let's take LeetCode contest"); got != "s'teL ekat edoCteeL tsetnoc" { fmt.Println("FAIL", got); os.Exit(1) }
    fmt.Println("PASS")
}''',
java='''package com.webfault.dsa;
import java.util.*;
class Main {
    static String reverseWords(String s){ String[] w=s.split(" "); StringBuilder sb=new StringBuilder(); for(int i=0;i<w.length;i++){ StringBuilder rev=new StringBuilder(w[i]).reverse(); if(i>0)sb.append(" "); sb.append(rev);} return sb.toString(); }
    public static void main(String[] args) {
        if(!reverseWords("Let's take LeetCode contest").equals("s'teL ekat edoCteeL tsetnoc")){System.out.println("FAIL");throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''',
ts='''export function demo(): void {
    function reverseWords(s:string):string{ return s.split(" ").map(w=>w.split("").reverse().join("")).join(" "); }
    if(reverseWords("Let's take LeetCode contest")!=="s'teL ekat edoCteeL tsetnoc"){console.log("FAIL");throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# lc_482 licenseKeyFormatting
add("lc_482",
go='''package main
import ("fmt";"os";"strings")
func licenseKeyFormatting(s string, k int) string {
    var clean []byte
    for i := 0; i < len(s); i++ { c := s[i]; if c>='a'&&c<='z' { c = c-'a'+'A' }; if c!='-' { clean = append(clean, c) } }
    var res []byte; n := len(clean); cnt := 0
    for i := n-1; i >= 0; i-- {
        if cnt==k { res = append(res, '-'); cnt=0 }
        res = append(res, clean[i]); cnt++
    }
    for i,j := 0,len(res)-1; i<j; i,j=i+1,j-1 { res[i],res[j]=res[j],res[i] }
    return string(res)
}
func main() {
    if got := licenseKeyFormatting("5F3Z-2e-9-w", 4); got != "5F3Z-2E9W" { fmt.Println("FAIL", got); os.Exit(1) }
    fmt.Println("PASS")
}''',
java='''package com.webfault.dsa;
class Main {
    static String licenseKeyFormatting(String s,int k){ StringBuilder clean=new StringBuilder(); for(char c:s.toCharArray()){ if(c=='-')continue; if(c>='a'&&c<='z')c=(char)(c-'a'+'A'); clean.append(c);} StringBuilder res=new StringBuilder(); int cnt=0; for(int i=clean.length()-1;i>=0;i--){ if(cnt==k){res.append('-');cnt=0;} res.append(clean.charAt(i));cnt++; } return res.reverse().toString(); }
    public static void main(String[] args) {
        if(!licenseKeyFormatting("5F3Z-2e-9-w",4).equals("5F3Z-2E9W")){System.out.println("FAIL");throw new RuntimeException("FAILED");}
        System.out.println("PASS");
    }
}''')

# lc_8 myAtoi
add("lc_8",
ts='''export function demo(): void {
    function myAtoi(s:string):number{ let i=0; while(i<s.length&&s[i]===' ')i++; if(i>=s.length)return 0; let sign=1; if(s[i]==='+'||s[i]==='-'){sign=s[i]==='-'?-1:1;i++;} let num=0; while(i<s.length&&s[i]>='0'&&s[i]<='9'){ num=num*10+(s.charCodeAt(i)-48); if(sign*num>2147483647)return 2147483647; if(sign*num<-2147483648)return -2147483648; i++; } return sign*num; }
    if(myAtoi("   -42")!==-42){console.log("FAIL "+myAtoi("   -42"));throw new Error("FAILED");}
    if(myAtoi("4193 with words")!==4193){console.log("FAIL2");throw new Error("FAILED");}
    if(myAtoi("words and 987")!==0){console.log("FAIL3");throw new Error("FAILED");}
    if(myAtoi("-91283472332")!==-2147483648){console.log("FAIL4");throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# lc_451 frequencySort
add("lc_451",
ts='''export function demo(): void {
    function frequencySort(s:string):string{ const m:Record<string,number>={}; for(const c of s)m[c]=(m[c]||0)+1; return s.split("").sort((a,b)=> m[b]-m[a]||(a<b?-1:1)).join(""); }
    const got=frequencySort("tree"); if(got!=="eetr"&&got!=="eert"){console.log("FAIL "+got);throw new Error("FAILED");}
    console.log("PASS");
}
demo();''')

# lc_43 multiply
add("lc_43",
go='''package main
import ("fmt";"os";"strings")
func multiply(num1, num2 string) string {
    if num1=="0"||num2=="0" { return "0" }
    n1,n2 := len(num1),len(num2); res := make([]int, n1+n2)
    for i:=n1-1;i>=0;i-- { for j:=n2-1;j>=0;j-- { p:=(num1[i]-'0')*(num2[j]-'0')+res[i+j+1]; res[i+j+1]=p%10; res[i+j]+=p/10 } }
    var sb strings.Builder
    for i, v := range res { if i==0 && v==0 { continue }; sb.WriteByte(byte(v+'0')) }
    return sb.String()
}
func main() {
    if got := multiply("123","456"); got != "56088" { fmt.Println("FAIL", got); os.Exit(1) }
    fmt.Println("PASS")
}''')

# ============================ END BATCH 4 (part 1) ============================

def main():
    ch5 = json.load(open(os.path.join(BASE, "_tools/scale_chunks.json")))["chunks"][5]
    done = load_progress()
    stats = {"done_pass": 0, "fail": 0, "skip": 0}
    for p in ch5:
        if p in done:
            s = done[p]
            stats[s] = stats.get(s, 0) + 1
            continue
        lang = p.split(".")[-1]
        lc = re.search(r"/(lc_\d+)_", p).group(1)
        full = os.path.join(BASE, p)
        if lc in SOL and lang in SOL[lc]:
            try:
                with open(full, "w") as f:
                    f.write(SOL[lc][lang])
            except Exception as e:
                record(p, "fail", "write error: %s" % e)
                stats["fail"] += 1
                continue
            ok, r = verify(full)
            if ok:
                record(p, "done_pass", "verified")
                stats["done_pass"] += 1
            else:
                note = (r.stdout + r.stderr)[:300]
                record(p, "fail", note)
                stats["fail"] += 1
        else:
            # not yet authored -> leave unrecorded so it stays resumable
            pass
    print("STATS", stats)

if __name__ == "__main__":
    main()
