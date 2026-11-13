-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107524703
-- LeetCode 107524703. 人鬼渡河问题 — Lua 版（方案1：安全判定谓词）
local function is_safe(r, g) -- local function is_safe(右指针, g)
	return 0 <= r and r <= 3 and 0 <= g and g <= 3 and (r == 0 or r == 3 or r == g)
end -- 终点

local cases = { -- 把 { 写入 local cases
	{ 3, 3, true },
	{ 3, 1, true },
	{ 2, 2, true },
	{ 1, 3, false },
	{ 0, 0, true },
}
for idx, c in ipairs(cases) do -- 遍历取 字符
	assert(is_safe(c[1], c[2]) == c[3], "is_safe(" .. c[1] .. "," .. c[2] .. ") failed") -- 断言校验
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
