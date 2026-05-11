from rapidfuzz import process, fuzz

def match_ingredients(ai_list, db_list, threshold=80):
    matched = []
    unmatched = []

    for item in ai_list:
        match, score, _ = process.extractOne(
            item, db_list, scorer=fuzz.token_sort_ratio
        )
        if score >= threshold:
            matched.append(match)
        else:
            unmatched.append(item)

    return matched, unmatched
