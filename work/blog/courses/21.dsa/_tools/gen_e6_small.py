import os

base556 = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/21.dsa/ts/stack/lc_556_下一个更大元素_iii"
base435 = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/21.dsa/ts/greedy/lc_435_无重叠区间"
base46 = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/21.dsa/ts/backtrack/lc_46_全排列"

# ---- lc_556 ----
body556_1 = '''    function nextGreaterElement(n: number): number {
        const MAX = 2147483647;
        let nums = String(n).split('');
        let i = nums.length - 2;
        while (i >= 0 && nums[i] >= nums[i + 1]) i--;
        if (i < 0) return -1;
        let j = nums.length - 1;
        while (nums[j] <= nums[i]) j--;
        const t = nums[i]; nums[i] = nums[j]; nums[j] = t;
        let left = i + 1, right = nums.length - 1;
        while (left < right) { const tt = nums[left]; nums[left] = nums[right]; nums[right] = tt; left++; right--; }
        const ans = parseInt(nums.join(''), 10);
        return ans <= MAX ? ans : -1;
    }'''

body556_2 = '''    function nextGreaterElement(n: number): number {
        const MAX = 2147483647;
        let x = n; let cnt = 1;
        while (x >= 10 && Math.floor(x / 10) % 10 >= x % 10) { x = Math.floor(x / 10); cnt++; }
        x = Math.floor(x / 10);
        if (x === 0) return -1;
        const target_digit = x % 10;
        let x2 = n; let cnt2 = 0;
        while (x2 % 10 <= target_digit) { x2 = Math.floor(x2 / 10); cnt2++; }
        const d = x2 % 10;
        let result = Math.floor(n / Math.pow(10, cnt)) * Math.pow(10, cnt);
        result += d * Math.pow(10, cnt - 1);
        result += n % Math.pow(10, cnt2 - 1);
        if (result > MAX || result <= n) return -1;
        return result;
    }'''

def ts556(body, cases):
    return '''export function demo(): void {
%s
    const cases = [
%s
    ];
    let fail = false;
    for (const c of cases) {
        const got = nextGreaterElement(c.in);
        if (got !== c.want) { fail = true; console.log("FAIL nextGreaterElement(" + c.in + ")=" + got + " want " + c.want); }
    }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();
''' % (body, cases)

cases1 = '''        { in: 1, want: -1 },
        { in: 12, want: 21 },
        { in: 21, want: -1 },
        { in: 123, want: 132 },
        { in: 321, want: -1 },
        { in: 1234, want: 1243 },
        { in: 4321, want: -1 },
        { in: 230241, want: 230412 },
        { in: 1999999999, want: -1 }'''

cases2 = '''        { in: 1, want: -1 },
        { in: 21, want: -1 },
        { in: 321, want: -1 },
        { in: 4321, want: -1 },
        { in: 1999999999, want: -1 }'''

with open(os.path.join(base556, "solution_1_1_____1______.ts"), "w") as f:
    f.write(ts556(body556_1, cases1))
with open(os.path.join(base556, "solution_2_2_____2___.ts"), "w") as f:
    f.write(ts556(body556_2, cases2))

# ---- lc_435 ----
body435 = '''    function eraseOverlapIntervals(intervals: number[][][] | null): number {
        if (!intervals || intervals.length === 0) return 0;
        const arr = intervals.slice().sort((a, b) => a[1] - b[1]);
        let count = 1;
        let end = arr[0][1];
        for (let i = 1; i < arr.length; i++) {
            if (arr[i][0] >= end) { count++; end = arr[i][1]; }
        }
        return arr.length - count;
    }'''

ts435 = '''export function demo(): void {
%s
    const cases = [
        { in: [[1, 2], [2, 3], [3, 4], [1, 3]], want: 1 },
        { in: [], want: 0 },
        { in: [[1, 2], [1, 3], [1, 4]], want: 2 },
        { in: null, want: 0 },
    ];
    let fail = false;
    for (const c of cases) {
        const got = eraseOverlapIntervals(c.in);
        if (got !== c.want) { fail = true; console.log("FAIL eraseOverlapIntervals(" + JSON.stringify(c.in) + ")=" + got + " want " + c.want); }
    }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();
''' % body435

with open(os.path.join(base435, "solution_1_1_____1____.ts"), "w") as f:
    f.write(ts435)
with open(os.path.join(base435, "solution_2_2_____2_____________.ts"), "w") as f:
    f.write(ts435)

# ---- lc_46 ----
body46_1 = '''    function permute(nums: number[]): number[][] {
        const res: number[][] = [];
        function backtrack(path: number[]) {
            if (path.length === nums.length) { res.push(path.slice()); return; }
            for (let i = 0; i < nums.length; i++) {
                if (path.indexOf(nums[i]) !== -1) continue;
                backtrack(path.concat([nums[i]]));
            }
        }
        backtrack([]);
        return res;
    }'''

body46_swap = '''    function permute(nums: number[]): number[][] {
        const res: number[][] = [];
        const a = nums.slice();
        function backtrack(start: number) {
            if (start === a.length) { res.push(a.slice()); return; }
            for (let i = start; i < a.length; i++) {
                const t = a[start]; a[start] = a[i]; a[i] = t;
                backtrack(start + 1);
                const t2 = a[start]; a[start] = a[i]; a[i] = t2;
            }
        }
        backtrack(0);
        return res;
    }'''

body46_used = '''    function permute(nums: number[]): number[][] {
        const res: number[][] = [];
        const used: boolean[] = new Array(nums.length).fill(false);
        function backtrack(path: number[]) {
            if (path.length === nums.length) { res.push(path.slice()); return; }
            for (let i = 0; i < nums.length; i++) {
                if (used[i]) continue;
                used[i] = true;
                path.push(nums[i]);
                backtrack(path);
                path.pop();
                used[i] = false;
            }
        }
        backtrack([]);
        return res;
    }'''

def ts46(body):
    return '''export function demo(): void {
%s
    function eqSet(a: number[][], b: number[][]): boolean {
        if (a.length !== b.length) return false;
        const key = (x: number[]) => x.slice().sort((p, q) => p - q).join(",");
        const sa = new Set(a.map(key));
        const sb = new Set(b.map(key));
        if (sa.size !== sb.size) return false;
        for (const k of sa) if (!sb.has(k)) return false;
        return true;
    }
    const want = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]];
    const got = permute([1, 2, 3]);
    let fail = false;
    if (!eqSet(got, want)) { fail = true; console.log("FAIL permute got=" + JSON.stringify(got)); }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();
''' % body

mapping46 = {
    "solution_1___1.ts": body46_1,
    "solution_2___2.ts": body46_swap,
    "solution_3___3.ts": body46_used,
    "solution_4___4.ts": body46_swap,
    "solution_5___5.ts": body46_used,
    "solution_6___6.ts": body46_swap,
}
for fn, body in mapping46.items():
    with open(os.path.join(base46, fn), "w") as f:
        f.write(ts46(body))

print("wrote lc_556, lc_435, lc_46")
