
![logo](https://github.com/Hack-io-Data/Imagenes/blob/main/01-LogosHackio/logo_azul@4x.png?raw=true)

# Introducción
## Introducción a la inteligencia artificial y *machine learning* 

La Inteligencia Artificial (IA) es una rama de la informática que busca crear sistemas capaces de realizar tareas que normalmente requieren de la inteligencia humana. Estas tareas pueden incluir la toma de decisiones, el reconocimiento de voz, la traducción de idiomas y la percepción visual, entre otras. La IA se basa en el principio de que el conocimiento humano puede ser definido de manera precisa y las máquinas pueden imitar la inteligencia humana.

El *Machine Learning*, también conocido como aprendizaje automático, es un subcampo de la Inteligencia Artificial (IA) que se centra en el diseño de sistemas que pueden aprender y mejorar a partir de la experiencia. En lugar de ser programados explícitamente, los sistemas de Machine Learning son capaces de adaptarse y aprender a partir de los datos.

El aprendizaje automático se basa en algoritmos que pueden aprender patrones a partir de datos. Los datos se utilizan para entrenar al modelo, y luego el modelo utiliza lo que ha aprendido para hacer predicciones o tomar decisiones sin ser programado explícitamente para realizar la tarea. Por ejemplo, un sistema de *machine learnin*g podría ser entrenado en un conjunto de datos de imágenes de perros y gatos. El sistema aprendería a identificar características que diferencian a los perros de los gatos, y luego podría utilizar ese conocimiento para clasificar nuevas imágenes que nunca antes había visto.

El *Deep Learnin*g, o aprendizaje profundo, es una subcategoría del *Machine Learning*. Utiliza redes neuronales artificiales con varias capas ocultas (de ahí el término "profundo") para modelar y comprender estructuras complejas en los datos. Al igual que con otros enfoques de *Machine Learning*, los sistemas de *Deep Learning* aprenden a partir de los datos. Sin embargo, las capas adicionales en las redes neuronales permiten a los sistemas de *Deep Learning* aprender representaciones de características a diferentes niveles de abstracción, lo que puede ser especialmente útil para tareas como el reconocimiento de voz o de imágenes.

![IA](https://github.com/Hack-io-Data/Imagenes/blob/main/02-Imagenes/IntroduccionMl/ImagenIA.png?raw=true)

## Tipos de aprendizaje en *machine learning*

En *Machine Learning*, hay tres tipos principales de aprendizaje:

- **Aprendizaje Supervisado (*Supervised Learning*)**:
En el aprendizaje supervisado, el modelo se entrena utilizando un conjunto de datos etiquetados. Esto significa que para cada entrada/fila en el conjunto de datos de entrenamiento, se proporciona la salida deseada. El objetivo del modelo es aprender una función que mapee las entradas a las salidas. Luego, el modelo puede hacer predicciones sobre nuevas entradas para las que no conoce las salidas correspondientes.
    
    Pongamos un ejemplo para entenderlo mejor, imagina que estas enseñando a un robot a reconocer frutas. Le muestras diferentes frutas como manzanas, plátanos y naranjas, y le dices qué fruta es cada una. Esto serían tus "datos de entrenamiento". Luego, cuando le muestras una fruta nueva que el robot nunca ha visto, el robot trata de adivinar qué fruta es basándose en lo que aprendió de las frutas anteriores (las frutas de los “datos de entrenamiento”). En el aprendizaje supervisado, el robot aprende a partir de ejemplos etiquetados, donde ya conocemos las respuestas correctas. El objetivo es que el robot aprenda a hacer predicciones precisas sobre datos nuevos que no ha visto antes.
    
    El aprendizaje supervisado se utiliza comúnmente en problemas de clasificación y regresión. Algunos ejemplos de algoritmos de aprendizaje supervisado:
    
    - Regresión Lineal
    - Regresión Logística
    - Máquinas de Vectores de Soporte (SVM)
    - Árboles de Decisión
    - Bosques Aleatorios
    - Redes Neuronales Artificiales
    
- **Aprendizaje No Supervisado (*Unsupervised Learning*)**:
En el aprendizaje no supervisado, el modelo se entrena utilizando un conjunto de datos no etiquetados. El objetivo principal del aprendizaje no supervisado es encontrar patrones o estructuras en los datos. El modelo debe descubrir relaciones entre las variables sin la ayuda de etiquetas de salida. Esto puede incluir técnicas como la agrupación (*clustering*), donde el objetivo es dividir los datos en grupos homogéneos, y la reducción de dimensionalidad, donde el objetivo es reducir la cantidad de variables manteniendo la información relevante.
    
    Igual que en el caso anterior, pongamos un ejemplo para entenderlo mejor. Ahora, en lugar de decirle al robot qué fruta es cada una, simplemente le muestras una mezcla de diferentes frutas sin etiquetar. El robot intenta encontrar patrones o similitudes entre las frutas. Pudiendo agrupar las frutas que se parecen entre sí en grupos diferentes. Aunque no sabemos qué fruta es cada una, el robot puede descubrir automáticamente que algunas frutas son similares entre sí y otras son diferentes, solo mirando los datos.
    
    Ejemplos de algoritmos de aprendizaje no supervisado:
    
    - K-Means
    - DBSCAN
    - Análisis de Componentes Principales (PCA)
    - Análisis de Componentes Independientes (ICA)
    - Reducción de Dimensionalidad basada en Autoencoders

- **Aprendizaje por Refuerzo (*Reinforcement Learning*)**:
En el aprendizaje por refuerzo, un agente aprende a tomar decisiones secuenciales para lograr un objetivo específico a través de la interacción con un entorno. El agente realiza acciones y recibe retroalimentación en forma de recompensas o castigos del entorno según el resultado de las acciones. El objetivo del agente es aprender una política que maximice la recompensa acumulada a lo largo del tiempo. El aprendizaje por refuerzo se utiliza comúnmente en problemas de control y toma de decisiones.
    
    Esta vez, imagina que estás enseñando a un perro a jugar a buscar una pelota. Cada vez que el perro encuentra la pelota, le das un premio. Cada vez que no encuentra la pelota, no hay premio. El perro aprende a través de la experiencia qué acciones lo llevan a obtener un premio y qué acciones no. Con el tiempo, el perro aprende a tomar las decisiones correctas para obtener el premio. En el aprendizaje por refuerzo, el "agente" (el perro en este caso) aprende a través de la interacción con su entorno, recibiendo recompensas por acciones buenas y aprendiendo de las consecuencias de sus acciones.
    
    Ejemplos de algoritmos de aprendizaje por refuerzo:
    
    - Q-Learning
    - Aprendizaje Profundo por Refuerzo (Deep Reinforcement Learning)
    - Política de Gradiente de Ascenso (Policy Gradient)
    - Actor-Critic


## Aplicaciones de *machine learning*  


El *Machine Learning* tiene una amplia gama de aplicaciones en la vida cotidiana y en el mundo de los negocios. Algunos ejemplos son:

- **Recomendaciones personalizadas**: Los algoritmos de *Machine Learning* son la columna vertebral de los sistemas de recomendación utilizados por los gigantes del comercio electrónico y de los servicios de *streaming*. Al analizar el comportamiento pasado del usuario y compararlo con el de otros usuarios, estos sistemas pueden predecir qué productos o contenidos pueden interesarle al usuario.
- **Detección de fraude**: En el sector financiero, los algoritmos de *Machine Learning* pueden ser entrenados para reconocer patrones de comportamiento fraudulento basándose en transacciones pasadas y otros datos disponibles. Al detectar anomalías en tiempo real, las empresas pueden reaccionar rápidamente para prevenir pérdidas económicas.
- **Gestión de la relación con el cliente**: Las empresas utilizan el *Machine Learning* para analizar las interacciones de los clientes y personalizar sus ofertas y servicios. Por ejemplo, los sistemas de chatbot utilizan el procesamiento del lenguaje natural para entender las consultas de los clientes y responder de manera adecuada.
- **Predicción de demanda y optimización de precios**: En la industria del *retail* y la logística, los algoritmos de *Machine Learning* pueden prever la demanda de los productos y optimizar los precios en tiempo real para maximizar las ventas y los beneficios.
- **Medicina personalizada**: En el sector de la salud, el *Machine Learning* se utiliza para personalizar los tratamientos basándose en el historial médico del paciente y en otros datos relevantes. También se utiliza para predecir la probabilidad de sufrir determinadas enfermedades basándose en factores de riesgo.

# Modelado en *Machine Learning*

## Proceso de modelado en *machine learning* 

El proceso de modelado en Machine Learning implica varios pasos:

1. **Definición del problema**: Antes de comenzar a modelar, necesitamos definir claramente el problema que queremos resolver. Esto incluye la identificación del objetivo de la modelización, la definición de las métricas de éxito y la comprensión de las limitaciones del problema.

2. **Recopilación de datos**: Los datos son el combustible del *Machine Learning*. Necesitamos recoger datos relevantes para el problema que estamos tratando de resolver. Los datos pueden ser recogidos de diferentes fuentes como bases de datos, archivos, sensores, internet, etc.

3. **Análisis Exploratorio detallado**: Para comprender mejor la relación entre las características y el valor de la página.

4. **Selección de Características (*Feature Selection*)**: A menudo, no todas las características/columnas de los datos son relevantes para el problema que se está intentando resolver. En esta etapa, se seleccionan las características/columnas más importantes para mejorar la eficiencia del modelo y evitar el sobreajuste.

5. **Preprocesamiento de datos**: Los datos recogidos necesitan ser procesados y transformados en un formato que pueda ser utilizado para la modelización. Esto puede incluir la limpieza de los datos (por ejemplo, la eliminación de datos faltantes o erróneos), la transformación de variables, la codificación de variables categóricas, la normalización de variables, etc.

6. **División de los datos**: Los datos se dividen en un conjunto de entrenamiento y un conjunto de prueba. El conjunto de entrenamiento se utiliza para entrenar el modelo, mientras que el conjunto de prueba se utiliza para evaluar el rendimiento del modelo.

7. **Seleccionar un algoritmo de *Machine Learning***: En función del problema que estamos tratando de resolver, seleccionamos un algoritmo de *Machine Learning*. Hay muchos algoritmos disponibles, cada uno de ellos con sus propias fortalezas y debilidades.

8. **Entrenamiento del modelo**: Utilizando el conjunto de entrenamiento, entrenamos nuestro modelo. En esta etapa, el modelo aprende a hacer predicciones a partir de los datos.

9. **Evaluación del modelo**: Después de entrenar el modelo, lo evaluamos utilizando el conjunto de prueba. Esto nos permite medir el rendimiento del modelo y cómo de bien ha aprendido a hacer predicciones.

10. **Ajuste del modelo**: En base a los resultados de la evaluación, podemos ajustar nuestro modelo. Esto puede incluir la modificación de los parámetros del modelo, la selección de diferentes características, o incluso la elección de un algoritmo de *Machine Learning* diferente.

11. **Despliegue del modelo**: Una vez que estamos satisfechos con el rendimiento de nuestro modelo, lo desplegamos en un entorno de producción donde puede ser utilizado para hacer predicciones en datos reales.

Este proceso puede ser iterativo. Es decir, es posible que necesitemos volver a algunas de las etapas anteriores en función de los resultados que obtengamos.

## Herramientas y bibliotecas de *machine learning* 

Existen varias bibliotecas y herramientas que son ampliamente utilizadas en el campo del *Machine Learning*:

- **Scikit-learn**: Esta es una de las bibliotecas más conocidas para el *Machine Learning.* Nos va a proporcionar una gama de algoritmos supervisados y no supervisados que nos van a permitir desarrollar nuestros modelos.

- **Pandas**: Nos va a permitir manipular y limpiar los datos antes del proceso de *Machine Learning*.

- **NumPy**: Proporciona soporte para matrices y matrices multidimensionales, junto con una gran colección de funciones matemáticas para operar con estas estructuras.

- **Matplotlib y Seaborn**: Son las librerías que usaremos para crear visualizaciones estáticas, animadas e interactivas en Python. Es útil para visualizar los datos y los resultados del Machine Learning.

- **TensorFlow**: La podemos usar para crear y entrenar redes neuronales profundas.

- **Keras**: Se ejecuta sobre TensorFlow. Ofrece una interfaz más fácil de usar y simplifica la creación de modelos de *Machine Learning*.

- **PyTorch**: La usaremos para  aprendizaje profundo con flexibilidad y velocidad.



# Ética y Desafíos en Machine Learning e Inteligencia Artificial

## Aspectos éticos en *machine learning*

La Inteligencia Artificial ha tenido un desarrollo vertiginoso en los últimos años, cambiando numerosos aspectos de nuestra sociedad y modificando la forma en que nos relacionamos con la tecnología. A medida que la IA se hace más omnipresente y se generan nuevos recursos basados en ella, se vuelve una obligación manejar su desarrollo y utilización de manera ética y responsable.

La ética desempeña un papel fundamental en el desarrollo. A medida que la IA y el *Machine Learning avanza* y se integra en diversas áreas de nuestra sociedad, es esencial considerar los siguientes conceptos clave de ética y comprender su relación con estas herramientas: 

- **Sesgo y Justicia**: Los algoritmos de *Machine Learning* pueden aprender y perpetuar los sesgos presentes en los datos. Por ejemplo, si los datos de entrenamiento para un algoritmo de contratación provienen de un proceso de contratación sesgado, el algoritmo puede aprender a hacer recomendaciones sesgadas. Es fundamental que los científicos de datos sean conscientes de este problema y tomen medidas para minimizar los sesgos en sus modelos. Por ejemplo, en 2019 Apple tuvo que pagar $9,75 millones para resolver una demanda por discriminación de edad. Su sistema de evaluación de empleo basado en IA utilizaba un algoritmo que penalizaba a los solicitantes de empleo mayores de 40 años.

- **Privacidad y Confidencialidad**: El *Machine Learning* a menudo requiere grandes cantidades de datos, que pueden contener información sensible. Los científicos de datos deben respetar la privacidad de los individuos y asegurarse de que los datos se manejan de manera segura y confidencial.

- **Transparencia y Explicabilidad**: Los algoritmos de *Machine Learning* pueden ser complejos y difíciles de entender. Esto puede crear problemas de transparencia y dificultar la explicación de cómo un algoritmo llega a una determinada decisión. Los profesionales de la ciencia de datos deben aspirar a crear modelos que sean lo más transparentes y explicables posible.

- **Responsabilidad**: Cuando los algoritmos de *Machine Learning* se utilizan para tomar decisiones con implicaciones significativas (como en medicina o en la justicia), es fundamental que haya responsabilidad por las decisiones tomadas por los algoritmos. Los científicos de datos deben ser conscientes de que son responsables del impacto de sus modelos en el mundo real.

## Desafñios en *machine learning* 

- **Calidad de los datos:** Uno de los mayores desafíos en Machine Learning es garantizar la calidad de los datos utilizados para entrenar modelos. Los datos incorrectos o incompletos pueden conducir a resultados inexactos y modelos ineficientes. Asegurarse de que los datos sean limpios, completos y relevantes para el problema que se está abordando es un paso crítico en cualquier proyecto de Machine Learning.

- **Sesgo en los datos:** El sesgo en los datos de entrenamiento puede llevar a modelos de Machine Learning que perpetúan o incluso amplifican las desigualdades existentes. Este es un problema importante en muchos campos, desde la contratación y la admisión a la universidad hasta la medicina y la justicia penal. La lucha contra el sesgo en Machine Learning requiere un enfoque consciente y cuidadoso para recoger y utilizar los datos.

- **Modelos interpretables:** A medida que los modelos de Machine Learning se vuelven más complejos, también se vuelven más difíciles de entender e interpretar. Esto puede ser un problema cuando se utilizan para tomar decisiones importantes. Los profesionales de Machine Learning están trabajando en métodos para aumentar la interpretabilidad y transparencia de los modelos.

- **Problemas de privacidad:** El ML a menudo requiere grandes cantidades de datos, que  incluyen información personal. Esto plantea importantes preocupaciones de privacidad. Es fundamental manejar estos datos de manera segura y en cumplimiento de las leyes y regulaciones de privacidad.

- **Dependencia de la infraestructura tecnológica:** El *Machine Learning* requiere una gran cantidad de poder de procesamiento y almacenamiento de datos. Esto puede ser costoso y requerir una infraestructura tecnológica significativa. A medida que los modelos de Machine Learning se vuelvan más complejos y los conjuntos de datos crezcan, este desafío solo se intensificará.

- **Escasez de Datos y Aprendizaje con pocos datos:** En algunas áreas, como la medicina o la energía, la recopilación de grandes cantidades de datos puede ser costosa o poco práctica. El desarrollo de técnicas de ML con pocos datos es esencial para superar esta limitación y obtener resultados confiables con conjuntos de datos pequeños.