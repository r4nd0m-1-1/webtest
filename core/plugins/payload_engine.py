def load_payloads(file_path):
    with open(file_path) as f:
        return [line.strip() for line in f if line.strip()]
