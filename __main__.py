#!/usr/bin/env python
#Plays Stratego with the user.
#Copyright (C) 2018 Ghostkeeper
#This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.
#You should have received a copy of the GNU Affero General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.

import tkinter #To create the GUI engine.

import playboard #The main board.

if __name__ == "__main__":
	gui_engine = tkinter.Tk()
	gui_engine.title("Stratego")
	window = playboard.PlayBoard(gui_engine)
	gui_engine.mainloop()