# SistemaTransporte
En Python se crean instrucciones para el desarrollo de un sistema inteligente que, a partir de una base de conocimiento escrito en reglas lógicas, desarrolle la mejor ruta para moverse desde un punto A y un punto B en el sistema de transporte masivo local.

# Sistema Inteligente para Rutas en Transporte Masivo

## Descripción
Este proyecto implementa un sistema inteligente que determina la mejor ruta en un sistema de transporte masivo. Utiliza la teoría de grafos con `networkx` y reglas lógicas con `experta` para calcular la ruta óptima entre dos estaciones.

## Tecnologías Utilizadas
- **Python 3.9+**
- `networkx`: Para modelar el sistema de transporte como un grafo.
- `experta`: Para definir reglas lógicas en la toma de decisiones.

## Instalación
1. Clona este repositorio:
   ```sh
   git clone https://github.com/tu-usuario/ruta-inteligente.git
   cd ruta-inteligente
   ```
2. Crea un entorno virtual (opcional pero recomendado):
   ```sh
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
3. Instala las dependencias:
   ```sh
   pip install networkx experta
   ```

## Uso
Para ejecutar el programa, usa:
```sh
python main.py
```

Ejemplo de salida:
```
La mejor ruta de A a D es: ['A', 'B', 'D']
```

## Explicación del Código
1. **Definición del Grafo:** Se modelan las estaciones y conexiones con `networkx`, donde cada conexión tiene un peso asociado.
2. **Motor de Inferencia:** Se usa `experta` para definir reglas lógicas que determinan la mejor ruta.
3. **Ejecución del Sistema:** Se ingresa una estación de origen y destino, y el sistema devuelve la mejor ruta calculada.

## Mejoras Futuras
- Incluir condiciones como tráfico en tiempo real.
- Optimización del algoritmo de búsqueda.

## Autor
Oscar Andres Martinez Vela

## Licencia
Este proyecto se distribuye bajo la licencia MIT.

