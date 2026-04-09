# Laboratorio III
# *Transporte* 
***

> En este proyecto presentamos un  modelo de colas que consta de un generador, una cola y un destino conectados en una red Network. Se configura una simulación de 200s donde el generador crea y transmite paquetes con intervalos dados por una distribución exponencial de media configurable, y la cola es capaz de atenderlos bajo una misma distribución.

***

## *Índice*

***

* Introducción

* Métodos  

* Resultados

* Discusión

* Referencias

***

## *Abstract*

***

En este trabajo se analizará el desempeño de una red frente a dos casos que modelan problemas comunes de flujo y congestión utilizando simulaciones paramétricas. Se diseñará un algoritmo con la intención solucionar los problemas identificados y mejorar el rendimiento de la red.

***

## *Introducción*

***

A continuación describiremos la red analizada en este trabajo, demostrando los distintos problemas de flujo y congestión que surgen en dos distintos casos que estudiaremos donde se varía la velocidad de transmisión de datos y la demora en diferentes partes de esta red.

![fig-1](images/modelos/before/Network.png "Figura 1")

En la *figura 1* podemos observar la red en cuestión,la cual, consta de tres componentes. Un nodo transmisor (NodeTx) que crea y transmite los paquetes simulando un host emitiendo paquetes recibidos por la capa de aplicación. Un buffer que recibe los paquetes emitidos por el generador, encolandolos y emitiendolos con cierta demora, creando un espacio de tiempo de manera que el receptor de estos paquetes pueda procesar los paquetes. Finalmente tenemos un nodo receptor (NodeRx) que es el destino final de los paquetes, el cual simula el host receptor de estos paquetes que viajan por la red y es quien se encargará de procesarlos.

![fig-2](images/modelos/before/nodeTx.png "Figura 2")

En la *figura 2* podemos ver las componentes del nodo transmisor, tenemos un generador que crea y emite los paquetes, y un buffer que encola los paquetes emitidos antes de transmitirlos fuera del nodo de manera controlada.

![fig-3](images/modelos/before/nodeRx.png "Figura 3")

En la *figura 3* podemos observar las diferentes componentes del nodo receptor. Este se compone por un buffer en el cual se alojan los paquetes recibidos, para luego enviarlos al sink, que es el destino final de los paquetes enviados.

Para los siguientes casos de estudio, mantuvimos las siguientes constantes:

* Tamaño del buffer del nodeTx: 2.000.000.
* Tamaño del buffer entre el nodeTx y el nodeRx: 200.
* Tamaño del buffer del nodeRx: 200.
* Tamaño en bytes de los paquetes: 12500.

### Caso De Estudio 1

* Para el primer caso de estudio se tuvo la siguiente configuración:

~~~
    - NodeTx a Queue: datarate = 1 Mbps y delay = 100 us
    - Queue a NodeRx: datarate = 1 Mbps y delay = 100 us
    - Queue a Sink: datarate = 0.5 Mbps
~~~

Estudiaremos como se comporta la red con un intervalo de generación de paquetes que tenga una distribución exponencial de 0.1, 0.5, 1.0 segundos.

Antes de mostrar los resultados de la simulación analicemos y demos una estimación de lo que va a ocurrir. Como podemos ver de la configuración el *datarate* del buffer del `nodeRx` al `sink` se reduce a la mitad por lo que podemos estimar que a medida que el intervalo de generación del paquete se hace mas pequeño ocurrirá una congestión en este tramo ya que el `nodeRx` recibir una mayor cantidad de paquetes en menos tiempo, que se transfieren al `sink` a menor velocidad que el resto de la red, saturando este buffer. Dada nuestra hipótesis veamos ahora los resultados de la simulación:

|Generation interval 0.1|Generation interval 0.5|Generation interval 1.0|
|:---------------------:|:---------------------:|:---------------------:|
|![Gráfico 1.1.1](images/caso_1/genInterval_0.1/cantidad_de_paquetes_en_el_buffer_vs_paquetes_dropeados_1_genInterval_0.1.png "Gráfico 1.1.1")|![Gráfico 1.2.1](images/caso_1/genInterval_0.5/cantidad_de_paquetes_en_el_buffer_vs_paquetes_dropeados_1_genInterval_0.5.png "Gráfico 1.2.1")|![Gráfico 1.3.1](images/caso_1/genInterval_1.0/cantidad_de_paquetes_en_el_buffer_vs_paquetes_dropeados_1_genInterval_1.0.png "Gráfico 1.3.1")|
*Cantidad De Paquetes En Los Buffers vs Paquetes Dropeados*

