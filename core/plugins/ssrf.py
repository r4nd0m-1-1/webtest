import aiohttp

async def scan(url, config):
    print(f"[SSRF] Scanning {url}")
    payload = "http://127.0.0.1:80"
    test_url = f"{url}?url={payload}"
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(test_url, timeout=config['timeout']) as resp:
                if resp.status == 200:
                    print(f"[HIGH] Possible SSRF at {test_url}")
        except Exception:
            pass
