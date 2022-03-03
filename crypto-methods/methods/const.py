from typing import Final


ENG_LCASE: Final = "abcdefghijklmnopqrstuvwxyz"
RUS_LCASE: Final = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

ALPHABETS: Final = (
    (ENG_LCASE, "en"),
    (RUS_LCASE, "ru")
)

POLYBIUS_SQUARE_EN: Final = {
    (1, 1): ("A",), (2, 1): ("B",), (3, 1): ("C",), (4, 1): ("D",),     (5, 1): ("E",),
    (1, 2): ("F",), (2, 2): ("G",), (3, 2): ("H",), (4, 2): ("I", "J"), (5, 2): ("K",),
    (1, 3): ("L",), (2, 3): ("M",), (3, 3): ("N",), (4, 3): ("O",),     (5, 3): ("P",),
    (1, 4): ("Q",), (2, 4): ("R",), (3, 4): ("S",), (4, 4): ("T",),     (5, 4): ("U",),
    (1, 5): ("V",), (2, 5): ("W",), (3, 5): ("X",), (4, 5): ("Y",),     (5, 5): ("Z",)
}

POLYBIUS_SQUARE_RU: Final = {
    (1, 1): ("А",),     (2, 1): ("Б",),     (3, 1): ("В",),     (4, 1): ("Г",), (5, 1): ("Д",),
    (1, 2): ("Е", "Э"), (2, 2): ("Ж", "З"), (3, 2): ("И", "Й"), (4, 2): ("К",), (5, 2): ("Л",),
    (1, 3): ("М",),     (2, 3): ("Н",),     (3, 3): ("О",),     (4, 3): ("П",), (5, 3): ("Р", "С"),
    (1, 4): ("Т",),     (2, 4): ("У",),     (3, 4): ("Ф", "Х"), (4, 4): ("Ц",), (5, 4): ("Ч",),
    (1, 5): ("Ш", "Щ"), (2, 5): ("Ы",),     (3, 5): ("Ь",),     (4, 5): ("Ю",), (5, 5): ("Я",)
}
