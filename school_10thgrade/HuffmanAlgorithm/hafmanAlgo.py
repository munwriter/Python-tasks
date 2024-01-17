import heapq
from collections import Counter
from typing import Type

from Node import Node


class HuffmanEncoding:
    def __init__(self, message: str) -> None:
        self.message = message

    def _define_char_frequency(self, message: str) -> Counter[str]:
        return Counter(message)

    def _sort_encoding_table(self, encoding_table: dict[str, str]) -> dict[str, str]:
        encoding_table = {char: encoding_table[char][::-1] for char in encoding_table}
        encoding_table = dict(
            sorted(encoding_table.items(), key=lambda x: (len(x[1]), x[1]))
        )
        return encoding_table

    def get_encoding_table(self) -> dict[str, str]:
        chars_frequency = self._define_char_frequency(self.message)
        heap = [Node(key, chars_frequency[key]) for key in chars_frequency]
        heapq.heapify(heap)
        self.encoding_table = {char: "" for char in self.message}
        while len(heap) > 1:
            low = heapq.heappop(heap)
            hight = heapq.heappop(heap)
            for i in hight.char:
                self.encoding_table[i] += "0"
            for i in low.char:
                self.encoding_table[i] += "1"
            if hight.char < low.char:
                hight.char = hight.char + low.char
            else:
                hight.char = low.char + hight.char
            hight.freq = hight.freq + low.freq
            heapq.heappush(heap, hight)
        self.encoding_table = self._sort_encoding_table(self.encoding_table)
        return self.encoding_table

    def encode(self) -> str:
        encoding_table = self.get_encoding_table()
        encoded_message = "".join([encoding_table[char] for char in self.message])
        return encoded_message

    @staticmethod
    def decode(encoding_table: dict[str, int], encoded_message: int) -> str:
        encoding_table = {code: char for char, code in encoding_table.items()}
        stack = ""
        decoded_message = ""
        for num in str(encoded_message):
            stack += num
            if encoding_table.get(stack):
                decoded_message += encoding_table[stack]
                stack = ""

        return decoded_message


class OutputFormatter:
    @staticmethod
    def format(
        encoding_table: dict[str, str]
    ) -> list[str] | list[Type]:  # todo - type hinting for empty list
        if not encoding_table:
            return []
        lines: list[str] = []
        for char, code in encoding_table.items():
            lines.append(f'"{char}" {code}\n')
        lines[-1] = lines[-1].strip()
        return lines


class PersistenceManager:
    def __init__(
        self, input_path: str, output_path: str, encoding: str = "utf-8"
    ) -> None:
        self.input_path = input_path
        self.output_path = output_path
        self.encoding = encoding

    def get_message(self) -> str:
        with open(self.input_path, "r", encoding=self.encoding) as f:
            message = f.read()
        return message

    def write_message(self, formatted_encoding_table: list[str] | list[Type]) -> None:
        with open(self.output_path, "w", encoding=self.encoding) as f:
            f.writelines(formatted_encoding_table)


# file_manager = PersistenceManager(
#     r"input.txt",
#     r"output.txt",
# )
# huffaman_encd_table = HuffmanEncoding(message="интервьюер интервента интервьюировал")
# print(huffaman_encd_table.get_encoding_table(), huffaman_encd_table.encode())
# # file_manager.write_message(OutputFormatter.format(huffaman_encd_table))
# print(
#     HuffmanEncoding.decode(
#         {
#             "е": "001",
#             "р": "010",
#             "в": "100",
#             "и": "101",
#             "н": "110",
#             "т": "111",
#             " ": "0001",
#             "а": "0110",
#             "ь": "00000",
#             "ю": "00001",
#             "л": "01110",
#             "о": "01111",
#         }, 1011101110010101000000000001001010000110111011100101010000111011101100001101110111001010100000000000110101001111100011001110
        
#     )
# )
