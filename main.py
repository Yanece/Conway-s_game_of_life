import numpy as np
import os
import time


def compute_number_neighbors(padded_frame, row_index, col_index):
    """Compute the number of live neighbors for a given cell."""
    neighborhood = padded_frame[
        row_index - 1 : row_index + 2, col_index - 1 : col_index + 2
    ]
    number_neighbors = np.sum(neighborhood) - padded_frame[row_index, col_index]
    return number_neighbors


def compute_next_frame(frame):
    """Compute the next generation based on Game of Life rules."""
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

print("init_Game_of_Life_grid:")
print(frame)
print("Next_generation:")
print(compute_next_frame(frame))
