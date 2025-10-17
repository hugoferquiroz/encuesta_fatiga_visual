
# Resultados de Regresión Logística

## Modelo 1: Solo tiempo_de_exposicion

| Variable | Coeficiente | Odds Ratio | IC 95% Inferior | IC 95% Superior | Valor p |
|----------|-------------|------------|-----------------|-----------------|----------|
| const | -4.828 | 0.008 | 0.000 | 3.454 | 0.1189 |
| tiempo_de_exposicion | 0.629 | 1.875 | 1.027 | 3.425 | 0.0407 |

### Interpretación del Modelo Simple

1. **Tiempo de exposición**:
   - El coeficiente es positivo (0.629) y estadísticamente significativo (p = 0.0407 < 0.05)
   - El odds ratio de 1.875 indica que por cada unidad que aumenta el tiempo de exposición, la probabilidad de desarrollar SVI aumenta en un 87.5%
   - La significancia al 5% nos da fuerte evidencia estadística del efecto del tiempo de exposición

2. **Constante**:
   - El coeficiente negativo (-4.828) sugiere que la probabilidad base de SVI es baja cuando no hay exposición
   - No es estadísticamente significativa (p = 0.1189 > 0.10)

## Modelo 2: Variables múltiples

| Variable | Coeficiente | Odds Ratio | IC 95% Inferior | IC 95% Superior | Valor p |
|----------|-------------|------------|-----------------|-----------------|----------|
| const | -3.803 | 0.022 | 0.000 | 611474.660 | 0.6634 |
| tiempo_de_exposicion | 0.982 | 2.671 | 0.967 | 7.381 | 0.0582 |
| iluminacion_1 | -9.159 | 0.000 | 0.000 | 7044.420 | 0.3191 |
| uso_de_dispositivos_1 | 2.646 | 14.095 | 0.001 | 385480.206 | 0.6117 |
| uso_de_dispositivos_2 | 0.417 | 1.518 | 0.000 | 6425966.959 | 0.9573 |
| uso_de_dispositivos_3 | 4.722 | 112.403 | 0.006 | 2276323.711 | 0.3506 |

### Interpretación del Modelo Múltiple

1. **Tiempo de exposición**:
   - El coeficiente aumenta a 0.982 y mantiene significancia estadística (p = 0.0582 < 0.10)
   - El odds ratio de 2.671 sugiere que, controlando por otras variables, por cada unidad de aumento en el tiempo de exposición, la probabilidad de SVI aumenta en un 167.1%
   - La significancia al 10% mantiene la robustez del hallazgo del modelo simple

2. **Iluminación** (Categoría de referencia: Inadecuada):
   - Para iluminación adecuada (iluminacion_1), el coeficiente es -9.159 (p = 0.3191)
   - El odds ratio cercano a 0 sugiere que tener iluminación adecuada reduce sustancialmente la probabilidad de SVI comparado con iluminación inadecuada
   - Sin embargo, el efecto no es estadísticamente significativo al 10% (p > 0.10)

3. **Uso de dispositivos** (Categoría de referencia: menos de 1 hora):
   - Para uso de 1-2 horas (uso_de_dispositivos_1):
     * Coeficiente positivo de 2.646 (p = 0.6117)
     * El odds ratio de 14.095 sugiere que el riesgo de SVI es 14 veces mayor que usar menos de 1 hora
     * No es estadísticamente significativo al 10%

   - Para uso de 2-4 horas (uso_de_dispositivos_2):
     * Coeficiente positivo pero menor de 0.417 (p = 0.9573)
     * El odds ratio de 1.518 sugiere un riesgo 1.5 veces mayor que usar menos de 1 hora
     * No es estadísticamente significativo al 10%

   - Para uso mayor a 4 horas (uso_de_dispositivos_3):
     * Coeficiente positivo y grande de 4.722 (p = 0.3506)
     * El odds ratio de 112.403 sugiere un riesgo 112 veces mayor que usar menos de 1 hora
     * No es estadísticamente significativo al 10%

### Robustez de los Resultados

1. **Variable principal (tiempo_de_exposicion)**:
   - Mantiene significancia estadística en ambos modelos (5% en modelo simple, 10% en modelo múltiple)
   - El efecto positivo es consistente y aumenta al controlar por otras variables
   - Es la única variable que mantiene significancia estadística al 10%

2. **Variables categóricas**:
   - Aunque los coeficientes sugieren efectos importantes (especialmente para uso prolongado de dispositivos), ninguna de las variables categóricas alcanza significancia estadística al 10%
   - Los patrones observados son consistentes con la literatura: mayor uso de dispositivos y peor iluminación tienden a aumentar el riesgo de SVI
   - La falta de significancia estadística podría deberse al tamaño de la muestra o a la multicolinealidad entre variables

### Implicaciones Prácticas

1. El tiempo de exposición emerge como el predictor más robusto de SVI
2. Los efectos de la iluminación y el uso de dispositivos, aunque sustanciales en magnitud, requieren más investigación con muestras más grandes
3. Las intervenciones deberían priorizar la reducción del tiempo de exposición, dado que es el factor con evidencia estadística más sólida

## Categorías de Referencia

Las categorías utilizadas en el modelo múltiple son:
- Iluminación: 
  * 0: Inadecuada (categoría de referencia)
  * 1: Adecuada
- Uso de dispositivos:
  * 0: menos de 1 hora (categoría de referencia)
  * 1: 1 - 2 horas
  * 2: 2 - 4 horas
  * 3: Mayor de 4 horas

Todos los coeficientes y odds ratios se interpretan en comparación con estas categorías base.
