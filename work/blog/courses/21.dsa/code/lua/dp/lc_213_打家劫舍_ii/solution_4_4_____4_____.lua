-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130716392
-- LeetCode 213. 打家劫舍II — Lua 版（方案4）
local function rob_line(nums)
	local a, b = 0, 0
	for _, v in ipairs(nums) do
		a, b = b, math.max(b, a + v)
	end
	return b
end
local function rob_ii(nums) -- local function rob_ii(数组)
	if #nums == 1 then
		return nums[1]
	end -- 若 #数组 等于 1 then return 数组[1] 终点
	local skip_first, skip_last = {}, {} -- 把 {}, {} 写入 local skip_first, skip_last
	for i = 2, #nums do
		skip_first[#skip_first + 1] = nums[i]
	end
	for i = 1, #nums - 1 do
		skip_last[#skip_last + 1] = nums[i]
	end
	return math.max(rob_line(skip_first), rob_line(skip_last)) -- 返回 math.取较大值 rob_line(skip_first), rob_line(skip_last))
end -- 终点
assert(rob_ii({ 2, 3, 2 }) == 3) -- 断言校验
assert(rob_ii({ 1, 2, 3, 1 }) == 4) -- 断言校验
assert(rob_ii({ 1 }) == 1) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