Podemos observar en las tres imágenes como a medida que incrementa el intervalo de generación se hay menos pérdida de paquetes y como hay menos cantidad de paquetes que pasan tiempo encolados en algún buffer.

* En el *gráfico 1.1.1* con un intervalo de *0.1* ocurre una congestión en el buffer del nodo receptor ya que recibe paquetes más rápido de lo que lo puede transmitir al `sink`, esto se ve en el gráfico donde la cantidad de paquetes en el buffer incrementa hasta llegar a 200 que es la capacidad máxima del buffer, luego de eso pasa a ser constante. Podemos ver que la pérdida de paquetes empieza justo cuando se llena el buffer ocurriendo de manera incremental sin detenerse.

* En el *gráfico 1.2.1* con el intervalo en *0.5* vemos que hay suficiente tiempo entre la emisión de paquetes por lo que le da al `nodeRx` tiempo suficiente para procesar los paquetes, esto lo podemos ver en la imagen donde se muestra que no hay paquetes perdidos. También podemos ver que la cantidad de paquetes en el buffer la mayor parte del tiempo se mantiene en 1, pero en ciertos momentos donde el intervalo de generación se vuelve mas pequeño, el buffer del medio tiene que encolar, esto se debe a que el intervalo es una distribución y no una constante.

* En el *gráfico 1.3.1* con un intervalo de *1.0* vemos que tanto la cantidad de paquetes en el buffer como la cantidad de paquetes perdidos es constante en 1 y 0 respectivamente, esto se debe a que espacio de tiempo entre cada emisión de paquetes es tan grande que al `nodeRx` le da tiempo suficiente para procesar un paquete antes de que llegue otro.

|Generation interval 0.1|Generation interval 0.5|Generation interval 1.0|
|:---------------------:|:---------------------:|:---------------------:|
|![Gráfico 1.2.2](images/caso_1/genInterval_0.1/capacidad_buffer_vs_delay_en_sink_caso_1_genInterval_0.1.png "Gráfico 1.1.2")|![Gráfico 1.2.2](images/caso_1/genInterval_0.5/capacidad_buffer_vs_delay_en_sink_caso_1_genInterval_0.5.png "Gráfico 1.2.2")|![Gráfico 1.3.2](images/caso_1/genInterval_1.0/capacidad_buffer_vs_delay_en_sink_caso_1_genInterval_1.0.png "Gráfico 1.3.2")|
*Capacidad Del Buffer Del Nodo Receptor vs Delay Del Sink*

Observemos ahora la relación del buffer con el sink. Debido a que el datarate entre el buffer y el sink es menor que en el resto de la red podemos observar donde ocurre la congestión. 

* Con un intervalo de 0.1 vemos como a medida que se va saturando el buffer va incrementando el delay del sink, hasta que se llena el buffer y el delay intenta estabiliazarse en 40 segundos. A medida que incrementa el intervalo de generacion de paquetes va disminuyendo el delay y la cantidad de paquetes en el buffer.

Ahora veamos un poco el comportamiento de la red en general:

|Generation interval 0.1|Generation interval 0.5|Generation interval 1.0|
|:---------------------:|:---------------------:|:---------------------:|
|![Gráfico 1.1.3](images/caso_1/genInterval_0.1/utilizacion_del_buffer_a_traves_del_tiempo_1_genInterval_0.1.png "Gráfico 1.1.3")|![Gráfico 1.2.3](images/caso_1/genInterval_0.5/utilizacion_del_buffer_a_traves_del_tiempo_1_genInterval_0.5.png "Gráfico 1.2.3")|![Gráfico 1.3.3](images/caso_1/genInterval_1.0/utilizacion_del_buffer_a_traves_del_tiempo_1_genInterval_1.0.png "Gráfico 1.3.3")|
*Utilización Del Buffer A Través Del Tiempo*

