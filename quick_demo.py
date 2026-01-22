#!/usr/bin/env python3
"""
📊 DEMO RÁPIDA - Análisis de Viviendas California
Ejecutar: python quick_demo.py
"""

import pandas as pd
import matplotlib.pyplot as plt

print("🚀 Demostración rápida del dataset de viviendas")
print("="*50)

# Cargar datos
df = pd.read_csv('data/housing.csv')

# Estadísticas básicas
print(f"\n📁 Dataset: {df.shape[0]} filas, {df.shape[1]} columnas")
print(f"💰 Valor medio de vivienda: ${df['median_house_value'].mean():,.0f}")
print(f"📍 Ubicaciones únicas: {df['ocean_proximity'].nunique()}")

# Gráfico rápido
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Histograma de valores
axes[0].hist(df['median_house_value'], bins=50, alpha=0.7, color='skyblue')
axes[0].set_title('Distribución de Valores de Vivienda')
axes[0].set_xlabel('Valor (USD)')

# Boxplot por ubicación
df.boxplot(column='median_house_value', by='ocean_proximity', ax=axes[1])
axes[1].set_title('Valores por Proximidad al Océano')
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('demo_plot.png', dpi=100)
print(f"\n✅ Gráfico guardado como 'demo_plot.png'")
plt.show()

print("\n🎯 Para análisis completo, ejecuta el notebook 'analysis.ipynb'")