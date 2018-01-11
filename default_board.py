#!/usr/bin/env python
#Play Stratego.
#Copyright (C) 2018 Ghostkeeper
#This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.
#You should have received a copy of the GNU Affero General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.

import hazard #To place hazards on the board.
import initial_spot #To determine the initial spots for both players.
import playboard #We're inheriting from PlayBoard.
import rank #To initialise the number of pieces per rank.

class DefaultBoard(playboard.PlayBoard):
	"""
	Board with default hazards.
	"""

	def build_board(self):
		"""
		Creates the configuration of this board.
		"""
		super().build_board()

		#Place two squares of hazards.
		self.board[2][4] = hazard.Hazard()
		self.board[2][5] = hazard.Hazard()
		self.board[3][4] = hazard.Hazard()
		self.board[3][5] = hazard.Hazard()

		self.board[6][4] = hazard.Hazard()
		self.board[6][5] = hazard.Hazard()
		self.board[7][4] = hazard.Hazard()
		self.board[7][5] = hazard.Hazard()

		#Placement for the player.
		for x in range(0, len(self.board)):
			for y in range(6, 10):
				self.board[x][y] = initial_spot.InitialSpot()

		#Placement for the AI.
		for x in range(0, len(self.board)):
			for y in range(0, 4):
				self.board[x][y] = initial_spot.InitialSpot(is_ai=True)

		#How many of each piece a player gets.
		self.num_pieces[rank.Rank.BOMB] = 6
		self.num_pieces[rank.Rank.SPY] = 1
		self.num_pieces[rank.Rank.SCOUT] = 8
		self.num_pieces[rank.Rank.MINER] = 5
		self.num_pieces[rank.Rank.SERGEANT] = 4
		self.num_pieces[rank.Rank.LIEUTENANT] = 4
		self.num_pieces[rank.Rank.CAPTAIN] = 4
		self.num_pieces[rank.Rank.MAJOR] = 3
		self.num_pieces[rank.Rank.COLONEL] = 2
		self.num_pieces[rank.Rank.GENERAL] = 1
		self.num_pieces[rank.Rank.MARSHALL] = 1
		self.num_pieces[rank.Rank.FLAG] = 1