Podemos ver como la utilización de los buffers fuera del nodo receptor se mantiene baja y la utilización del buffer dentro de este incrementa y se mantiene alta para el primer intervalo. A medida que el intervalo es mayor la utilización de los buffers va bajando.

|Generation interval 0.1|Generation interval 0.5|Generation interval 1.0|
|:---------------------:|:---------------------:|:---------------------:|
|![Gráfico 1.1.4](images/caso_1/genInterval_0.1/vida_del_paquete_dentro_del_buffer_1_genInterval_0.1.png "Gráfico 1.1.4")|![Gráfico 1.2.4](images/caso_1/genInterval_0.5/vida_del_paquete_dentro_del_buffer_1_genInterval_0.5.png "Gráfico 1.2.4")|![Gráfico 1.3.4](images/caso_1/genInterval_1.0/vida_del_paquete_dentro_del_buffer_1_genInterval_1.0.png "Gráfico 1.3.4")|
*Vida Del Paquete Dentro De Los Buffers De La Red*

Ahora vemos la duración de los paquetes dentro de cada buffer. Observamos como en el primer intervalo los paquetes pasan mucho más tiempo en el buffer del receptor que en cualquier otro buffer de la red y esto va disminuyendo a medida que el intervalo se hace más grande.

Con este análisis podemos concluir que nuestra hipótesis es correcta y ocurre una congestión en el nodo receptor cuando hay una mayor carga de paquetes recibidos debido a que la velocidad de transmisión entre el buffer y el sink es más lenta que en el resto de la red.

***

### Caso de estudio 2

* Para el segundo caso de estudio se tuvo la siguiente configuración:

~~~
  - NodeTx a Queue: datarate = 1 Mbps y delay = 100 us
  - Queue a NodeRx: datarate = 0.5 Mbps
  - Queue a Sink: datarate = 1 Mbps y delay = 100 us
~~~

Al igual que en el primer caso hagamos una predicción analizando la configuración dada. Como podemos ver la configuración tiene los mismos valores que el primer caso, la única diferencia es que nos indica cual es el enlace alterado. Esta vez el datarate del Queue al `NodeRx` se reduce a 0.5 Mbps, por lo que podemos esperar ver resultados similares solo que en vez de que la congestión ocurra desde el buffer del nodo receptor al `sink`, ocurrirá desde el Queue central al `nodeRx`.

Veamos ahora los resultados de la simulación:

|Generation interval 0.1|Generation interval 0.5|Generation interval 1.0|
|:---------------------:|:---------------------:|:---------------------:|
|![Gráfico 2.1.1](images/caso_2/genInterval_0.1/cantidad_de_paquetes_en_el_buffer_vs_paquetes_dropeados_2_genInterval_0.1.png "Gráfico 2.1.1")|![Gráfico 2.2.1](images/caso_2/genInterval_0.5/cantidad_de_paquetes_en_el_buffer_vs_paquetes_dropeados_2_genInterval_0.5.png "Gráfico 2.2.1")|![Gráfico 2.3.1](images/caso_2/genInterval_1.0/cantidad_de_paquetes_en_el_buffer_vs_paquetes_dropeados_2_genInterval_1.0.png "Gráfico 2.3.1")|
*Cantidad De Paquetes En Los Buffers vs Paquetes Dropeados*

|Generation interval 0.1|Generation interval 0.5|Generation interval 1.0|
|:---------------------:|:---------------------:|:---------------------:|
|![Gráfico 2.1.2](images/caso_2/genInterval_0.1/capacidad_buffer_vs_delay_en_sink_caso_2_genInterval_0.1.png "Gráfico 2.1.2")|![Gráfico 2.2.2](images/caso_2/genInterval_0.5/capacidad_buffer_vs_delay_en_sink_caso_2_genInterval_0.5.png "Gráfico 2.2.2")|![Gráfico 2.3.2](images/caso_2/genInterval_1.0/capacidad_buffer_vs_delay_en_sink_caso_2_genInterval_1.0.png "Gráfico 2.3.2")|
*Capacidad del buffer del nodo Receptor vs delay de la red*

