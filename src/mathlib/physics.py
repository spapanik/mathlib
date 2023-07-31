from dataclasses import dataclass, field


@dataclass(frozen=True)
class Constant:
    value: float
    unit: str
    name: str = field(repr=False)
    relative_uncertainty: float = field(repr=False)

    def __float__(self):
        return self.value


e = Constant(1.602176634e-19, "C", "elementary charge", 0)
c = Constant(299792458, "m/s", "speed of light in vacuum", 0)
h = Constant(6.62607015e-34, "J*s", "Planck constant", 0)
k = Constant(1.380649e-23, "J/K", "Boltzmann constant", 0)
G = Constant(6.67430e-11, "m^3/(kg*s^2)", "Gravitational constant", 2.2e-5)
L = Constant(6.02214076e23, "mol^-1", "Avogadro constant", 0)
u_0 = Constant(1.25663706212e-6, "N/A^2", "vacuum permeability", 1.5e-10)
k_e = Constant(8.9875517923e9, "N*m^2/C^2", "Coulomb constant", 1.5e-10)
