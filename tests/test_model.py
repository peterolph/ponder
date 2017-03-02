
from haive import model, hexes, types
import random
import pytest

@pytest.fixture(autouse=True)
def m():
	m = model.Model()

	yield m

	for token, loc in m.tokens.items():
		if loc is not None:
			print(token, loc)
			assert m.reverse[loc] == token

def test_can_create():
	assert model.Model() is not None

def test_can_str():
	assert str(model.Model()) is not None

def test_move(m):
	token = random.choice(list(m.tokens))
	m.move(token, hexes.centre)
	assert m.tokens[token] == hexes.centre

def test_move_to_cover(m):
	token1, token2 = random.sample(list(m.tokens), 2)
	m.move(token1, hexes.centre)
	m.move(token2, hexes.centre)
	assert m.tokens[token2] == hexes.centre
	assert m.tokens[token1] == token2
	assert m.trapped(token1) == True

def test_cover_then_uncover(m):
	token1, token2 = random.sample(list(m.tokens), 2)
	m.move(token1, hexes.centre)
	m.move(token2, hexes.centre)
	m.move(token2, hexes.offsets[0])
	assert m.tokens[token2] == hexes.offsets[0]
	assert m.tokens[token1] == hexes.centre
	assert m.trapped(token1) == False

def test_cannot_split_hive(m):
	token1, token2, token3 = random.sample(list(m.tokens), 3)
	m.move(token1, hexes.centre)
	m.move(token2, hexes.offsets[0])
	m.move(token3, hexes.opposite(hexes.offsets[0]))
	assert m.trapped(token1) == True
	assert m.trapped(token2) == False
	assert m.trapped(token3) == False
