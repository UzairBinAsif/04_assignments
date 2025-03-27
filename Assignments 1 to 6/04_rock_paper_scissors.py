import random as r

def play() -> str:
    user: str = input('Choose between: (R) for rock, (P) for paper and (S) for scissors\n')
    computer: str = r.choice(['r', 'p', 's'])
    
    if user == computer:
        return 'It\'s a tie.'
    
    if is_win(user, computer):
        return 'You won!'
    
    return 'You lost!'
    
# r > s, s > p, p > r

def is_win(player, opponent) -> bool:
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
            return True
print(play())