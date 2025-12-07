# IPC2DIC_Proyecto1_8
Desarrollar un sistema integral capaz de simular una plataforma de gestión de recursos mediante la implementación de estructuras de datos enlazadas, el procesamiento y generación de archivos XML

## Objetivos especícos
* Implementar estructuras de datos enlazadas (listas simples, dobles, circulares, pilas o colas de prioridad)

* Precesar archivos XML de entrada con múltiples configuraciones y generar archivos XML de salida

* Realizar reportes gráficos utilizando Graphviz

## Enunciado
El funcionamiento del sistema dependerá del procesamiento de un archivo XML de entrada, el
cual contendrá la configuración completa de centros de datos, máquinas virtuales,
contenedores y solicitudes, además de instrucciones para realizar operaciones como creación
de recursos, migración, balanceo de carga o procesamiento de solicitudes. 

El sistema deberá
interpretar este archivo, validar su estructura y ejecutar las acciones que corresponda según lo
especificado.

Se deberá generar un archivo XML de salida que contenga un resumen del estado final del
sistema, estadísticas de utilización de recursos, operaciones realizadas y alertas detectadas
durante la ejecución.

De manera adicional, será necesario generar reportes visuales mediante Graphviz, con el
objetivo de representar gráficamente la estructura de los centros de datos, las máquinas
virtuales, los contenedores, la cola de solicitudes o cualquier otra representación que facilite la
comprensión del estado del sistema.

## Archivo de entrada para el programa
El sistema deberá de ser capaz de recibir un archivo de entrada el cuál será el siguiente:

```
<?xml version="1.0" encoding="UTF-8"?>
<cloudSync>
    <configuracion>
        <centrosDatos>
            <centro id="DC001" nombre="DataCenter Principal">
                <ubicacion>
                    <pais>Guatemala</pais>
                    <ciudad>Guatemala City</ciudad>
                </ubicacion>
                <capacidad>
                    <cpu>64</cpu>
                    <ram>256</ram>
                    <almacenamiento>500</almacenamiento>
                </capacidad>
            </centro>
            <centro id="DC002" nombre="DataCenter Respaldo">
                <ubicacion>
                    <pais>Guatemala</pais>
                    <ciudad>Antigua Guatemala</ciudad>
                </ubicacion>
                <capacidad>
                    <cpu>32</cpu>
                    <ram>128</ram>
                    <almacenamiento>300</almacenamiento>
                </capacidad>
            </centro>
        </centrosDatos>
        <maquinasVirtuales>
            <vm id="VM001" centroAsignado="DC001">
                <sistemaOperativo>Ubuntu 22.04 LTS</sistemaOperativo>
                <recursos>
                    <cpu>8</cpu>
                    <ram>16</ram>
                    <almacenamiento>100</almacenamiento>
                </recursos>
                <ip>192.168.1.10</ip>
                <contenedores>
                    <contenedor id="CNT001">
                        <nombre>WebServer</nombre>
                        <imagen>nginx:latest</imagen>
                        <recursos>
                            <cpu>30</cpu>
                            <ram>512</ram>
                        </recursos>
                        <puerto>8080</puerto>
                    </contenedor>
                </contenedores>
            </vm>
            <vm id="VM002" centroAsignado="DC001">
                <sistemaOperativo>Windows Server 2022</sistemaOperativo>
                <recursos>
                    <cpu>4</cpu>
                    <ram>8</ram>
                    <almacenamiento>80</almacenamiento>
                </recursos>
                <ip>192.168.1.11</ip>
                <contenedores>
                    <contenedor id="CNT002">
                        <nombre>Database</nombre>
                        <imagen>mysql:8.0</imagen>
                        <recursos>
                            <cpu>50</cpu>
                            <ram>1024</ram>
                        </recursos>
                        <puerto>3306</puerto>
                    </contenedor>
                </contenedores>
            </vm>
        </maquinasVirtuales>
        <solicitudes>
            <solicitud id="REQ001">
                <cliente>Empresa Demo</cliente>
                <tipo>Deploy</tipo>
                <prioridad>8</prioridad>
                <recursos>
                    <cpu>4</cpu>
                    <ram>8</ram>
                    <almacenamiento>50</almacenamiento>
                </recursos>
                <tiempoEstimado>30</tiempoEstimado>
            </solicitud>
            <solicitud id="REQ002">
                <cliente>Cliente Prueba</cliente>
                    <tipo>Backup</tipo>
                    <prioridad>5</prioridad>
                    <recursos>
                        <cpu>2</cpu>
                        <ram>4</ram>
                        <almacenamiento>100</almacenamiento>
                    </recursos>
                <tiempoEstimado>60</tiempoEstimado>
            </solicitud>
        </solicitudes>
    </configuracion>
    <instrucciones>
        <instruccion tipo="crearVM">
            <id>VM003</id>
            <centro>DC002</centro>
            <so>Debian 11</so>
            <cpu>4</cpu>
            <ram>8</ram>
            <almacenamiento>60</almacenamiento>
        </instruccion>
            <instruccion tipo="migrarVM">
            <vmId>VM001</vmId>
            <centroOrigen>DC001</centroOrigen>
            <centroDestino>DC002</centroDestino>
            </instruccion>
            <instruccion tipo="procesarSolicitudes">
            <cantidad>2</cantidad>
        </instruccion>
    </instrucciones>
</cloudSync>
```

