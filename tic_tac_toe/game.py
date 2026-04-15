# game.py

from gameparts import Board

# Вот код, о котором говорится в абзаце выше.
game = Board()
game.display()
game.make_move(1, 1, 'X')
print('Ход сделан!')
game.display()