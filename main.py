import numpy as np
import os
import time


def compute_number_neighbors(padded_frame, row_index, col_index):
    neighborhood = padded_frame[
        row_index - 1 : row_index + 2, col_index - 1 : col_index + 2
    ]
    return np.sum(neighborhood) - padded_frame[row_index, col_index]


def compute_next_frame(frame):
    padded_frame = np.pad(frame, 1, mode="constant")
    new_frame = np.zeros_like(frame)

    for row_index in range(1, padded_frame.shape[0] - 1):
        for col_index in range(1, padded_frame.shape[1] - 1):
            neighbors = compute_number_neighbors(padded_frame, row_index, col_index)
            cell = padded_frame[row_index, col_index]

            if cell == 1 and neighbors in (2, 3):
                new_frame[row_index - 1, col_index - 1] = 1
            elif cell == 0 and neighbors == 3:
                new_frame[row_index - 1, col_index - 1] = 1
    return new_frame


def print_grid_ascii(frame):
    for row in frame:
        line = "".join("■" if cell else "·" for cell in row)
        print(line)


frame = np.array(
    [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 1, 0],
        [0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0],
        [0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0],
    ]
)

generation_number = 0

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print(f"Generation {generation_number}:")
    print_grid_ascii(frame)
    time.sleep(0.8)
    frame = compute_next_frame(frame)
    generation_number += 1
