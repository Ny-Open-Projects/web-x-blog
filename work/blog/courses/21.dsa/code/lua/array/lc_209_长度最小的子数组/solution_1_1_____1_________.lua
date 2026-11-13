-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133807379
-- LeetCode 209. 长度最小的子数组 — Lua 版（方案1）
local function min_sub_array_len(target, nums) -- local function min_sub_array_len(目标值, 数组)
	local l, sum, best = 1, 0, math.huge -- 把 1, 0, math.huge 写入 local l, sum, best
	for r = 1, #nums do -- 把 1, #数组 do 写入 for r
		sum = sum + nums[r] -- 把 累计和 加 数组[右指针] 存入 累计和
		while sum >= target do -- 把 目标值 do 写入 while sum >
			if r - l + 1 < best then
				best = r - l + 1
			end -- 若 右指针 减 左指针 加 1 小于 当前最优 then 当前最优 赋值为 右指针 减 左指针 加 1 终点
			sum = sum - nums[l] -- 把 累计和 减 数组[左指针] 存入 累计和
			l = l + 1 -- 把 左指针 加 1 存入 左指针
		end -- 终点
	end -- 终点
	if best == math.huge then
		return 0
	end -- 若 当前最优 等于 math.huge then return 0 终点
	return best -- 返回 当前最优
end -- 终点
assert(min_sub_array_len(7, { 2, 3, 1, 2, 4, 3 }) == 2) -- 断言校验
assert(min_sub_array_len(4, { 1, 4, 4 }) == 1) -- 断言校验
assert(min_sub_array_len(11, { 1, 1, 1, 1, 1, 1, 1, 1 }) == 0) -- 断言校验
assert(min_sub_array_len(1, { 1, 2, 3 }) == 1) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
