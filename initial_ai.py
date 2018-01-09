#!/usr/bin/env python
#Play Stratego.
#Copyright (C) 2018 Ghostkeeper
#This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.
#You should have received a copy of the GNU Affero General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.

import hazard #To find impassable cells.
import initial_spot #To find the places where a piece can be placed.
import rank #To add knowledge about the function of each rank.

class InitialAI:
	"""
	AI which places the pieces on the board for the start position.
	"""

	def __init__(self, board):
		self.board = board

		self.strength = 10 #Total number of iterations to compute. More makes a stronger AI but takes longer to compute.

		self.defense_value = { #How well each piece defends the pieces behind him.
			rank.Rank.FLAG: 0.0,
			rank.Rank.BOMB: 100.0,
			rank.Rank.SPY: 0.0,
			rank.Rank.SCOUT: 5.0,
			rank.Rank.MINER: 10.0,
			rank.Rank.SERGEANT: 15.0,
			rank.Rank.LIEUTENANT: 20.0,
			rank.Rank.CAPTAIN: 30.0,
			rank.Rank.MAJOR: 35.0,
			rank.Rank.COLONEL: 40.0,
			rank.Rank.GENERAL: 60.0,
			rank.Rank.MARSHALL: 90.0
		}
		self.offense_value = { #How important it is for each piece to be able to attack the enemy.
			rank.Rank.FLAG: 0.0,
			rank.Rank.BOMB: 0.0,
			rank.Rank.SPY: 5.0,
			rank.Rank.SCOUT: 85.0,
			rank.Rank.MINER: 30.0,
			rank.Rank.SERGEANT: 30.0,
			rank.Rank.LIEUTENANT: 35.0,
			rank.Rank.CAPTAIN: 40.0,
			rank.Rank.MAJOR: 45.0,
			rank.Rank.COLONEL: 50.0,
			rank.Rank.GENERAL: 60.0,
			rank.Rank.MARSHALL: 90.0
		}
		self.mobility_value = { #How likely each piece is to get out of the way for other pieces.
			rank.Rank.FLAG: 0.0,
			rank.Rank.BOMB: 0.0,
			rank.Rank.SPY: 5.0,
			rank.Rank.SCOUT: 100.0,
			rank.Rank.MINER: 15.0,
			rank.Rank.SERGEANT: 75.0,
			rank.Rank.LIEUTENANT: 70.0,
			rank.Rank.CAPTAIN: 50.0,
			rank.Rank.MAJOR: 50.0,
			rank.Rank.COLONEL: 50.0,
			rank.Rank.GENERAL: 60.0,
			rank.Rank.MARSHALL: 70.0
		}
		self.protect_value = { #How important it is to protect each piece.
			rank.Rank.FLAG: 1000.0,
			rank.Rank.BOMB: 0.0,
			rank.Rank.SPY: 60.0,
			rank.Rank.SCOUT: 0.0,
			rank.Rank.MINER: 40.0,
			rank.Rank.SERGEANT: 0.0,
			rank.Rank.LIEUTENANT: 0.0,
			rank.Rank.CAPTAIN: 0.0,
			rank.Rank.MAJOR: 1.0,
			rank.Rank.COLONEL: 2.0,
			rank.Rank.GENERAL: 3.0,
			rank.Rank.MARSHALL: 10.0
		}

	def place(self):
		"""
		Places the pieces on the board for the AI player.
		"""
		safety = self.__distance_to_outside()
		attack = self.__distance_to_other()

		for iteration in range(0, 1):#self.strength):
			rankings = self.__compute_fitness(safety, attack)

	def __compute_fitness(self, safety, attack):
		"""
		Computes for every rank how fit a piece is to place there.
		:param safety: The safety of the cell according to the current set-up.
		:param attack: The attack of a cell according to the current set-up.
		Lower is better.
		:return: A dictionary of boards, one for each rank, that contain a float
		for every cell that indicates how well a piece with that rank would be
		placed in that cell.
		"""
		rankings = {}
		for current_rank in rank.all_ranks:
			rankings[current_rank] = [[0.0 for y in range(0, len(self.board[x]))] for x in range(0, len(self.board))]
			for x in range(0, len(self.board)):
				for y in range(0, len(self.board[x])):
					if isinstance(self.board[x][y], initial_spot.InitialSpot) and self.board[x][y].is_ai:
						rankings[current_rank][x][y] = self.protect_value[current_rank] * safety[x][y] + self.offense_value[current_rank] / max(attack[x][y], 0.0001)
		return rankings

	def __distance_to_outside(self):
		"""
		Computes for every cell the distance it is to a place that will not be
		occupied by the AI's initial set-up.
		:return: A grid of floats representing that distance.
		"""
		distances = [[0.0 + len(self.board[x]) + len(self.board) for y in range(0, len(self.board[x]))] for x in range(0, len(self.board))]
		computed = [[False for y in range(0, len(self.board[x]))] for x in range(0, len(self.board))]

		border = set()
		for x in range(0, len(self.board)):
			for y in range(0, len(self.board[x])):
				if isinstance(self.board[x][y], hazard.Hazard):
					continue
				if not isinstance(self.board[x][y], initial_spot.InitialSpot) or not self.board[x][y].is_ai: #Not allowed to place.
					distances[x][y] = 0
					computed[x][y] = True
					if x > 0 and isinstance(self.board[x - 1][y], initial_spot.InitialSpot) and self.board[x - 1][y].is_ai:
						border.add((x - 1, y))
					if y > 0 and isinstance(self.board[x][y - 1], initial_spot.InitialSpot) and self.board[x][y - 1].is_ai:
						border.add((x, y - 1))
					if x < len(self.board) - 1 and isinstance(self.board[x + 1][y], initial_spot.InitialSpot) and self.board[x + 1][y].is_ai:
						border.add((x + 1, y))
					if y < len(self.board[x]) - 1 and isinstance(self.board[x][y + 1], initial_spot.InitialSpot) and self.board[x][y + 1].is_ai:
						border.add((x, y + 1))

		current_distance = 1.0
		while len(border) > 0:
			next_border = set()
			for x, y in border:
				if isinstance(self.board[x][y], hazard.Hazard):
					continue
				if current_distance < distances[x][y]:
					distances[x][y] = current_distance
					computed[x][y] = True
					if x > 0 and not computed[x - 1][y]:
						next_border.add((x - 1, y))
					if y > 0 and not computed[x][y - 1]:
						next_border.add((x, y - 1))
					if x < len(self.board) - 1 and not computed[x + 1][y]:
						next_border.add((x + 1, y))
					if y < len(self.board[x]) - 1 and not computed[x][y + 1]:
						next_border.add((x, y + 1))
			border = next_border
			current_distance += 1.0

		return distances

	def __distance_to_other(self):
		"""
		Computes for every cell the distance it is to the enemy.
		:return: A grid of floats representing that distance.
		"""
		distances = [[0.0 + len(self.board[x]) + len(self.board) for y in range(0, len(self.board[x]))] for x in range(0, len(self.board))]
		computed = [[False for y in range(0, len(self.board[x]))] for x in range(0, len(self.board))]

		border = set()
		for x in range(0, len(self.board)):
			for y in range(0, len(self.board[x])):
				if isinstance(self.board[x][y], hazard.Hazard):
					continue
				if isinstance(self.board[x][y], initial_spot.InitialSpot) and not self.board[x][y].is_ai: #Initial spot of the player.
					distances[x][y] = 0
					computed[x][y] = True
					if x > 0 and (not isinstance(self.board[x - 1][y], initial_spot.InitialSpot) or self.board[x - 1][y].is_ai):
						border.add((x - 1, y))
					if y > 0 and (not isinstance(self.board[x][y - 1], initial_spot.InitialSpot) or self.board[x][y - 1].is_ai):
						border.add((x, y - 1))
					if x < len(self.board) - 1 and (not isinstance(self.board[x + 1][y], initial_spot.InitialSpot) or self.board[x + 1][y].is_ai):
						border.add((x + 1, y))
					if y < len(self.board[x]) - 1 and (not isinstance(self.board[x][y + 1], initial_spot.InitialSpot) or self.board[x][y + 1].is_ai):
						border.add((x, y + 1))

		current_distance = 1.0
		while len(border) > 0:
			next_border = set()
			for x, y in border:
				if isinstance(self.board[x][y], hazard.Hazard):
					continue
				if current_distance < distances[x][y]:
					distances[x][y] = current_distance
					computed[x][y] = True
					if x > 0 and not computed[x - 1][y]:
						next_border.add((x - 1, y))
					if y > 0 and not computed[x][y - 1]:
						next_border.add((x, y - 1))
					if x < len(self.board) - 1 and not computed[x + 1][y]:
						next_border.add((x + 1, y))
					if y < len(self.board[x]) - 1 and not computed[x][y + 1]:
						next_border.add((x, y + 1))
			border = next_border
			current_distance += 1.0

		return distances