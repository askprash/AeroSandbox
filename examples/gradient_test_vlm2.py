from aerosandbox import *
import autograd.numpy as np
from autograd import grad


def f(x):
    a = Airplane(
        name="Single Wing",
        xyz_ref=[0, 0, 0],
        wings=[
            Wing(
                name="Wing",
                xyz_le=[0, 0, 0],
                symmetric=True,
                sections=[
                    WingSection(
                        xyz_le=[0, 0, 0],
                        chord=0.5,
                        twist=0,
                        airfoil=Airfoil(name="naca0012")
                    ),
                    WingSection(
                        xyz_le=[0, 1, 0],
                        chord=0.5,
                        twist=0,
                        airfoil=Airfoil(name="naca0012")
                    )
                ]
            )
        ]
    )
    a.set_ref_dims_from_wing()

    ap = vlm2(
        airplane=a,
        op_point=OperatingPoint(velocity=10,
                                alpha=x,
                                beta=0),
    )
    ap.test()

    return ap.test_var


val = 5.0  # nominal value of parameter

# # Finite Difference
# h = 1e-8  # step size
# dfdx_fd = (f(val + h) - f(val)) / h
# print('dfdx_fd = ', dfdx_fd)

# Autograd
dfdx_ag = grad(f)(val)
print('dfdx_ag = ', dfdx_ag)