#!/usr/bin/env python
#Play Stratego.
#Copyright (C) 2018 Ghostkeeper
#This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.
#You should have received a copy of the GNU Affero General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.

import tkinter #To introduce GUI elements.

class PlayBoard:
	"""
	A data class that represents the current state of the game.

	Because this project is not intended to become big, the GUI is also handled
	here. If it should ever become big, you're going to have to rewrite stuff.
	"""
	def __init__(self, gui_engine):
		"""
		Sets up the game.
		"""
		self.gui_engine = gui_engine

		self.board_settings()

		self.__build_board()

	def board_settings(self):
		"""
		Initialise the settings for this play board.

		This is intended to be overwritten by specialised boards.
		"""
		self.width = 10
		self.height = 10

	def __build_board(self):
		"""
		Creates the play board, initialising everything on it.
		"""

		#The board, containing pieces or blocking parts.
		self.board = [[None for i in range(0, self.height)] for i in range(0, self.width)]