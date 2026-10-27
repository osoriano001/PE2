# # from sys import path
# # path.append('..∖∖packages')
 
# import packages.extra.iota
# print(packages.extra.iota.funI())


# # from sys import path
# # path.append('..∖∖packages')

# from packages.extra.iota import funI
# print(funI())

# # from sys import path

# # path.append('..∖∖packages')

# import packages.extra.good.best.sigma
# from packages.extra.good.best.tau import funT

# print(packages.extra.good.best.sigma.funS())
# print(funT())

# # from sys import path

# # path.append('..∖∖packages')


# import packages.extra.good.best.sigma as sig
# import packages.extra.good.alpha as alp

# print(sig.funS())
# print(alp.funA())

from sys import path

path.append('packages\\extrapack.zip')

import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import funI
from extra.good.beta import funB

print(sig.funS())
print(alp.funA())
print(funI())
print(funB())