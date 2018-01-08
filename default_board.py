#!/usr/bin/env python
#Play Stratego.
#Copyright (C) 2018 Ghostkeeper
#This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.
#You should have received a copy of the GNU Affero General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.

import hazard #To place hazards on the board.
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