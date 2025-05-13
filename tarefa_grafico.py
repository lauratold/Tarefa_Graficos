import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('ecommerce_preparados.csv')

# múltiplos gráficos
plt.figure(figsize=(15, 18))

# Histograma da Nota
plt.subplot(3, 3, 1)
plt.hist(df['Nota'], bins=30, color='steelblue', edgecolor='black')
plt.title('Histograma - Nota')
plt.xlabel('Nota')
plt.ylabel('Frequência')
plt.grid(True)

# Histograma do Preço
plt.subplot(3, 3, 2)
plt.hist(df['Preço'], bins=30, color='green', edgecolor='black')
plt.title('Histograma - Preço')
plt.xlabel('Preço')
plt.ylabel('Frequência')
plt.grid(True)

# Gráfico de Dispersão: Preço vs Nota
plt.subplot(3, 3, 3)
plt.scatter(df['Preço'], df['Nota'], color='#5883a8', alpha=0.6, s=30)
plt.title('Dispersão - Preço vs Nota')
plt.xlabel('Preço')
plt.ylabel('Nota')

# Gráfico de Dispersão
plt.subplot(3, 3, 4)
plt.scatter(df['Preço'], df['Nota'], color='#FF6347', alpha=0.6, s=30)
plt.title('Dispersão - Preço vs Nota')
plt.xlabel('Preço')
plt.ylabel('Nota')

# Mapa de Calor
plt.subplot(3, 3, 5)
corr = df[['Nota', 'Preço']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlação: Nota e Preço')

# Gráfico de Barra (Média de Nota por Faixa de Preço)
plt.subplot(3, 3, 6)
faixa_preco = pd.cut(df['Preço'], bins=10)
media_nota = df.groupby(faixa_preco)['Nota'].mean()
media_nota.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Média da Nota por Faixa de Preço')
plt.xlabel('Faixa de Preço')
plt.ylabel('Média da Nota')
plt.xticks(rotation=45)
plt.grid(True)

# Gráfico de Pizza (Distribuição de Nota)
plt.figure(figsize=(8, 8))
nota_contagem = df['Nota'].value_counts()
nota_contagem.plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette('Set3', len(nota_contagem)))
plt.title('Proporção de Notas')
plt.ylabel('')
plt.show()

# Gráfico de Densidade de Preço
plt.figure(figsize=(10, 6))
sns.kdeplot(df['Preço'], shade=True, color='purple')
plt.title('Densidade de Preço')
plt.xlabel('Preço')
plt.ylabel('Densidade')
plt.grid(True)
plt.show()

# Gráfico de Regressão entre Nota e Preço
plt.figure(figsize=(10, 6))
sns.regplot(x='Preço', y='Nota', data=df, scatter_kws={'color': 'blue', 'alpha': 0.5}, line_kws={'color': 'red'})
plt.title('Regressão entre Preço e Nota')
plt.xlabel('Preço')
plt.ylabel('Nota')
plt.grid(True)
plt.show()
