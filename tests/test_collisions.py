# tests/test_main.py
from unittest.mock import Mock
from main import check


def test_1():
    # Create a platform and a group of entities
    platform = Mock(rect=Mock(centery=150))
    entity1 = Mock(rect=Mock(centery=0))
    entity2 = Mock(rect=Mock(centery=50))
    entity3 = Mock(rect=Mock(centery=110))
    group = [entity1, entity2, entity3]

    # Test collision detection
    result = check(platform, group, 40)
    assert result is False

    result = check(platform, group, 50)
    assert result is True


def test_2():
    # Create a platform and a group of entities
    platform = Mock(rect=Mock(centery=100))
    entity1 = Mock(rect=Mock(centery=0))
    entity2 = Mock(rect=Mock(centery=30))
    entity3 = Mock(rect=Mock(centery=200))
    entity4 = Mock(rect=Mock(centery=120))
    group = [entity1, entity2, entity3, entity4]

    # Test collision detection
    result = check(platform, group, 10)
    assert result is False

    result = check(platform, group, 30)
    assert result is True