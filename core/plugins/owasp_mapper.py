def map_to_owasp(vuln_type):
    mapping = {
        "SQLi": "A01: Injection",
        "XSS": "A03: Injection",
        "CSRF": "A05: Broken Access Control",
        "XXE": "A04: Insecure Design",
        "SSRF": "A10: SSRF"
    }
    return mapping.get(vuln_type, "Unknown")
