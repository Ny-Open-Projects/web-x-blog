-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133834060
-- LeetCode 2407. 最长递增子序列II — Lua 版（方案1）
local function length_of_lis(nums, k) -- local function length_of_lis(数组, 下标 k)
	local n = #nums -- 把 #数组 写入 local n
	local dp = {} -- 把 {} 写入 local dp
	for i = 1, n do
		dp[i] = 1
	end -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
	local best = 0 -- 把 0 写入 local best
	for i = 1, n do -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
		for j = 1, i - 1 do -- 让 下标 j 从 1 走到 下标 i（Lua 1 基）
			if nums[j] < nums[i] and nums[i] - nums[j] <= k then -- 若 数组[下标 j] 小于 数组[下标 i] and 数组[下标 i] 减 数组[下标 j] 不超过 下标 k then
				if dp[j] + 1 > dp[i] then
					dp[i] = dp[j] + 1
				end
			end -- 终点
		end -- 终点
		if dp[i] > best then
			best = dp[i]
		end -- 若 DP 表[下标 i] 超过 当前最优 then 当前最优 赋值为 DP 表[下标 i] 终点
	end -- 终点
	return best -- 返回 当前最优
end -- 终点
assert(length_of_lis({ 4, 2, 1, 4, 3, 4, 5, 8, 15 }, 3) == 5) -- 断言校验
assert(length_of_lis({ 1 }, 1) == 1) -- 断言校验
assert(length_of_lis({}, 3) == 0) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
