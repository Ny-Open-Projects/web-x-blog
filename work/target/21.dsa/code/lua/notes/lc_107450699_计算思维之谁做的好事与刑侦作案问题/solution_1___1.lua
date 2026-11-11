-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107450699
-- 计算思维之谁做的好事 — Lua 版（方案1）
local function find_good_man() -- local function find_good_man()
	for _, m in ipairs({ "A", "B", "C", "D" }) do -- 遍历取 映射表
		local t = 0 -- 把 0 写入 local t
		if m ~= "A" then
			t = t + 1
		end -- 若 映射表 ~ 赋值为 「A」 then 另一字符串 赋值为 另一字符串 加 1 终点
		if m == "C" then
			t = t + 1
		end -- 若 映射表 等于 「C」 then 另一字符串 赋值为 另一字符串 加 1 终点
		if m == "D" then
			t = t + 1
		end -- 若 映射表 等于 「D」 then 另一字符串 赋值为 另一字符串 加 1 终点
		if m ~= "D" then
			t = t + 1
		end -- 若 映射表 ~ 赋值为 「D」 then 另一字符串 赋值为 另一字符串 加 1 终点
		if t == 3 then
			return m
		end -- 若 另一字符串 等于 3 then return 映射表 终点
	end -- 终点
	return "?" -- 返回 「?」
end -- 终点
assert(find_good_man() == "C") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