Como podemos ver, los gráficos que se presentan son iguales a los que se encuentran en el caso 1, con la excepción de que el buffer afectado ahora es el Queue entre el `nodeTx` y el `nodeRx`. Vemos en los gráficos que a medida que disminuye el intervalo de generación de paquetes, se va saturando la Queue, lo que, como consecuencia produce más delay en la red.

Ahora veamos un poco el comportamiento de la red en general:

|Generation interval 0.1|Generation interval 0.5|Generation interval 1.0|
|:---------------------:|:---------------------:|:---------------------:|
|![Gráfico 2.1.3](images/caso_2/genInterval_0.1/utilizacion_del_buffer_a_traves_del_tiempo_2_genInterval_0.1.png "Gráfico 2.1.3")|![Gráfico 2.2.3](images/caso_2/genInterval_0.5/utilizacion_del_buffer_a_traves_del_tiempo_2_genInterval_0.5.png "Gráfico 2.2.3")|![Gráfico 2.3.3](images/caso_2/genInterval_1.0/utilizacion_del_buffer_a_traves_del_tiempo_2_genInterval_1.0.png "Gráfico 2.3.3")|
*utilizacion del buffer a traves del tiempo*

|Generation interval 0.1|Generation interval 0.5|Generation interval 1.0|
|:---------------------:|:---------------------:|:---------------------:|
|![Gráfico 2.1.4](images/caso_2/genInterval_0.1/vida_del_paquete_dentro_del_buffer_2_genInterval_0.1.png "Gráfico 2.1.4")|![Gráfico 2.1.4](images/caso_2/genInterval_0.5/vida_del_paquete_dentro_del_buffer_2_genInterval_0.5.png "Gráfico 2.2.4")|![Gráfico 2.3.4](images/caso_2/genInterval_1.0/vida_del_paquete_dentro_del_buffer_2_genInterval_1.0.png "Gráfico 2.3.4")|
*vida del paquete dentro de los buffers de la red*

Ahora vemos la duración de los paquetes dentro de cada buffer. Al igual que en los gráficos anteriores, observamos como los gráficos son iguales a los del primer caso solo que el buffer afectado esta vez es el Queue.

Haciendo un análisis entre los dos casos de estudio vemos que la única diferencia en los resultados es cuando se ven con detenimiento las zonas afectadas, en el primer caso vemos que el buffer del nodo receptor es el que se afecta a medida que disminuye el intervalo de generación de paquetes y en el segundo caso es el buffer que se encuentra en el medio de la red, entre el nodo transmisor y el receptor.

## *Métodos*

***
Para solucionar los problemas existentes en la red se plantea un algoritmo de control de flujo y control de congestión. Primero se agregó un canal de retorno a través del cual el `nodoRx` puede mandar paquetes de control al `nodoTx`. Además se plantean modificar los modulos `queue` internos por nuevos módulos `transportRx` y `transportTx` respectivamente para poder indicar comportamientos diferentes a cada uno.

La nueva estructura de la red queda entonces:

![fig-3-1](images/modelos/after/Network.png)
*Figura 3.1: La red con canal de retorno*

![fig-3-2](images/modelos/after/nodeTx.png)
*Figura 3.2: El nuevo nodeTx con el modulo TransortTx#*

![fig-3-3](images/modelos/after/nodeRx.png)
*Figura 3.3: El nuevo nodeRx con el modulo TransportRx*

Luego de aplicar dichas modificaciones podemos empezar a describir un algoritmo propio. El algoritmo se encargará de manejar un nuevo delay que se agrega en la salida del módulo `transportTx` aplicando entonces control de flujo y de congestión.

### Mensajes de Control

A través del canal de retorno, el módulo `nodeRx` podrá enviar mensajes de control al módulo `nodeTx`. Estos mensajes serán de similares características que los mensajes de datos, pero tendrán el mínimo tamaño y utilizamos el campo `kind` para diferenciarlos. Los mensajes quedan divididos de la siguiente manera:

* *Mensajes de tipo 2*: Mensajes de control que indican al nodeTx que aumente el delay entre cada paquete.
* *Mensajes de tipo 3*: Mensajes de control que indican al nodeTx que disminuya el delay entre cada paquete.
* *Mensajes de otro kind*: Mensajes de datos.

El módulo `transportTx` tendrá el siguiente comportamiento al recibir mensajes de control:

