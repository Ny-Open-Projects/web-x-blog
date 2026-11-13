-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134424807
-- LeetCode 485. 最大连续1的个数 — Lua 版（方案1）
local function find_max_consecutive_ones(nums) -- local function find_max_consecutive_ones(数组)
	local best, cur = 0, 0 -- 把 0, 0 写入 local best, cur
	for _, v in ipairs(nums) do -- 遍历取 值
		if v == 1 then
			cur = cur + 1
			if cur > best then
				best = cur
			end
		else
			cur = 0
		end -- 否则
	end -- 终点
	return best -- 返回 当前最优
end -- 终点
assert(find_max_consecutive_ones({ 1, 1, 0, 1, 1, 1 }) == 3) -- 断言校验
assert(find_max_consecutive_ones({ 1, 0, 1, 1, 0, 1 }) == 2) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
