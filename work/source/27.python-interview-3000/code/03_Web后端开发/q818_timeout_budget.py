
limits = {"gateway": 3000, "app": 2500, "rpc": 2000, "db": 800}
ok = limits["db"] <= limits["rpc"] <= limits["app"] <= limits["gateway"]
print("嵌套预算合法:", ok)
for layer, ms in limits.items():
    print(f"{layer}: {ms}ms")
