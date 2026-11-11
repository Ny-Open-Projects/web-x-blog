import os

base78 = "/Users/Wang/Code/github/web-x-blog/work/target/21.dsa/ts/backtrack/lc_78_子集"
base213 = "/Users/Wang/Code/github/web-x-blog/work/target/21.dsa/ts/dp/lc_213_打家劫舍_ii"

def ts78(body, name):
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
    const want = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]];
    const got = subsets([1, 2, 3]);
    let fail = false;
    if (!eqSet(got, want)) { fail = true; console.log("FAIL subsets got=" + JSON.stringify(got)); }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();
''' % body

backtrack = '''    function subsets(nums: number[]): number[][] {
        const result: number[][] = [];
        const path: number[] = [];
        function backtrack(start: number) {
            result.push(path.slice());
            for (let i = start; i < nums.length; i++) {
                path.push(nums[i]);
                backtrack(i + 1);
                path.pop();
            }
        }
        backtrack(0);
        return result;
    }'''

iterative = '''    function subsets(nums: number[]): number[][] {
        const res: number[][] = [[]];
        for (const num of nums) {
            const sz = res.length;
            for (let i = 0; i < sz; i++) {
                res.push(res[i].concat([num]));
            }
        }
        return res;
    }'''

mapping78 = {
    "solution_1___1.ts": ts78(backtrack, "S1"),
    "solution_2___2.ts": ts78(backtrack, "S2"),
    "solution_3___3.ts": ts78(iterative, "S3"),
}

def ts213(body):
    return '''export function demo(): void {
%s
    const cases = [
        { in: [2, 3, 2], want: 3 },
        { in: [1, 2, 3, 1], want: 4 },
        { in: [5], want: 5 },
        { in: [], want: 0 },
    ];
    let fail = false;
    for (const c of cases) {
        const got = rob(c.in);
        if (got !== c.want) { fail = true; console.log("FAIL rob(" + JSON.stringify(c.in) + ")=" + got + " want " + c.want); }
    }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();
''' % body

body213_1 = '''    function rob(nums: number[]): number {
        const n = nums.length;
        if (n === 0) return 0;
        if (n === 1) return nums[0];
        const dp1 = new Array(n).fill(0);
        const dp2 = new Array(n).fill(0);
        dp1[0] = nums[0];
        dp1[1] = Math.max(nums[0], nums[1]);
        dp2[1] = nums[1];
        for (let i = 2; i < n; i++) dp1[i] = Math.max(dp1[i - 1], dp1[i - 2] + nums[i]);
        for (let i = 2; i < n - 1; i++) dp2[i] = Math.max(dp2[i - 1], dp2[i - 2] + nums[i]);
        return Math.max(dp1[n - 2], dp2[n - 1]);
    }'''

body213_2 = '''    function rob(nums: number[]): number {
        const length = nums.length;
        if (length === 0) return 0;
        if (length === 1) return nums[0];
        function robRange(start: number, end: number): number {
            if (end === start) return nums[start];
            const dp = new Array(end + 1).fill(0);
            dp[start] = nums[start];
            dp[start + 1] = Math.max(nums[start], nums[start + 1]);
            for (let i = start + 2; i <= end; i++) dp[i] = Math.max(dp[i - 2] + nums[i], dp[i - 1]);
            return dp[end];
        }
        return Math.max(robRange(0, length - 2), robRange(1, length - 1));
    }'''

body213_4 = '''    function rob(nums: number[]): number {
        const n = nums.length;
        if (n === 0) return 0;
        if (n === 1) return nums[0];
        function helper(arr: number[]): number {
            let f0 = 0, f1 = 0;
            for (const x of arr) { const nf = Math.max(f1, f0 + x); f0 = f1; f1 = nf; }
            return f1;
        }
        return Math.max(nums[0] + helper(nums.slice(2, n - 1)), helper(nums.slice(1, n)));
    }'''

mapping213 = {
    "solution_1_1_____1_____.ts": ts213(body213_1),
    "solution_2_2_____2_____.ts": ts213(body213_2),
    "solution_4_4_____4_____.ts": ts213(body213_4),
}

for fn, content in mapping78.items():
    with open(os.path.join(base78, fn), "w") as f:
        f.write(content)
for fn, content in mapping213.items():
    with open(os.path.join(base213, fn), "w") as f:
        f.write(content)
print("wrote", len(mapping78) + len(mapping213))
