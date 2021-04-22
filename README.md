# [P06](https://github.com/erumabo/2021s1-p06)

Programa para la asignación P06 del curso Proyecto de Ingeniería de Software, IS 2021

## Descripción

Hacer un programa que haga un CRUD de una tabla en una base de datos MySql.

La base de datos debe estar ubicada en una pc de manera local y el programa debe ser escrito en el ambiente android, y ejecutarse desde un celular.  Se deben mostrar ambos: la tabla en la pc y los datos de la tabla en el celular.

De no conectar la aplicación ejecutandose en móvil con la base datos en su pc de manera local y con sincronización en tiempo real, la nota es 0.

Es un trabajo estrictamente individual.

En la revisión deberán abrir sus códigos y explicar la estructura del programa y su función, además deberan ejecutar sus códigos. El funcionamiento incorrecto al momento de la ejecución no es justificacion válida y se les bajaran los puntos correspondientes. 

Recomendación: Realizar un programa simple, evitar olores de software y documentar bien su código. Antes de la revisión asegurese que el programa corre correctamente.

## Solución

La aplicación está hecha usando el _framework_ [Quasar v1.15](https://quasar.dev/) con [Vue v2](https://vuejs.org/) y convertida a una aplicación Android mediante [Capacitor v2](https://capacitorjs.com/).
Para la base de datos se usa MySQL en un contenedor [Docker](https://hub.docker.com/_/mysql/) y un API hcho con [Python Bottle](https://bottlepy.org/docs/0.12/index.html) para interactuar con ella.
