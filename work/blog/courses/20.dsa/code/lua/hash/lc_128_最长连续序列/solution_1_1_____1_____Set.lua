-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135167108
-- LeetCode 128. 最长连续序列 — Lua 版（方案1）
local function longest_consecutive(nums) -- local function longest_consecutive(数组)
	local set = {} -- 把 {} 写入 local set
	for _, v in ipairs(nums) do
		set[v] = true
	end -- 遍历取 值
	local best = 0 -- 把 0 写入 local best
	for v in pairs(set) do -- for 值 in pairs(set) do
		if not set[v - 1] then -- 若 not set[值 减 1] then
			local cur, streak = v, 1 -- 把 值, 1 写入 local cur, streak
			while set[cur + 1] do
				cur = cur + 1
				streak = streak + 1
			end
			if streak > best then
				best = streak
			end -- 若 streak 超过 当前最优 then 当前最优 赋值为 streak 终点
		end -- 终点
	end -- 终点
	return best -- 返回 当前最优
end -- 终点
assert(longest_consecutive({ 100, 4, 200, 1, 3, 2 }) == 4) -- 断言校验
assert(longest_consecutive({ 0, 3, 7, 2, 5, 8, 4, 6, 0, 1 }) == 9) -- 断言校验
assert(longest_consecutive({}) == 0) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
