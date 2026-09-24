def update_score(current_score):
    """-10 per wrong ans"""
    new_score = current_score - 10
    if new_score < 0:
        return 0
    return new_score

def get_rating(final_score):
    if final_score >= 80:
        return "Excellent"
    elif final_score >= 50:
        return "Good"
    else:
        return "Keep Practicing"