## Identificadores y nombres
En todo el archivo, los elementos como centros de datos, máquinas virtuales, contenedores ysolicitudes utilizan IDs y nombres únicos.
Esto permite que el sistema los identifique sin confusión y relacione instrucciones 
con los recursos adecuados.

## Recursos principales del sistema

### CPU (en centros y VMs):
Representa la cantidad de núcleos de procesamiento disponibles o utilizados.(no en
porcentaje).

### RAM:
Indica la cantidad de memoria en gigabytes que un centro o una VM puede utilizar.

#### Almacenamiento:
Define el espacio disponible para instalar máquinas, sistemas operativos, contenedores o
archivos.

### CPU y RAM en contenedores
Los contenedores consumen recursos dentro de una VM:
* CPU (porcentaje) → cuánto del CPU de la VM utilizará el contenedor.
* RAM (MB) → memoria reservada en MB para la aplicación dentro del contenedor.
Estos valores permiten calcular el uso total y las limitaciones de la VM que los hospeda.

## Solicitudes del sistema
Una solicitud representa una tarea enviada por un cliente que requiere recursos del sistema.
Estas solicitudes se insertan en una cola de prioridad, donde las más urgentes se procesan
primero.

### Campos importantes
* Cliente: quién solicita la operación.
* Tipo de solicitud: acción específica que se debe realizar.
* Prioridad: valor entre 1 y 10 que determina su urgencia (10 = más urgente).
* Recursos: CPU, RAM y almacenamiento requeridos para atender la solicitud.
* Tiempo estimado: duración aproximada para completar la tarea, este será un tiempo
simulado, no es necesario simular en tiempo real.

### Tipos de solicitudes:
|Tipo  | Explicaión | 
|:--   |:--         |
|Deploy| Crea una nueva VM con el id de la solicitud y la asigna al data center con más recursos disponibles |   
|Backup| Crea una nueva VM en estado suspendida, con el id de la solicitud y la asigna al data center con más recursos disponibles |   

## Instrucciones del sistema
Las instrucciones indican acciones que el sistema debe ejecutar después de cargar el archivo.
Estas acciones pueden modificar recursos o el estado del sistema.

### Tipos de instrucciones y su función
|Tipo   | Explicaión | 
|:--    |:--         |
| crearVM | Ordena crear una nueva máquina virtual dentro de un centro específico, validando si hay recursos suficientes |   
| migrarVM | Traslada una VM de un centro a otro. Se deben verificar recursos y disponibilidad. |  
| PrecesarSolicitudes | Indica cuántas solicitudes deben tomarse de la cola de prioridad para ser ejecutadas. | 

