
# Resultados de Regresión Logística

## Modelo 1: Solo tiempo_de_exposicion

| Variable | Coeficiente | Odds Ratio | IC 95% Inferior | IC 95% Superior | Valor p |
|----------|-------------|------------|-----------------|-----------------|----------|
| const | -4.828 | 0.008 | 0.000 | 3.454 | 0.1189 |
| tiempo_de_exposicion | 0.629 | 1.875 | 1.027 | 3.425 | 0.0407 |

## Modelo 2: Variables múltiples

| Variable | Coeficiente | Odds Ratio | IC 95% Inferior | IC 95% Superior | Valor p |
|----------|-------------|------------|-----------------|-----------------|----------|
| const | -3.803 | 0.022 | 0.000 | 611474.660 | 0.6634 |
| tiempo_de_exposicion | 0.982 | 2.671 | 0.967 | 7.381 | 0.0582 |
| iluminacion_1 | -9.159 | 0.000 | 0.000 | 7044.420 | 0.3191 |
| uso_de_dispositivos_1 | 2.646 | 14.095 | 0.001 | 385480.206 | 0.6117 |
| uso_de_dispositivos_2 | 0.417 | 1.518 | 0.000 | 6425966.959 | 0.9573 |
| uso_de_dispositivos_3 | 4.722 | 112.403 | 0.006 | 2276323.711 | 0.3506 |

## Categorías de Referencia

Las siguientes categorías se utilizaron como referencia en el modelo múltiple:
- Iluminación: Primera categoría
- Frecuencia de pausas: Primera categoría
- Uso de dispositivos: Primera categoría

Los coeficientes y odds ratios para las variables dummy se interpretan en relación a estas categorías de referencia.
