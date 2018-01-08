#!/usr/bin/env python
#Play Stratego.
#Copyright (C) 2018 Ghostkeeper
#This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.
#You should have received a copy of the GNU Affero General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.

import rank #To determine which piece wins based on rank.

class Piece:
	"""
	Represents a piece on the board.
	"""

	def __init__(self, rank, *, is_ai=False):
		#Ranks are an integer:

		self.rank = rank
		self.is_ai = is_ai

	def __eq__(self, other):
		return self.rank == other.rank

	def __gt__(self, other):
		"""
		Determines whether this piece defeats the other piece.
		:param other: The piece to test whether it defeats it.
		:return: ``True`` if this piece defeats the other piece.
		"""
		#Equal ranks, both die (see __eq__).
		if self.rank == other.rank:
			return False

		#Bombs defeat everything except miners (and then disappear but that is not encoded here).
		if self.rank == rank.Rank.BOMB and other.rank != rank.Rank.MINER:
			return True
		if self.rank != rank.Rank.MINER and other.rank == rank.Rank.BOMB:
			return False

		#Spy defeats marshall.
		if self.rank == rank.Rank.SPY and other.rank == rank.Rank.MARSHALL:
			return True
		if self.rank == rank.Rank.MARSHALL and other.rank == rank.Rank.SPY:
			return False

		#Otherwise, a piece defeats another piece if its rank is higher.
		return self.rank > other.rank