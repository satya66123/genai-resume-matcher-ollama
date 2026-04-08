def quality_score(text):
    if not text:
        return 0

    t = text.lower()
    score = 0

    keywords = [
        "missing", "gap",
        "strength", "good",
        "suggest", "improve",
        "experience", "skills"
    ]

    for k in keywords:
        if k in t:
            score += 1

    return min(score, 5)


def select_best(results):
    best = max(results, key=lambda x: (x["quality"], -x["time"]))
    fastest = min(results, key=lambda x: x["time"])
    return best, fastest