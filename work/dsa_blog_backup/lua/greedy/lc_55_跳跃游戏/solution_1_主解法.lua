-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133844403
-- LeetCode 55. 跳跃游戏 — Lua 版（方案1）
local function can_jump(nums) -- local function can_jump(数组)
	local max_reach = 0 -- 把 0 写入 local max_reach
	for i = 1, #nums do -- 把 1, #数组 do 写入 for i
		if i - 1 > max_reach then
			return false
		end -- 若 下标 i 减 1 超过 max_reach then return false 终点
		local r = (i - 1) + nums[i] -- 把 (下标 i 减 1) 加 数组[下标 i] 写入 local r
		if r > max_reach then
			max_reach = r
		end -- 若 右指针 超过 max_reach then max_reach 赋值为 右指针 终点
	end -- 终点
	return true -- 返回 true
end -- 终点
assert(can_jump({ 2, 3, 1, 1, 4 }) == true) -- 断言校验
assert(can_jump({ 3, 2, 1, 0, 4 }) == false) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
