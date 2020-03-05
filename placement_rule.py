# -*- coding: utf-8 -*-
import numpy as np


placement_rule_num = 5


class PlacementRule:
    def __init__(self):
        self.placement_message = 'OK'
        self.placement_rule_list = [self.check_base_placement_rule, ]

    def check_placement_rule(self, data, board, placement):
        x, y = placement
        obj_number = board[x][y]
        if obj_number == 1:
            pass

        elif obj_number == 2:
            pass

        elif obj_number == 3:
            pass

        new_board = None

        return self.placement_message, new_board

    # noinspection PyMethodMayBeStatic
    def check_base_placement_rule(self, data, board, placement):  # rule 0 : check if user's placement where the stone is
        x, y = placement
        if (x < 0 or x > data.board_size) or (y < 0 or y > data.board_size):
            self.placement_message = f'out of the board : {x, y}'

        if board[x][y] != 0:
            # print(board)
            # print(y, x, board[y][x])
            self.placement_message = f'There is already a stone : {x, y}'

    # 착수 종류
    def move(self):  # 이동
        pass

    def add(self):  # 새로운 돌 추가
        pass

    # 착수 방향
    def width(self):  # 가로
        pass

    def height(self):  # 세로
        pass

    def diagonal(self):  # 대각선
        pass

    # 거리
    def distance_move(self):  # 이동시 거리
        pass

    def distance_add(self):  # 추가시 거리 - 인접 or 어디든
        pass

    # 착수 옵션
    def block_move(self):  # 이동시 충돌 무시 여부
        pass

    def take_out_and_add(self):  # 상대방 돌이 존재할 시 없애고 추가
        pass

    def only_reverse(self):  # 상대방 돌을 뒤집을 수 있는 곳에만 돌 이동/추가 가능
        pass


