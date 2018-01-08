#!/usr/bin/env python
#Play Stratego.
#Copyright (C) 2018 Ghostkeeper
#This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.
#You should have received a copy of the GNU Affero General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.

import hazard #To place hazards on the board.
import initial_spot #To determine the initial spots for both players.
import playboard #We're inheriting from PlayBoard.

class DefaultBoard(playboard.PlayBoard):
	"""
	Board with default hazards.
	"""
	def build_board(self):
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
		self.num_pieces[0] = 6 #Bombs.
		self.num_pieces[1] = 1 #Spies.
		self.num_pieces[2] = 8 #Scouts.
		self.num_pieces[3] = 5 #Miners.
		self.num_pieces[4] = 4 #Sergeants.
		self.num_pieces[5] = 4 #Lieutenants.
		self.num_pieces[6] = 4 #Captains.
		self.num_pieces[7] = 3 #Majors.
		self.num_pieces[8] = 2 #Colonels.
		self.num_pieces[9] = 1 #Generals.
		self.num_pieces[10] = 1 #Marshalls.
		self.num_pieces[11] = 1 #Flags.