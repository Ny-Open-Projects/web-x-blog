-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134066015
-- LeetCode 41. 缺失的第一个正数 — Lua 版（方案5）
local function first_missing_positive(nums) -- local function first_missing_positive(数组)
	if #nums == 0 then
		return 1
	end -- 若 #数组 等于 0 then return 1 终点
	local pos = {} -- 把 {} 写入 local pos
	for _, v in ipairs(nums) do -- 遍历取 值
		if v > 0 then
			pos[#pos + 1] = v
		end -- 若 值 超过 0 then pos[#pos 加 1] 赋值为 值 终点
	end -- 终点
	if #pos == 0 then
		return 1
	end -- 若 #pos 等于 0 then return 1 终点
	table.sort(pos) -- 排序
	if pos[1] ~= 1 then
		return 1
	end -- 若 pos[1] ~ 赋值为 1 then return 1 终点
	local n = #pos -- 把 #pos 写入 local n
	for i = 1, n - 1 do -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
		if pos[i + 1] - pos[i] > 1 then
			return pos[i] + 1
		end
	end -- 终点
	return pos[n] + 1 -- 返回 pos[元素个数] 加 1
end -- 终点
assert(first_missing_positive({ 1, 2, 0 }) == 3) -- 断言校验
assert(first_missing_positive({ 3, 4, -1, 1 }) == 2) -- 断言校验
assert(first_missing_positive({ 7, 8, 9, 11, 12 }) == 1) -- 断言校验
assert(first_missing_positive({}) == 1) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
