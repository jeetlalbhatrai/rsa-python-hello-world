def classify_value(n: int) -> dict:
    status = "high" if n >= 100 else "low"
    return {"value": n, "status": status}
