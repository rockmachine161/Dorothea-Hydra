import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import socket


# Ruta al archivo CSV
maligno = "/home/osboxes/Documents/Dorothea/Labs/lab_attacks/results/Pruebas/Maligno4.csv"
benigno = "/home/osboxes/Documents/Dorothea/Labs/lab_normal/results/benigno1.csv"

# Valor fijo a añadir en la nueva columna
valor_maligno = 1
valor_benigno = 0

# Cargar archivos CSV
df1 = pd.read_csv(maligno)
df2 = pd.read_csv(benigno)

# Agregar una columna con un valor fijo
df1['Tipo Trafico'] = valor_maligno
df2['Tipo Trafico'] = valor_benigno

# Se unen los archivos en uno
df_concatenado = pd.concat([df1, df2], axis=0)
df_concatenado.to_csv('/home/osboxes/Documents/Dorothea/Scripts/csv_valores_intermedios.csv', index=False)

# Se eliminan columnas innecesarias
columnas_eliminar = ['engine_type', 'engine_id', 'tos', 'src_mask', 'dst_mask', 'src_as', 'dst_as' ]  
df_concatenado = df_concatenado.drop(columnas_eliminar, axis=1)

# Se define la función que realizará la conversión de las IPs a enteros
def normalize_ip(ip):
    try:
        # Convierte la dirección IP en formato de bytes y luego integer
        packed_ip = socket.inet_aton(ip)
        packed_ip = int.from_bytes(packed_ip, byteorder='big')
        return packed_ip
    except socket.error:
        # Si la dirección IP es inválida, devuelve None
        return None

# Se definen las columnas del archivo que tienen las direcciones IP que se tienen que normalizar
DireccionesIP = ["exaddr", "srcaddr", "dstaddr", "nexthop"]
for direccion in DireccionesIP:
    df_concatenado[direccion] = df_concatenado[direccion].apply(normalize_ip)


# Se realiza ahora la normalización se las columnas para 
# posteriormente trabajar con ellas
columnas = ['#:unix_secs', 'unix_nsecs', "exaddr", 'sysuptime', 'dpkts', 'doctets', 'first', 'last', "srcaddr", "dstaddr", "nexthop", "input", 'output', 'srcport', 'dstport', 'prot', 'tcp_flags', 'Tipo Trafico']
scaler = MinMaxScaler()
df_concatenado[columnas] = scaler.fit_transform(df_concatenado[columnas])
df_concatenado.to_csv('/home/osboxes/Documents/Dorothea/Scripts/csv_normalizado.csv', index=False)





