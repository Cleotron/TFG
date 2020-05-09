import dataclasses


@dataclasses.dataclass
class Base:
    name: str
    long: float
    lat: float
    demand: int
