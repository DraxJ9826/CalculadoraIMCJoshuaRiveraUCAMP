# CalculadoraIMCJoshuaRiveraUCAMP
Proyecto de Python - Calculadora de IMC
Este proyecto es una Calculadora de IMC (Índice de Masa Corporal) desarrollada en Python.
El programa solicita al usuario datos personales como nombre, apellidos, edad, peso y estatura, calcula el IMC y muestra:
-El valor del IMC con dos decimales.
-La categoría según el IMC (Bajo peso, Peso normal, Sobrepeso, Obesidad).
-El rango de peso recomendado según el IMC normal (18.5–24.9) cosa que no se pedia en el entregable, pero me parecio un detalle bonito.

El objetivo principal es practicar entrada de datos, validaciones, estructuras de datos (listas y diccionarios) y cálculos matemáticos en Python.

Cómo se realizó el programa
1. Funciones de validación: 
   - `pedirNumero()` para validar números (int o float) y rangos sensatos.  
   - `pedirNombre()` para validar nombres y apellidos (solo letras y espacios).  

2. Almacenamiento de datos:  
   - Cada persona se guarda como un diccionario con sus datos y el IMC calculado.  
   - Todos los diccionarios se almacenan en una lista para procesarlos de manera ordenada segun como se fueron ingresando.
   - En un punto pensé que podria tal vez acomodarlo pero ya según lo que se requiera, ejemplo, se acomoda por peso de menor a mayor o por orden alfabetico, pero es una cuestion aparte del entregable  

3. Cálculo del IMC:  
4. Rango de peso recomendado:  
   IMC = peso/estatura^2  
   Segun el peso recomendado (buscando estos datos en internet) se realiza la clasificacion
   Luego se clasifica automáticamente en: Bajo peso, Peso normal, Sobrepeso u Obesidad para comentarle al usuario.  

5. Interfaz de usuario:  
   - Mensajes claros para cada entrada teniendo en cuenta que es un programa de consola.  
   - Validaciones para que no se deje ningún campo vacío ni se ingresen datos inválidos.  
   - Resultados finales claros y organizados.  