* *Kind 2*: Aumenta el delay entre cada paquete en 0.1 segundos
* *Kind 3*: Disminuye el delay entre cada paquete en 0.2 segundos

La diferencia entre el intervalo de aumento y disminución le permite al módulo `transportTx` recuperarse rápidamente cuando los problemas de flujo o congestión disminuyen.

### Envío de los Mensajes de Control

El comportamiento mas interesante del algoritmo es el que describe como el módulo `transportRx` detecta problemas y envía los mensajes de control. Podemos divir el comportamiento en dos grandes grupos: Control de Flujo y Control de Congestión.

### Control de Flujo

El control de flujo es necesario cuando se encuentra en la red un nodo receptor de baja capacidad que no es capaz de procesar los paquetes entrantes a tiempo. Cuando esto ocurre, se empiezan a acumular paquetes en el `queue` del modulo receptor (`transportTx` en nuestro caso) y este puede llegar a perder paquetes si el problema no se controla a tiempo. Este problema es fácil de detectar, ya que el módulo `transportRx` tiene acceso al estado actual de su `queue` interno. El módulo debe enviar entonces un mensaje de tipo 2 por el canal de retorno cuando le llega un paquete nuevo y detecta que la capacidad de su cola supera cierto umbral (Una configuración del 80% parece funcionar bien). Al mismo tiempo, si al llegar un paquete la capacidad de su cola no supera el umbral, envía un mensaje de tipo 3.

### Control de Congestión

El control de congestión es necesario cuando hay un nodo intermedio en la red que se encuentra desbordado (Le llegan paquetes más rápido de lo que puede procesar) y comienza a perder paquetes. Este problema es más complicado de tratar, ya que el módulo `transportRx` no tiene acceso al estado de los nodos intermedios. Para detectar congestión se usará una nueva métrica de **delay**. Esta metrica medirá ,de cada paquete ,cuanto tiempo transcurre desde que sale de `transportTx` hasta que llega a `transportRx` (El tiempo que anda recorriendo la red).
Cuando llega el primer paquete al modulo `transportRx` se registra el delay del mismo y éste se toma como referencia para el resto de la comunicación. En el resto de los paquetes se mide el delay y se compara con esa referencia. Si el delay de un mensaje entrante es mayor a la referencia multiplicada por una tolerancia (Esta tolerancia es otro parámetro que se puede modificar, pero un valor de 5 parace ser un buen balance) se envia un mensaje de tipo 2. En caso contrario se envia un mensaje de tipo 3.

### Módulo impaciente

El último control que se aplica sobre el modulo `transportRx` se lo denomina "Modulo Impaciente". El mismo consiste en un timer interno dentro de `transportRx` que envia un mensaje de tipo 3 cuando pasa cierto tiempo sin recibir paquetes. Este timer ayuda al modulo `transportTx` a recuperar la velocidad de trasnmision mas rapidamente en caso que el mismo haya disminuido mucho.

***

## *Resultados*

|![fig-7](images/after/caso_1/genInterval_0.1/vida_del_paquete_dentro_del_buffer_1_genInterval_0.1.png "Gráfico 1.1.1")|![Gráfico 1.2.1](images/after/caso_1/genInterval_0.1/capacidad_buffer_vs_delay_en_sink_caso_1_genInterval_0.1.png "Gráfico 1.2.1")|![Gráfico 1.3.1](images/after/caso_1/genInterval_0.1/utilizacion_del_buffer_a_traves_del_tiempo_1_genInterval_0.1.png "Gráfico 1.3.1")|![Gráfico 1.3.1](images/after/caso_1/genInterval_0.1/cantidad_de_paquetes_en_el_buffer_vs_paquetes_dropeados_1_genInterval_0.1.png "Gráfico 1.3.1")|
|:---------------------:|:---------------------:|:---------------------:|:------------------:|

Luego de correr las simulaciones parametricas en el caso 1 pero con el algoritmo implementado notamos XXXXX diferencias principales:

