-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145582435
-- LeetCode 3105. 最长的严格递增或递减子数组 — Lua 版（方案2）
local function longest_monotonic_subarray(nums) -- local function longest_monotonic_subarray(数组)
	if #nums == 0 then
		return 0
	end -- 若 #数组 等于 0 then return 0 终点
	local inc, dec, best = 1, 1, 1 -- 把 1, 1, 1 写入 local inc, dec, best
	for i = 2, #nums do -- 把 2, #数组 do 写入 for i
		if nums[i] > nums[i - 1] then
			inc = inc + 1
			dec = 1 -- 若 数组[下标 i] 超过 数组[下标 i 减 1] then inc 赋值为 inc 加 1; dec 赋值为 1
		elseif nums[i] < nums[i - 1] then
			dec = dec + 1
			inc = 1
		else
			inc = 1
			dec = 1
		end -- 否则
		if inc > best then
			best = inc
		end -- 若 inc 超过 当前最优 then 当前最优 赋值为 inc 终点
		if dec > best then
			best = dec
		end -- 若 dec 超过 当前最优 then 当前最优 赋值为 dec 终点
	end -- 终点
	return best -- 返回 当前最优
end -- 终点
assert(longest_monotonic_subarray({ 1, 2, 3, 4, 5 }) == 5) -- 断言校验
assert(longest_monotonic_subarray({ 5, 4, 3, 2, 1 }) == 5) -- 断言校验
assert(longest_monotonic_subarray({ 1, 4, 3, 2, 5 }) == 3) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
