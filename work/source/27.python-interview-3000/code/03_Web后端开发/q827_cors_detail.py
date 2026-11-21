
def cors_headers(origin: str, allowlist: set, with_credentials: bool) -> dict:
    if origin in allowlist:
        h = {"Access-Control-Allow-Origin": origin}
        if with_credentials:
            h["Access-Control-Allow-Credentials"] = "true"
            h["Vary"] = "Origin"
        return h
    return {}   # 不命中白名单就不放行

print(cors_headers("https://app.example.com", {"https://app.example.com"}, True))
print(cors_headers("https://evil.example.net", {"https://app.example.com"}, True))
