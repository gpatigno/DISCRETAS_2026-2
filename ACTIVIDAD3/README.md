# Enunciado de la Actividad No. 3

Se tiene un **System-on-Chip (SoC)** simplificado con cinco componentes principales:

- CPU
- GPU
- Memoria SRAM
- Módulo de I/O (entrada/salida)
- Acelerador DSP

Las conexiones entre estos componentes forman una pequeña red dentro del chip. Podemos representar esta red como un **grafo ponderado**, donde:

- Cada **nodo** corresponde a uno de los componentes.
- Cada **arista** corresponde a un enlace de comunicación directo entre dos componentes.
- El **peso** de cada arista representa el retardo de comunicación (por ejemplo, la latencia en nanosegundos o ciclos de reloj) en ese enlace.

A continuación, se presenta la **matriz de adyacencia ponderada** del grafo correspondiente al SoC, donde cada celda representa el retardo (peso) de comunicación entre cada par de componentes.

|     |      | 1 | 2 | 3 | 4 | 5 |
|-----|------|---|---|---|---|---|
|     |      | CPU | SRAM | GPU | I/O | DSP |
| 1 | CPU  | 0 | 7 |   | 6 | 11 |
| 2 | SRAM | 7 | 0 |   | 0 | 3 |
| 3 | GPU  |   |   |   |   |   |
| 4 | I/O  | 6 | 0 |   | 0 | 4 |
| 5 | DSP  | 11 | 3 |   | 4 | 0 |


#
#
# Ejercicios

Lleve a cabo los siguientes ejercicios de esta **Actividad en Clase**:

- [Ejercicio 1](https://github.com/gpatigno/DISCRETAS_2026-2/blob/main/ACTIVIDAD3/Ejercicio1.md)
- [Ejercicio 2](https://github.com/gpatigno/DISCRETAS_2026-2/blob/main/ACTIVIDAD3/Ejercicio2.md)


#
#

# Formulario de entrega de esta Actividad

En el siguiente enlace se encuentra el **Formulario de Google** para responder las diferentes respuestas solicitadas en los ejercicios realizados en esta Actividad:

https://forms.gle/Je72sK7EGJTfsLny9


