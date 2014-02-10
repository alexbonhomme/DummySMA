#! /usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Created on 28 janv. 2014

@author: Alexandre Bonhomme
'''
from pacman.PacmanFrame import PacmanFrame
from pacman.PacmanSMA import PacmanSMA
import logging as log


log.basicConfig(level = log.INFO)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(dest = "grid_rows",
                        help = "number of rows in the grid",
                        type = int)
    parser.add_argument(dest = "grid_cols",
                        help = "number of columns in the grid",
                        type = int)
    parser.add_argument(dest = "grid_box_size",
                        help = "size of a box in the grid",
                        type = int)
    parser.add_argument(dest = "waiting_time_millis",
                        help = "time in milliseconds between each cycle",
                        type = int)
    parser.add_argument("-p",
                        "--phantom",
                        dest = "phantom",
                        help = "number of phantom, [1..4] ",
                        choices = [1, 2, 3, 4],
                        type = int,
                        default = 4)
    parser.add_argument("-s",
                        "--stop",
                        dest = "stopEat",
                        help = "stop when phantom eat Pacman",
                        default = False)
    parser.add_argument("-c",
                        "--cycles",
                        dest = "cycles",
                        help = "number of cycles",
                        type = int)
    parser.add_argument("-d",
                        "--dijkstra",
                        help = "display dijkstra grid",
                        action = 'store_true',
                        default = False)
    args = parser.parse_args()

    # hack here we consider that "rows" = the x size (e.i. the width)
    GRID_ROWS, GRID_COLS = args.grid_cols, args.grid_rows
    BOX_SIZE = args.grid_box_size
    WIN_WIDTH, WIN_HEIGHT = GRID_ROWS * BOX_SIZE, GRID_COLS * BOX_SIZE

    sma = PacmanSMA(GRID_COLS, GRID_ROWS, stopEat = args.stopEat)
    sma.initWalls(3, 5, (GRID_COLS * GRID_ROWS) / 30)
    sma.initPacman()
    sma.initGhosts(args.phantom)

    frame = PacmanFrame(WIN_HEIGHT, WIN_WIDTH, BOX_SIZE, sma, dijkstra = args.dijkstra)
    if args.cycles:
        frame.repeat(args.cycles, args.waiting_time_millis, sma.runOnce)
    else:
        frame.after(args.waiting_time_millis, sma.runOnce)

    frame.run()
