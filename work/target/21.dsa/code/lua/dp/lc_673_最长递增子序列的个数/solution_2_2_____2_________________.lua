-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130771847
-- LeetCode 673. 最长递增子序列的个数 — Lua 版（方案2）
local function find_number_of_lis(nums) -- local function find_number_of_lis(数组)
	local n = #nums -- 把 #数组 写入 local n
	local dp, cnt = {}, {} -- 把 {}, {} 写入 local dp, cnt
	for i = 1, n do
		dp[i] = 1
		cnt[i] = 1
	end -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
	local best, res = 0, 0 -- 把 0, 0 写入 local best, res
	for i = 1, n do -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
		for j = 1, i - 1 do -- 让 下标 j 从 1 走到 下标 i（Lua 1 基）
			if nums[j] < nums[i] then -- 若 数组[下标 j] 小于 数组[下标 i] then
				if dp[j] + 1 > dp[i] then
					dp[i] = dp[j] + 1
					cnt[i] = cnt[j]
				elseif dp[j] + 1 == dp[i] then
					cnt[i] = cnt[i] + cnt[j]
				end
			end -- 终点
		end -- 终点
		if dp[i] > best then
			best = dp[i]
			res = cnt[i]
		elseif dp[i] == best then
			res = res + cnt[i]
		end -- 把 赋值为 当前最优 then 结果 赋值为 结果 加 计数[下标 i] 终点 写入 elseif dp[i]
	end -- 终点
	return res -- 返回 结果
end -- 终点
assert(find_number_of_lis({ 1, 3, 5, 4, 7 }) == 2) -- 断言校验
assert(find_number_of_lis({ 2, 2, 2, 2, 2 }) == 5) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
