#!/usr/bin/env python
#Play Stratego.
#Copyright (C) 2018 Ghostkeeper
#This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.
#You should have received a copy of the GNU Affero General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.

import enum #To enumerate the possible play states.

class PlayState(enum.Enum):
	"""
	The possible states of the turn play.
	"""

	SETUP = 0 #The player is setting up their pieces.
	SETUP_SELECTED = 1 #The player is setting up their pieces and he has a piece selected for play.
	TURN = 2 #It's the player's turn to move.
	SELECTED = 3 #It's the player's turn to move and he has a piece selected to move.