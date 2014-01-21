#! /usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Created on 20 janv. 2014

@author: Alexandre Bonhomme
'''
import logging as log
from segregation.SegregationFrame import SegregationFrame
from segregation.SegregationSMA import SegregationSMA


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
    parser.add_argument("--pop_a",
                        dest = "pop_a",
                        help = "initial population A",
                        type = int,
                        default = 50)
    parser.add_argument("--pop_b",
                        dest = "pop_b",
                        help = "initial population B",
                        type = int,
                        default = 50)
    parser.add_argument("-s",
                        "--satisfaction",
                        dest = "satisfactionThreshold",
                        help = "the satisfaction threshold",
                        type = float,
                        default = 0.3)
    parser.add_argument("-c",
                        "--cycles",
                        dest = "cycles",
                        help = "number of cycles",
                        type = int)
    args = parser.parse_args()

    # hack here we consider that "rows" = the x size (e.i. the width)
    GRID_ROWS, GRID_COLS = args.grid_cols, args.grid_rows
    BOX_SIZE = args.grid_box_size
    WIN_WIDTH, WIN_HEIGHT = GRID_ROWS * BOX_SIZE, GRID_COLS * BOX_SIZE

    sma = SegregationSMA(GRID_COLS, GRID_ROWS, args.satisfactionThreshold)
    sma.initBlueAgents(args.pop_a)
    sma.initRedAgents(args.pop_b)

    frame = SegregationFrame(WIN_HEIGHT, WIN_WIDTH, BOX_SIZE, sma)
    if args.cycles:
        frame.repeat(args.cycles, args.waiting_time_millis, sma.runOnce)
    else:
        frame.after(args.waiting_time_millis, sma.runOnce)

    frame.run()