* La capacidad del buffer del móduloRx oscila entre el 80% y 70% de capacidad en lugar de llegar al 100%. Esto permite que no se pierdan paquetes.
* Como consecuencia, los paquetes que antes se perdían se encuentran en el queue del módulo Tx.
* La vida del paquete dentro del buffer esta directamente relacionada a la cantidad de paquetes en el buffer.
* El delay de la red aumenta de manera lineal sin aparente límite, ya que el generador esta emitiendo paquetes más rapidamente de lo que la red puede soportar. Los paquetes quedan encolados en el módulo `transportTx` hasta que pueden salir.

|![fig-7](images/after/caso_2/genInterval_0.1/vida_del_paquete_dentro_del_buffer_2_genInterval_0.1.png "Gráfico 1.1.1")|![Gráfico 1.2.1](images/after/caso_2/genInterval_0.1/capacidad_buffer_vs_delay_en_sink_caso_2_genInterval_0.1.png "Gráfico 1.2.1")|![Gráfico 1.3.1](images/after/caso_2/genInterval_0.1/utilizacion_del_buffer_a_traves_del_tiempo_2_genInterval_0.1.png "Gráfico 1.3.1")|![Gráfico 1.3.1](images/after/caso_2/genInterval_0.1/cantidad_de_paquetes_en_el_buffer_vs_paquetes_dropeados_2_genInterval_0.1.png "Gráfico 1.3.1")|
|:---------------------:|:---------------------:|:---------------------:|:------------------:|

Podemos ver en los graficos que el nodeRx trata de mantener el delay en cierto umbral comunicandose con el transmisor para indicarle si debe incrementar o disminuir la velocidad de transmision, con esto vemos como oscila la cantidad y duracion de los paquetes en el Queue en cierto rango tratando de estabilizarse. Podemos ver en la ultima grafica como no se pierden paquetes y la cantidad de paquetes no sobrepasa 7.5% (15 paquetes) de la capacidad del queue.

|![fig-4.7](images/after/extras/EmitidaVsDelay.png)|![fig-4.7](images/after/extras/EmitidaVsPerdidos.png)|![fig-4.7](images/after/extras/EmitidaVsUtil.png)|
|:-:|:-:|:-:|

Podemos ver en estos gráficos de carga emitida que nuestro algoritmo logra saturar la red por completo en los casos 1 y 2 al igual que en la parte 1 (Por eso todas las lineas se encuentran superpuestas). La diferencia principal es que el algoritmo no pierde paquetes y esto lo logra comprometiendo un poco el delay de los mismos.

***

## *Discusión*

***

Luego de implementar y analizar el algoritmo se identificaron ciertos aspectos para mejorar en una futura versión.

1. Hay multiples parámetros que controlan como funciona el algoritmo (El umbral para control de flujo, la tolarancia para control de congestión o el timer del "Modulo Impaciente" por ejemplo). Durante la implementación se seleccionaron valores que dan un buen resultado, pero no se realizó un analisis exhaustivo para encontrar el punto óptimo de cada uno.
1. También es probable que el mejor valor para los parametros mencionados anteriormente no sea un valor fijo sino que el algoritmo se beneficie de algún tipo de ajuste dinamico para acomodarse mejor las condiciones especificas de cada red.
1. En la seccion de Control de Congestión se utiliza el delay del primer paquete que llega como métrica para comparar el resto de paquetes. Una mejor estrategia contemplaría una modificación de esa metrica a lo largo de la vida de la red, utilizando un delay promedio o actualizandolo cada cierto tiempo.
1. Un aspecto que se podría mejorar es la cantidad de mensajes de control que se envían. En redes de baja capacidad (En donde el algoritmo es más necesario) puede afectar la alta cantidad de paquetes de control que se envían y contribuir a los problemas de congestión ya presentes. Una mejor solución podría mandar menos paquetes e incluir mas información sobre cuanto aumentar o disminuir el delay de transmisión.

***

## *Autores y sobre el desarrollo*

***

Es
te proyecto es autoria de Cerutti Valentino (valentino.cerutti@mi.unc.edu.ar), Viera Alfredo (alfredo.viera@mi.unc.edu.ar) y Linares Molina Jahilyn Alejandra (jahilyn.linares@mi.unc.edu.ar). En lo que duró el desarrollo del proyecto, probamos distintas técnicas para programar en equipo, tales como la división de tareas o lo que se conoce como pair programming.