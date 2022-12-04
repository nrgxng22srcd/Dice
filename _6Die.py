import Random
from Random import randint, randrange;

class _6Die:
	def __init__(self, sides=6):
		self.sides = sides;
	def _roll(self):
		self.roll_count = random.randint(1, self.sides);
	def _get(self):
		return self.roll_count;
	def numSides(self):
		return self.sides;
	def __str__(self):
		return str(self.sides);
	def __repr__(self):
		print('your die has: {} ' f'{self.sides};
		return format(self.sides);
			  
def roll_6Die(rolls, sides):
			  s6_d1 = _6Die();
			  s6_d2 = _6Die();
			  count = 0;
			  while count <= rolls:
			  	s6_d1._roll();
			  	s6_d2._roll();
			  	print(f'{count} : {s6_d1._get()} - {s6_d2._get()}');
			  	count += 1
			  	break;
			  
