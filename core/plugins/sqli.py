import aiohttp

async def scan(url, config):
    print(f"[SQLi] Scanning {url}")
    payloads = open("payloads/sql_payloads.txt").read().splitlines()
    async with aiohttp.ClientSession() as session:
        for p in payloads:
            test_url = f"{url}?id={p}"
            try:
                async with session.get(test_url, timeout=config['timeout']) as resp:
                    text = await resp.text()
                    if "sql" in text.lower() or "syntax" in text.lower():
                        print(f"[CRITICAL] SQLi detected at {test_url}")
            except Exception:
                continue
