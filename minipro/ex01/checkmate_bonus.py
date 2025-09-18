#!/usr/bin/env python3

def is_check(board_str):
    """ตรวจว่า King ถูก check หรือไม่"""
    board = board_str.splitlines()
    size = len(board)

    # หาตำแหน่ง King
    king_pos = None
    for i in range(size):
        for j in range(size):
            if board[i][j] == "K":
                king_pos = (i, j)
                break
    if not king_pos:
        return False

    x, y = king_pos

    # ฟังก์ชันช่วยเช็คทิศทาง
    def check_direction(dx, dy, pieces):
        i, j = x + dx, y + dy
        while 0 <= i < size and 0 <= j < size:
            if board[i][j] != ".":
                return board[i][j] in pieces
            i += dx
            j += dy
        return False

    # Rook หรือ Queen → แนวนอน/แนวตั้ง
    if (check_direction(1, 0, "RQ") or
        check_direction(-1, 0, "RQ") or
        check_direction(0, 1, "RQ") or
        check_direction(0, -1, "RQ")):
        return True

    # Bishop หรือ Queen → ทแยง
    if (check_direction(1, 1, "BQ") or
        check_direction(1, -1, "BQ") or
        check_direction(-1, 1, "BQ") or
        check_direction(-1, -1, "BQ")):
        return True

    # Pawn → กินทแยงบน
    for dx, dy in [(-1, -1), (-1, 1)]:
        i, j = x + dx, y + dy
        if 0 <= i < size and 0 <= j < size and board[i][j] == "P":
            return True

    return False


def is_checkmate(board_str):
    """ตรวจว่า King อยู่ในสถานะ Checkmate หรือไม่"""
    board = board_str.splitlines()
    size = len(board)

    # หาตำแหน่ง King
    king_pos = None
    for i in range(size):
        for j in range(size):
            if board[i][j] == "K":
                king_pos = (i, j)
                break
    if not king_pos:
        return False

    x, y = king_pos

    # ถ้าไม่โดน check เลย → ไม่ใช่ checkmate
    if not is_check(board_str):
        return False

    # ทิศทางที่ King เดินได้ (8 ช่องรอบตัว)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1)
    ]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < size and 0 <= ny < size:
            # จำลองย้าย King ไปช่องใหม่
            new_board = [list(row) for row in board]
            new_board[x][y] = "."
            new_board[nx][ny] = "K"
            new_board_str = "\n".join("".join(r) for r in new_board)

            # ถ้าหนีไปได้โดยไม่โดน check → ไม่ใช่ checkmate
            if not is_check(new_board_str):
                return False

    return True