## Consola del sistema
La aplicación deberá de contar con las siguientes funcionalidades:

### Menu principal
* Cargar archivo XML
* Gestión de centros de datos 
* Gestión de máquinas virtuales
* Gestión de contenedores
* Gestión de solicitudes
* Reporte graphviz
* Generar XML de salida
* Historial de operacones
* Salir

#### Carga archivo XML
 El sistema debe de ser capaz de recibir un archivo de entrada xml y imprimir la carga de centros de datos, VM, Solicitudes y instrucciones

 #### Gestión de centro de datos:
  Esta opción debería de contar con las opciones descritas
 | Opciónes | Función | Descripción | Formato |
|:-----|:--|:--|:--|
| Listar todos los centros|Mostrar todos los centros registrados|Despliega en pantalla la información completa de cada centro de datos, incluyendo recursos totales, disponibles, porcentaje usado y cantidad de VMs activas||
| Buscar centro por ID|Buscar y mostrar lainformación de un centro específico | Permite ingresar el ID y muestra únicamente los datos del centro. Si no existe debe de mostrar un mensaje de error|Mismo formato que el listado, pero solo para el centro encontrado.      |Adelante (H3P2)|   
| Ver centro con más recursos|Mostrar el centro con mayor disponibilidad |Calcula qué centro tiene más recursos disponibles (CPU, RAM y Almacenamiento)|El formato debe ser igual al de listar todos los centros pero con el centro con más recursos.|
| Volver al menú principal|Regresar al menú general|Cierra el submenú y vuelve al menú princpal Regar|Sin formato|   

### Gestión de máquinas virtuales: Deberá contener las siguientes opciones
 | Opciónes | Función | Descripción | Formato |
|:-----|:--|:--|:--|
|Bucar VM por ID|Buscar una máquina virtual específica|Permite ingresar un ID y muestra toda la información de VM, incluyendo sistemas operativo, recursos asignados, centro en el que se encuentra y contenedores que ejecuta. Si la VM no existe, mostrar mensaje de error||
|Listar VM de un centro| Mostrar todas las VM alojadas en un centro específico|Solicita el ID del centro de datos y despliega una lista detallada de todas las máquinas virtuales registradas en ese centro, junto con sus recursos y estado general.||
|Migrar VM entre centros|Mover una VM a otro centro de datos|Permite seleccionar una máquina virtual y trasladarla a otro centro. El sistema debe validar que el centro destino tenga los recursos suficientes para recibirla. También debe actualizar los recursos disponibles en ambos centros.|No requier ningún formato especil|
|Vover al menú principal|Regresar al menú general|Cierra este submenú y vuelve al menú principal del programa.|No requier formato especial.|

### Gestión de contenedores: Deberá contener las siguientes opciones
| Opciónes | Función | Descripción | Formato |
|:-----|:--|:--|:--|
|Desplegar contenedor en VM|Crear e inicia un nuevo contenedor dentro de una máquina vitual|Permite seleccionar una VM, asignarle un contenedor con nombre, imagen y recursos específicos (CPU,RAM,Almacenamiento) y desplegarlo si la VM tiene los recursos suficientes tambien actualiza el uso de recursos en la VM del despliegue| no requiere formato|
|Listar contenedores de una VM|Mostrar todos los contenedores alojados en una VM específica|Solicita el ID de la máquina virtual y muestra la lista de contenedores con sus recursos|Muestra el ID de la maquina su estado y sus CPU y RAM|
|Cambiar estado de contenedor|Pausar,Reiniciar o Activar un contenedor|Permite modificar el estado operativo del contenedor|No requiere formato|
|Eliminar contenedor|Eliminar un contenedor de una VM| Elimina un contenedor existente y libera los recursos que estaba utilizando dentro de la VM,si el contenedor no existe mostrar un mensaje de error|No requier formato|
|Volver al menú principipal| Regresar al menú general|Cierra este submenú y retorna al menú principal del sistema.|No requiere formato|

