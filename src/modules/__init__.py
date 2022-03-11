from typing import Final

from .atbash.atbash_widget import AtbashWidget
from .scytale.scytale_widget import ScytaleWidget
from .polybius_square.polybius_square_widget import PolybiusSquareWidget
from .caesar.caesar_widget import CaesarWidget
from .cardan_grille.cardan_grille_widget import CardanGrilleWidget
from .richelieu.richelieu_widget import RichelieuWidget


WIDGETS_CIPHERS: Final = (
    AtbashWidget,
    ScytaleWidget,
    PolybiusSquareWidget,
    CaesarWidget,
    CardanGrilleWidget,
    RichelieuWidget
)
