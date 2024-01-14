import heapq
from collections import Counter

from Node import Node


class HuffmanEncoding:
    def __init__(self, **kwargs: str) -> None:
        if len(kwargs.keys() & {"message", "path"}) != 1:
            raise ValueError("One keyword argument is required: message=x or path=x")
        if "message" in kwargs:
            self.message = kwargs["message"]
        else:
            self.message = self._get_message(kwargs["path"])

    def _define_char_frequency(self, message: str) -> Counter[str]:
        return Counter(message)

    def _get_message(self, file_path: str) -> str:
        with open(file_path, "r", encoding="utf-8") as f:
            message = f.readline()
        return message

    def _sort_encoding_table(self, encoding_table: dict[str, str]) -> dict[str, str]:
        encoding_table = {char: encoding_table[char][::-1] for char in encoding_table}
        encoding_table = dict(
            sorted(encoding_table.items(), key=lambda x: (-len(x[1]), x[0]))
        )
        return encoding_table

    def get_encoding_table(self) -> dict[str, str]:
        chars_frequency = self._define_char_frequency(self.message)
        self.encoding_table = {char: "" for char in self.message}
        heap = [Node(key, chars_frequency[key]) for key in chars_frequency]
        heapq.heapify(heap)
        while len(heap) > 1:
            low = heapq.heappop(heap)
            hight = heapq.heappop(heap)
            for i in low.char:
                self.encoding_table[i] += "1"
            for i in hight.char:
                self.encoding_table[i] += "0"
            hight.char = hight.char + low.char
            hight.freq = hight.freq + low.freq
            heapq.heappush(heap, hight)

        return self._sort_encoding_table(self.encoding_table)

    def encode(self) -> str:
        encoding_table = self.get_encoding_table()
        encoded_message = "".join([encoding_table[char] for char in self.message])
        return encoded_message

    def write_answer(self, path: str) -> None:
        with open(path, "w", encoding="utf-8") as f:
            ...
