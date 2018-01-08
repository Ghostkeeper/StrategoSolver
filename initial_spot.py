#!/usr/bin/env python
#Play Stratego.
#Copyright (C) 2018 Ghostkeeper
#This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.
#You should have received a copy of the GNU Affero General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.

class InitialSpot:
	"""
	Marks a place on the board to be the initial placement for pieces of either
	the user or the AI.
	"""

	def __init__(self, is_ai=False):
		"""
		Creates the marker cell.
		:param is_ai: Whether this spot is meant for the initial placement of an
		AI piece. If it's not AI, it's meant for the player.
		"""
		self.is_ai = is_ai