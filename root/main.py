from utils import generate_secret_number, check_user_guess
from score import deduct_points, get_score_rating

secret_number = generate_secret_number()
player_score = 100

while True:
    if check_user_guess(secret_number):
        break
    else:
        player_score = deduct_points(player_score)

rating = get_score_rating(player_score)
print(f"\nGame Over!")
print(f"Final Score: {player_score}")
print(f"Rating: {rating}")