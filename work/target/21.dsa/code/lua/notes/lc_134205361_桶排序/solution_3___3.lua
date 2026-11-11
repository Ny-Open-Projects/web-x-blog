-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134205361
-- 数据结构与算法之排序: 桶排序 — Lua 版（方案3）
local function get_index(arr, k) -- local function get_index(数组, 下标 k)
	for _, v in ipairs(arr) do -- 遍历取 值
		if v == k then
			return k
		end -- 若 值 等于 下标 k then return 下标 k 终点
	end -- 终点
	return -1 -- 返回 减 1
end -- 终点
assert(get_index({ 1, 2, 3 }, 1) == 1) -- 断言校验
assert(get_index({ 1, 2, 3 }, 2) == 2) -- 断言校验
assert(get_index({ 1, 2, 3 }, 3) == 3) -- 断言校验
assert(get_index({ 3, 1, 2 }, 2) == 2) -- 断言校验
assert(get_index({ 1, 2, 3 }, 5) == -1) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
