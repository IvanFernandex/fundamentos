# Fundamentos de la Programación — FIUBA 🐍
 
Repositorio con los trabajos prácticos, problemas de laboratorio y material de cursada de la materia **Fundamentos de la Programación**, dictada en la Facultad de Ingeniería de la Universidad de Buenos Aires (FIUBA) — Cátedra Servetto.


## 🎓 Sobre la materia/catedra

*Fundamentos de la Programación* es una materia introductoria de la carrera de Ingeniería en Informática (y otras carreras) de FIUBA, donde se trabajan los conceptos básicos de programación: variables, estructuras de control, funciones, listas, diccionarios, manejo de archivos (texto y binarios), recursividad, backtracking y resolución de problemas.

La modalidad se baso en dos clases semanales (6hs totales) con una clase teorica donde se explicaban los temas de esa semana y una clases de modalidad practica en los laboratorios donde se buscaba resolver los problemas propuestos.

Se resolvian cuestionarios de autoevalucion y respuestas en los fotos a temas con algun foco especifico a traves del campus virtual.

Las semanas 13-16 se enfocaron en la realizacion de un proyecto final 

## 📁 Estructura del repositorio

Se omiten las semanas 8-12 ya que no se resolvieron los ejercicios de dichas semanas.

```
fundamentos/
├── Problemas-labo/      # Problemas semanales de las clases practicas
├── Teoricas-html/        # Material de las clases teóricas
├── semana2/              # Ejercicios - Semana 2
├── semana3/               # Ejercicios - Semana 3
├── semana4/               # Ejercicios - Semana 4
├── semana5/               # Ejercicios - Semana 5
├── semana6/               # Ejercicios - Semana 6
├── semana7/               # Ejercicios - Semana 7
├── semana8/               # Ejercicios - Semana 8
├── tp-grupal-semana8/    # Trabajo práctico grupal (archivos binarios / bitmap)
└── tp-final/              # Trabajo práctico grupal final de la materia
```

> La organización sigue el cronograma de la cursada: cada carpeta `semanaN` contiene los ejercicios prácticos correspondientes a esa semana.
---

## 🏆 Proyecto final integrador
 
El trabajo de `tp-final` corresponde al **Dominio B del catálogo: Gestor de inventario de un depósito** propuesto por el profesor. Es un sistema en Python que administra el stock de productos de un depósito, registrando entradas y salidas de mercadería y manteniendo las existencias actualizadas.

Funcionalidades principales:
 
- Persistencia de productos en un **archivo binario** de registros de longitud fija (código, descripción, stock, stock mínimo, precio unitario), usando el módulo `struct`.
- **Índice en memoria** (diccionario) para localizar un producto por código en tiempo O(1).
- Registro de **movimientos** de entrada y salida, con su efecto sobre el stock.
- Detección de productos por debajo de su stock mínimo (productos a reponer).
- Listado del inventario ordenado (por descripción o cantidad), con un algoritmo de ordenamiento implementado por el equipo.
- Menú de consola para operar el sistema.

 
El proyecto fue desarrollado en equipo, siguiendo las cuatro fases de la cátedra (análisis y diseño → codificación e integración → evaluación y optimización → presentación y defensa oral), con documentación interna (docstrings con precondiciones/postcondiciones), casos de análisis (normales, límite y extremos) e informe escrito final.
