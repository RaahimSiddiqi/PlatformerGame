from src.Player import Player
from src.constants import ACC, FRIC, WIDTH
import pytest
from pygame.locals import K_LEFT, K_RIGHT

@pytest.fixture
def player():
    return Player()

def test_move_boundary(player):
    player.pos.x = WIDTH + 30
    player.update_position()
    assert player.pos.x == 0

def test_move_left(player):
    player.change_acceleration({K_LEFT: True, K_RIGHT: False})
    assert player.acc.x == -ACC

def test_move_right(player):
    player.change_acceleration({K_LEFT: False, K_RIGHT: True})
    assert player.acc.x == ACC