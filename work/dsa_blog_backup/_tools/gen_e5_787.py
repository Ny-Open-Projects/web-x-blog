import os

base = "/Users/Wang/Code/webfault-ai/dsa/ts/dp/lc_787_k_站中转内最便宜的航班"

def wrap(body):
    return '''export function demo(): void {
%s
    const cases = [
        { n: 4, flights: [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], src: 0, dst: 3, k: 1, want: 700 },
        { n: 4, flights: [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], src: 0, dst: 0, k: 1, want: 0 },
        { n: 3, flights: [[0, 1, 1], [1, 2, 1]], src: 0, dst: 2, k: 1, want: 2 },
        { n: 3, flights: [[0, 1, 1]], src: 0, dst: 2, k: 1, want: -1 },
    ];
    let fail = false;
    for (const c of cases) {
        const got = findCheapestPrice(c.n, c.flights, c.src, c.dst, c.k);
        if (got !== c.want) { fail = true; console.log("FAIL findCheapestPrice n=" + c.n + " want " + c.want + " got " + got); }
    }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();
''' % body

body_dp2d = '''    function findCheapestPrice(n: number, flights: number[][], src: number, dst: number, k: number): number {
        const INF = Infinity;
        const dp: number[][] = [];
        for (let i = 0; i < k + 2; i++) dp.push(new Array(n).fill(INF));
        for (let i = 0; i < k + 2; i++) dp[i][src] = 0;
        for (let i = 1; i <= k + 1; i++) {
            for (const f of flights) {
                const frm = f[0], to = f[1], price = f[2];
                if (dp[i - 1][frm] !== INF) dp[i][to] = Math.min(dp[i][to], dp[i - 1][frm] + price);
            }
        }
        let ans = INF;
        for (let i = 1; i <= k + 1; i++) ans = Math.min(ans, dp[i][dst]);
        return ans === INF ? -1 : ans;
    }'''

body_bellman = '''    function findCheapestPrice(n: number, flights: number[][], src: number, dst: number, k: number): number {
        const INF = Infinity;
        const dist: number[] = new Array(n).fill(INF);
        dist[src] = 0;
        for (let pass = 0; pass < k + 1; pass++) {
            const prev = dist.slice();
            for (const f of flights) {
                const frm = f[0], to = f[1], price = f[2];
                if (prev[frm] !== INF) dist[to] = Math.min(dist[to], prev[frm] + price);
            }
        }
        return dist[dst] === INF ? -1 : dist[dst];
    }'''

body_dfs = '''    function findCheapestPrice(n: number, flights: number[][], src: number, dst: number, k: number): number {
        const INF = Infinity;
        const graph: { [k: number]: number[][] } = {};
        for (const f of flights) {
            const frm = f[0], to = f[1], price = f[2];
            if (!graph[frm]) graph[frm] = [];
            graph[frm].push([to, price]);
        }
        const memo: { [k: string]: number } = {};
        function dfs(city: number, rem: number): number {
            if (city === dst) return 0;
            if (rem === 0) return INF;
            const key = city + "," + rem;
            if (memo[key] !== undefined) return memo[key];
            let best = INF;
            const edges = graph[city] || [];
            for (const e of edges) {
                const to = e[0], price = e[1];
                const nxt = dfs(to, rem - 1);
                if (nxt !== INF) best = Math.min(best, price + nxt);
            }
            memo[key] = best;
            return best;
        }
        const res = dfs(src, k + 1);
        return res === INF ? -1 : res;
    }'''

body_adj = '''    function findCheapestPrice(n: number, flights: number[][], src: number, dst: number, k: number): number {
        const INF = Infinity;
        const w: number[][] = [];
        for (let i = 0; i < n; i++) { w.push(new Array(n).fill(INF)); w[i][i] = 0; }
        for (const f of flights) { w[f[0]][f[1]] = f[2]; }
        const dist: number[] = new Array(n).fill(INF);
        dist[src] = 0;
        for (let pass = 0; pass < k + 1; pass++) {
            const prev = dist.slice();
            for (let i = 0; i < n; i++) {
                if (prev[i] === INF) continue;
                for (let j = 0; j < n; j++) {
                    if (prev[i] + w[i][j] < dist[j]) dist[j] = prev[i] + w[i][j];
                }
            }
        }
        return dist[dst] === INF ? -1 : dist[dst];
    }'''

mapping = {
    "solution_1___1.ts": body_dp2d,
    "solution_3___3.ts": body_dfs,
    "solution_5___5.ts": body_adj,
}
for n in [2, 4, 6, 7, 8, 9, 10, 11]:
    mapping["solution_%d___%d.ts" % (n, n)] = body_bellman

for fn, body in mapping.items():
    with open(os.path.join(base, fn), "w") as f:
        f.write(wrap(body))
print("wrote", len(mapping))
