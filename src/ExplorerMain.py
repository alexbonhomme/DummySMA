#! /usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Created on 28 janv. 2014

@author: Alexandre Bonhomme
'''
from explorer.ExplorerSMA import ExplorerSMA
from explorer.ExplorerFrame import ExplorerFrame
import logging as log

log.basicConfig(level = log.DEBUG)

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
    parser.add_argument("-n",
                        "--explorers",
                        dest = "explorers",
                        help = "number of explorers",
                        default = 1,
                        type = int)
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
    parser.add_argument("-m",
                        "--miner",
                        help = "use a miner agent to build the maze",
                        action = 'store_true',
                        default = False)
    args = parser.parse_args()

    # hack here we consider that "rows" = the x size (e.i. the width)
    GRID_ROWS, GRID_COLS = args.grid_cols, args.grid_rows
    BOX_SIZE = args.grid_box_size
    WIN_WIDTH, WIN_HEIGHT = GRID_ROWS * BOX_SIZE, GRID_COLS * BOX_SIZE

    sma = ExplorerSMA(GRID_COLS, GRID_ROWS)
    frame = ExplorerFrame(WIN_HEIGHT, WIN_WIDTH, BOX_SIZE, sma, dijkstra = args.dijkstra)

    # Building agent
    if args.miner:
        sma.initBuilder(1, GRID_COLS * GRID_ROWS)
        # this variable is used by the BuilderAgent
        # to initialize the explorers.
        # Pretty dirty but functional
        sma.explorers = args.explorers

    # Random of puzzle pieces
    else:
        sma.initWalls(3, 5, (GRID_COLS * GRID_ROWS) / 30)
        sma.initExplorers(args.explorers)

    # start main
    if args.cycles:
        frame.repeat(args.cycles, args.waiting_time_millis, sma.runOnce)
    else:
        frame.after(args.waiting_time_millis, sma.runOnce)

    frame.run()
