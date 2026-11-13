-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134577890
-- LeetCode 179. 最大数 — Lua 版（方案2）
local function largest_number(nums) -- local function largest_number(数组)
	local strs = {} -- 把 {} 写入 local strs
	for i, v in ipairs(nums) do
		strs[i] = tostring(v)
	end -- 遍历取 值
	table.sort(strs, function(a, b) -- 排序
		return a .. b > b .. a -- 返回 数组 .. b 超过 b .. 数组
	end) -- 终点)
	if strs[1] == "0" then
		return "0"
	end -- 若 strs[1] 等于 「0」 then return 「0」 终点
	return table.concat(strs) -- 返回 table.concat(strs)
end -- 终点
assert(largest_number({ 10, 2 }) == "210") -- 断言校验
assert(largest_number({ 3, 30, 34, 5, 9 }) == "9534330") -- 断言校验
assert(largest_number({ 0, 0 }) == "0") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
