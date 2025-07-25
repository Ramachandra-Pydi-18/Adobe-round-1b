def analyze_text(data, keywords):
    result = []
    for filename, text in data.items():
        score = sum(text.lower().count(kw.lower()) for kw in keywords)
        result.append({
            "file": filename,
            "score": score,
            "matched_keywords": [kw for kw in keywords if kw.lower() in text.lower()]
        })
    result.sort(key=lambda x: x["score"], reverse=True)
    return result
