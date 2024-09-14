from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .VeilFamiliarMove import VeilFamiliarMove
    from .myTypes.EssenceTypes import EssenceType

class VeilFamiliarType:
    def __init__(
        self,
        type_name: EssenceType,
        weaknesses: list = [],
        resistances: list = [],
        immunities: list = [],
    ):
        self.type_name = type_name
        self.weaknesses = weaknesses
        self.resistances = resistances
        self.immunities = immunities

    def is_immune(self, move: "VeilFamiliarMove") -> bool:
        return move.type_name in self.immunities
    
    def is_weak(self, move: "VeilFamiliarMove") -> bool:
        return move.type_name in self.weaknesses
    
    def is_resistant(self, move: "VeilFamiliarMove") -> bool:
        return move.type_name in self.resistances
    
    def is_typeboosted_move(self, move: "VeilFamiliarMove"):
        return move.type_name == self.type_name



    def get_type_name(self) -> str:
        return self.type_name
    
    def __str__(self):
        return str(self.type_name)
    
    
    def __add__(self, other):
        if isinstance(other, VeilFamiliarType):
            return VeilFamiliarType(
                type_name=f"{self.type_name} {other.type_name}",
                weaknesses=self.weaknesses + other.weaknesses,
                resistances=self.resistances + other.resistances,
                immunities=self.immunities + other.immunities,
            )
        else:
            raise TypeError(
                "Unsupported operand type(s) for +: 'VeilFamiliarType' and '{}'".format(
                    type(other).__name__
                )
            )
