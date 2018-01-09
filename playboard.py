#!/usr/bin/env python
#Play Stratego.
#Copyright (C) 2018 Ghostkeeper
#This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.
#You should have received a copy of the GNU Affero General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.

import tkinter #To introduce GUI elements.

import hazard #To test for hazards.
import initial_ai #To call an AI for the initial piece placement.
import initial_spot #To test for the initial spots.
import piece #To test the pieces and their ranks on the board.
import play_state #To track the current turn state.

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
		self.play_state = play_state.PlayState.SETUP #The game starts with the player setting up their pieces.

		self.build_board()

		setup_ai = initial_ai.InitialAI(self)
		setup_ai.place()

		self.display()

	def board_settings(self):
		"""
		Initialise the settings for this play board.

		This is intended to be overwritten by specialised boards.
		"""
		self.width = 10
		self.height = 10

	def build_board(self):
		"""
		Creates the play board, initialising everything on it.
		"""

		#The board, containing pieces or blocking parts.
		self.board = [[None for i in range(0, self.height)] for i in range(0, self.width)]
		self.board_gui = [[None for i in range(0, self.height)] for i in range(0, self.width)]
		self.num_pieces = {i:0 for i in range(0, 12)} #Pieces 0 through 11 all get 0 pieces by default.

	def display(self):
		"""
		Puts the current state of the board on the display.
		"""
		for x in range(0, len(self.board)):
			for y in range(0, len(self.board[x])):
				if isinstance(self.board[x][y], hazard.Hazard):
					continue #Leave this cell empty.
				self.board_gui[x][y] = tkinter.Button(width=1, height=1, text=" ")
				self.board_gui[x][y].grid(column=x, row=y)

				if self.play_state == play_state.PlayState.TURN:
					if self.board[x][y] is None:
						self.board_gui[x][y].config(state=tkinter.DISABLED) #TODO

				if self.play_state == play_state.PlayState.SETUP:
					if not isinstance(self.board[x][y], initial_spot.InitialSpot) or self.board[x][y].is_ai:
						self.board_gui[x][y].config(state=tkinter.DISABLED) #Only allow places where the user can place anything.

				#Display of visible pieces.
				if isinstance(self.board[x][y], piece.Piece):
					if not self.board[x][y].is_ai:
						self.board_gui[x][y].config(text=self._display_rank(self.board[x][y].rank), font=("Sans", "10", "bold"))
					else: #AI piece.
						if True: #TODO: Test if the user may see this piece. For debugging we now always want to see it.
							self.board_gui[x][y].config(text=self._display_rank(self.board[x][y].rank))

	@staticmethod
	def _display_rank(rank):
		"""
		Converts a piece's rank to something that will be displayed to the user.
		:param piece_rank: The rank of a piece.
		:return: A character that is displayed for that rank.
		"""
		if rank == rank.FLAG:
			return "F"
		if rank == rank.BOMB:
			return "B"
		if rank == rank.MARSHALL:
			return "X"
		return str(rank.value)