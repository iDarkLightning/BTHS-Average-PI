import sqlite3

class Grade:
	instances = []

	def __init__(self, name, score, category, weight):
		"""Initializes the different values of a course"""
		self.name = name
		self.score = score
		self.category = category
		self.weight = weight
		self.weighted(weight)
		Grade.instances.append(self)

	def weighted(self, weight):
		"""Takes in the weight given by the user and sets course level and weighted score"""
		if weight == 0:
			self.level = 'Regular'
			self.weighted_score = self.score
		elif weight == 1:
			self.level = 'HONORS'
			self.weighted_score = self.score * 1.05
		elif weight == 2:
			self.level = 'AP'
			self.weighted_score = self.score * 1.1
		return None

	def add_database(self):
		"""Adds the course to the SQLite Database"""
		self.conn = sqlite3.connect('courses.db')
		self.cursor = self.conn.cursor()
		with self.conn:
			self.cursor.execute('INSERT OR REPLACE INTO courses VALUES (?, ?, ?, ?)', (self.name, self.score, self.category, self.weight))