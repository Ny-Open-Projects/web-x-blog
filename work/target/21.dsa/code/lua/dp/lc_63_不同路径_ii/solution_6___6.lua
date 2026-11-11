-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130704336
-- LeetCode 63. 不同路径II — Lua 版（方案6）
local function unique_paths_with_obstacles(grid) -- local function unique_paths_with_obstacles(网格)
	local m, n = #grid, #grid[1] -- 把 #网格, #网格[1] 写入 local m, n
	local dp = {} -- 把 {} 写入 local dp
	for j = 1, n do
		dp[j] = 0
	end -- 让 下标 j 从 1 走到 元素个数（Lua 1 基）
	dp[1] = grid[1][1] == 1 and 0 or 1 -- 把 网格[1][1] 等于 1 and 0 or 1 写入 dp[1]
	for i = 1, m do -- 让 下标 i 从 1 走到 映射表（Lua 1 基）
		for j = 1, n do -- 让 下标 j 从 1 走到 元素个数（Lua 1 基）
			if grid[i][j] == 1 then
				dp[j] = 0 -- 若 网格[下标 i][下标 j] 等于 1 then DP 表[下标 j] 赋值为 0
			elseif j > 1 then
				dp[j] = dp[j] + dp[j - 1]
			end -- 把 DP 表[下标 j] 加 DP 表[下标 j 减 1] 终点 写入 elseif j > 1 then dp[j]
		end -- 终点
	end -- 终点
	return dp[n] -- 返回 DP 表[元素个数]
end -- 终点
assert(unique_paths_with_obstacles({ { 0, 0, 0 }, { 0, 1, 0 }, { 0, 0, 0 } }) == 2) -- 断言校验
assert(unique_paths_with_obstacles({ { 0, 1 }, { 0, 0 } }) == 1) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
