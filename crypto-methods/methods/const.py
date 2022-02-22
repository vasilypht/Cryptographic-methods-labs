from typing import Final

ENG_LCASE: Final = "abcdefghijklmnopqrstuvwxyz"
RUS_LCASE: Final = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

# Polybius square constants
PS_ENG_LETTER_INDEX: Final = {
    "A": (1, 1), "B": (2, 1), "C": (3, 1), "D": (4, 1),              "E": (5, 1),
    "F": (1, 2), "G": (2, 2), "H": (3, 2), "I": (4, 2), "J": (4, 2), "K": (5, 2),
    "L": (1, 3), "M": (2, 3), "N": (3, 3), "O": (4, 3),              "P": (5, 3),
    "Q": (1, 4), "R": (2, 4), "S": (3, 4), "T": (4, 4),              "U": (5, 4),
    "V": (1, 5), "W": (2, 5), "X": (3, 5), "Y": (4, 5),              "Z": (5, 5)
}

PS_ENG_INDEX_LETTER: Final = {
    (1, 1): ("A",), (2, 1): ("B",), (3, 1): ("C",), (4, 1): ("D",),     (5, 1): ("E",),
    (1, 2): ("F",), (2, 2): ("G",), (3, 2): ("H",), (4, 2): ("I", "J"), (5, 2): ("K",),
    (1, 3): ("L",), (2, 3): ("M",), (3, 3): ("N",), (4, 3): ("O",),     (5, 3): ("P",),
    (1, 4): ("Q",), (2, 4): ("R",), (3, 4): ("S",), (4, 4): ("T",),     (5, 4): ("U",),
    (1, 5): ("V",), (2, 5): ("W",), (3, 5): ("X",), (4, 5): ("Y",),     (5, 5): ("Z",)
}

PS_RUS_LETTER_INDEX: Final = {
    "А": (1, 1),              "Б": (2, 1),              "В": (3, 1),              "Г": (4, 1), "Д": (5, 1),
    "Е": (1, 2), "Э": (1, 2), "Ж": (2, 2), "З": (2, 2), "И": (3, 2), "Й": (3, 2), "К": (4, 2), "Л": (5, 2),
    "М": (1, 3),              "Н": (2, 3),              "О": (3, 3),              "П": (4, 3), "Р": (5, 3), "С": (5, 3),
    "Т": (1, 4),              "У": (2, 4),              "Ф": (3, 4), "Х": (3, 4), "Ц": (4, 4), "Ч": (5, 4),
    "Ш": (1, 5), "Щ": (1, 5), "Ы": (2, 5),              "Ь": (3, 5),              "Ю": (4, 5), "Я": (5, 5)
}

PS_RUS_INDEX_LETTER: Final = {
    (1, 1): ("А",),     (2, 1): ("Б",),     (3, 1): ("В",),     (4, 1): ("Г",), (5, 1): ("Д",),
    (1, 2): ("Е", "Э"), (2, 2): ("Ж", "З"), (3, 2): ("И", "Й"), (4, 2): ("К",), (5, 2): ("Л",),
    (1, 3): ("М",),     (2, 3): ("Н",),     (3, 3): ("О",),     (4, 3): ("П",), (5, 3): ("Р", "С"),
    (1, 4): ("Т",),     (2, 4): ("У",),     (3, 4): ("Ф", "Х"), (4, 4): ("Ц",), (5, 4): ("Ч",),
    (1, 5): ("Ш", "Щ"), (2, 5): ("Ы",),     (3, 5): ("Ь",),     (4, 5): ("Ю",), (5, 5): ("Я",)
}
