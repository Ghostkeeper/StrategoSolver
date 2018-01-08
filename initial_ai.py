#!/usr/bin/env python
#Play Stratego.
#Copyright (C) 2018 Ghostkeeper
#This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.
#You should have received a copy of the GNU Affero General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.

import rank #To add knowledge about the function of each rank.

class InitialAI:
	"""
	AI which places the pieces on the board for the start position.
	"""

	def __init__(self, board):
		self.board = board

		self.strength = 10 #Total number of iterations to compute. More makes a stronger AI but takes longer to compute.

		self.defense_value = {
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
		self.offense_value = {
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
		self.scout_value = {
			rank.Rank.FLAG: 0.0,
			rank.Rank.BOMB: 0.0,
			rank.Rank.SPY: 0.0,
			rank.Rank.SCOUT: 100.0,
			rank.Rank.MINER: 5.0,
			rank.Rank.SERGEANT: 75.0,
			rank.Rank.LIEUTENANT: 70.0,
			rank.Rank.CAPTAIN: 50.0,
			rank.Rank.MAJOR: 20.0,
			rank.Rank.COLONEL: 15.0,
			rank.Rank.GENERAL: 10.0,
			rank.Rank.MARSHALL: 8.0
		}
		self.protect_value = {
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

		for iteration in range(0, self.strength):
			#First make a mapping for every possible location how safe pieces are when they are placed there.
			pass #TODO: Place pieces and recompute safety (and other measurements).

	def __distance_to_outside(self):
		"""
		Computes for every cell the distance is to a place that will not be
		occupied by the AI's initial set-up.
		:return: A grid of floats representing that distance.
		"""
		safety = [[0 for y in range(0, len(self.board[x]))] for x in range(0, len(self.board))]
		#TODO: Breadth-first search to find these distances.
		return safety