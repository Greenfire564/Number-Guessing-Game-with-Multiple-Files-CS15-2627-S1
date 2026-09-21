def deduct_points(current_score):
    new_score = current_score - 10
    return max(0, new_score)


def get_score_rating(final_score):
    if final_score >= 80:
        return "Excellent"
    elif final_score >= 50:
        return "Good"
    else:
        return "Keep Practicing"


if __name__ == "__main__":
    test_score = 100
    test_score = deduct_points(test_score)
    print(f"Test deduction (expected 90): {test_score}")

    floor_test = deduct_points(5)
    print(f"Test floor limit (expected 0): {floor_test}")

    print(f"Score 90 Rating: {get_score_rating(90)}")
    print(f"Score 60 Rating: {get_score_rating(60)}")
    print(f"Score 30 Rating: {get_score_rating(30)}")