### Gestión de solicitudes, el sistema debe de ser capaz de poder atender las solicitudes
| Opciónes | Función | Descripción | Formato |
|:-----|:--|:--|:--|
|Agregar nueva solicitud|Insertar una solicitud en la cola de prioridad|Permite crear una nueva solicitud indicando si ID, cliente, tipo, prioridad, recursos y tiempo estimado. La solicituda se inserta en una cola donde la prioridad más alta se procesan primero.|No requiere un formato|
|Procesar solicitud de mayor prioridad|Atender la solicitud más urgente de la cola|Extrae y procesa únicamente la solicitud con mayor prioridad. El sistema debe verificar que existan recursos suficientes en los centros o MV|No requiere formato|
|Procesar N solicitudes|Atender varias solicitudes en orden de prioridad|Permite procesar una cantidad específica N de solicitudes. Si no hay suficientes procesa todas las disponibles|Mostrar las solicitudes que se procesaron de una manera correcta|
|Ver cola de solicitudes|Mostrar todas las solicitudes pendientes ordenadas por prioridad|Lista todas las solicitudes actualmente en espera, ordenadas de mayor a menor prioridad|Muesta cliente, tipo, prioridad, recursos requeridos y tiempo estimando|
|Ver cola de solicitudes|Mostrar todas las solicitudes pendientes ordenadas por prioridad|Lista todas las solicitudes actualmente en espera ordenades de mayor a menor prioridad|Muestra cliente, tipo, prioridad, recursos requeridos y tiempo estimado.|

## Archivo de salida XML
Se deberá generar un archivo de salida con el siguiente formato:

```
<?xml version="1.0" ?>
<resultadoCloudSync>
    <timestamp>2025-12-01T16:30:49.716569</timestamp>
    <estadoCentros>
        <centro id="DC001">
            <nombre>DataCenter Principal</nombre>
            <recursos>
                <cpuTotal>64</cpuTotal>
                <cpuDisponible>56</cpuDisponible>
                <cpuUtilizacion>12.50%</cpuUtilizacion>
                <ramTotal>256</ramTotal>
                <ramDisponible>240</ramDisponible>
                <ramUtilizacion>6.25%</ramUtilizacion>
            </recursos>
            <cantidadVMs>2</cantidadVMs>
            <cantidadContenedores>1</cantidadContenedores>
        </centro>
        <centro id="DC002">
            <nombre>DataCenter Respaldo</nombre>
            <recursos>
                <cpuTotal>32</cpuTotal>
                <cpuDisponible>20</cpuDisponible>
                <cpuUtilizacion>37.50%</cpuUtilizacion>
                <ramTotal>128</ramTotal>
                <ramDisponible>104</ramDisponible>
                <ramUtilizacion>18.75%</ramUtilizacion>
            </recursos>
            <cantidadVMs>2</cantidadVMs>
            <cantidadContenedores>1</cantidadContenedores>
        </centro>
    </estadoCentros>
    <estadisticas>
        <vmsActivas>4</vmsActivas>
        <contenedoresTotales>2</contenedoresTotales>
    </estadisticas>
</resultadoCloudSync>
```
## Reportes 
El sistema deberá generar reportes gráficos utilizando Graphviz para visualizar de manera estructurada el estado de los recursos administrados. Como mínimo, se deben incluir cuatro

reportes:

* un reporte general de los centros de datos registrados

* un reporte de las máquinas virtuales alojadas en un centro específico seleccionado por su ID

* un reporte de los contenedores desplegados en una máquina virtual seleccionada por ID

* un reporte de la cola de solicitudes, mostrando su orden de prioridad

Los datos específicos mostrados en cada reporte, así como el diseño visual, colores, estilos, formas de nodos y detalles adicionales, quedan completamente a libre elección.
