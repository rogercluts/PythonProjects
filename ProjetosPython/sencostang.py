from math import radians, sin, cos, tan
an = float(input('Digite o ângulo desejado: '))
sen = sin(radians(an))
print(f'O angulo de {an} tem o SENO de {sen:.2f}')
cos = cos(radians(an))
print(f'O angulo de {an} tem o COSSENO de {cos:.2f}')
tan = tan(radians(an))
print(f'O angulo de {an} tem a TANGENTE de {tan:.2f}')