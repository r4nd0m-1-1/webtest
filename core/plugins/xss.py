import aiohttp

async def scan(url, config):
    print(f"[XSS] Scanning {url}")
    payloads = open("payloads/xss_payloads.txt").read().splitlines()
    async with aiohttp.ClientSession() as session:
        for p in payloads:
            test_url = f"{url}?q={p}"
            try:
                async with session.get(test_url, timeout=config['timeout']) as resp:
                    text = await resp.text()
                    if p in text:
                        print(f"[HIGH] XSS detected at {test_url}")
            except Exception:
                continue
