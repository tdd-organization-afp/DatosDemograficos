# Curso de programación para QA

[![Build Status](https://travis-ci.org/tdd-organization-afp/DatosDemograficos.svg?branch=master)](https://travis-ci.org/github/tdd-organization-afp/DatosDemograficos)


[![codecov](https://codecov.io/gh/tdd-organization-afp/DatosDemograficos/branch/master/graph/badge.svg)](https://codecov.io/gh/tdd-organization-afp/DatosDemograficos)


Plantilla para el [curso de desarrollo para QA](https://jj.github.io/curso-tdd)

## Visualizador de información demográfica

Esta api aceptará diferentes datos sobre la demografía española recogidos en el INE y los transformará para poder visualizarlos de diferentes formas.

## Herramientas que van a utilizarse

La elección de estas herramientas se discute en un [issue](https://github.com/tdd-organization-afp/tdd-provisional/issues/7) y se irán modificando en función de las necesidades que tenga el proyecto.

- Lenguaje: `Python`.
- Logging: mecanismo interno del lenguaje o `Logstach`.
- Configuración remota: `etcd`.
- Aplicación web: `Flask`.
- Gráficas: `Matplotlib` y `Geopandas`.

## Estructura del proyecto

La estructura principal se encuentra dentro de la carpeta [DatosDemograficos](https://github.com/tdd-organization-afp/DatosDemograficos/tree/master/DatosDemogr%C3%A1ficos). Ahí se localizan todos los archivos relativos a la API, el frontend...

Además, también hemos incluido un archivo [requirements.txt](https://github.com/tdd-organization-afp/DatosDemograficos/blob/master/requirements.txt) con los requisitos necesarios para el proyecto.

## Colaboradores

| Usuario |
|---------|
| @morevi  |
| @aure-nogueras  |
| @PedroMFC  |

## Instrucciones

Tanto para ejecutar los tests como para instalar las dependencias es necesario tener instalado `poetry`. Para la instalación de dependencias se usará la orden

```console
poetry install
```

o si se desean actualizar las mismas

```console
poetry update
```

# Tests

Por su parte, para ejecutar los archivos con los tests se puede usar la orden

```console
python3 -m pytest ../tests/test_*.py
```

Sin embargo, se puede usar `taskipy` como *task runner* y ejecutar los tests de una manera más sencilla junto con la funcionalidad que proporciona `poetry` ejecutando la orden

```console
poetry run task test
```

donde `test` puede ser sustituida por cualquier otra tarea para ejecutar los archivos de tests.

# Tests de cobertura

Para ejecutar los tests de cobertura desde el ejecutor de tareas, se usará

```console
poetry run task coverage
```

