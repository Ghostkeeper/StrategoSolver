#!/usr/bin/env python
#Play Stratego.
#Copyright (C) 2018 Ghostkeeper
#This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.
#You should have received a copy of the GNU Affero General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.

import enum #To enumerate the ranks.

class Rank(enum.Enum):
	"""
	The ranks that a piece can have.
	"""

	FLAG = -1
	BOMB = 0
	SPY = 1
	SCOUT = 2
	MINER = 3
	SERGEANT = 4
	LIEUTENANT = 5
	CAPTAIN = 6
	MAJOR = 7
	COLONEL = 8
	GENERAL = 9
	MARSHALL = 10

all_ranks = {Rank.FLAG, Rank.BOMB, Rank.SPY, Rank.SCOUT, Rank.MINER, Rank.SERGEANT, Rank.LIEUTENANT, Rank.CAPTAIN, Rank.MAJOR, Rank.COLONEL, Rank.GENERAL, Rank.MARSHALL}