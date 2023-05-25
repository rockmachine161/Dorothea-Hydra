import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

data = pd.read_csv('/home/osboxes/Documents/Dorothea/Scripts/csv_normalizado.csv')

X = data.drop('Tipo Trafico', axis=1)  # Coge todos los datos menos los de la columna Tipo Trafico
y = data['Tipo Trafico'] #Valor para el estudio

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo MLP
mlp = MLPClassifier(hidden_layer_sizes=(100, 100), max_iter=1000)  # Ajusta los tamaños de las capas ocultas según tus necesidades
mlp.fit(X_train, y_train)

# Evaluar el modelo
accuracy = mlp.score(X_test, y_test)
print('Precisión del modelo:', accuracy)
