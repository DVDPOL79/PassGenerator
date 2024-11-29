# Historias de Usuario para el Generador de Contraseñas

## Historia de Usuario 1: Configuración básica de la contraseña
**Como** usuario,  
**quiero** poder generar una contraseña segura indicando solo la longitud deseada,  
**para** proteger mis cuentas de accesos no autorizados.

### Criterios de aceptación
- El sistema debe permitir al usuario especificar la longitud de la contraseña.
- La contraseña generada debe incluir al menos un tipo de carácter (letras, números o símbolos).

---

## Historia de Usuario 2: Personalización de caracteres incluidos
**Como** usuario,  
**quiero** seleccionar los tipos de caracteres que se incluirán en mi contraseña (mayúsculas, minúsculas, números y/o caracteres especiales),  
**para** ajustarla a los requisitos de diferentes plataformas.

### Criterios de aceptación
- El sistema debe preguntar si se incluirán:
  - Mayúsculas.
  - Minúsculas.
  - Números.
  - Caracteres especiales.
- El generador debe validar que al menos un tipo de carácter sea seleccionado.

---

## Historia de Usuario 3: Evitar caracteres ambiguos
**Como** usuario,  
**quiero** poder excluir caracteres ambiguos como `l`, `I`, `1`, `O` y `0` de la contraseña,  
**para** evitar confusiones al usarla.

### Criterios de aceptación
- El sistema debe incluir una opción para evitar caracteres ambiguos.
- Si la opción está activada, los caracteres ambiguos no deben aparecer en la contraseña generada.

---

## Historia de Usuario 4: Guardar contraseñas en un archivo
**Como** usuario,  
**quiero** tener la opción de guardar las contraseñas generadas en un archivo,  
**para** acceder a ellas fácilmente cuando las necesite.

### Criterios de aceptación
- El sistema debe preguntar al usuario si desea guardar la contraseña.
- Si el usuario elige guardar, la contraseña debe añadirse a un archivo llamado `contrasenas.txt`.

---

## Historia de Usuario 5: Validación de entradas
**Como** usuario,  
**quiero** recibir mensajes claros cuando ingreso valores inválidos,  
**para** evitar errores en el proceso de generación de contraseñas.

### Criterios de aceptación
- El sistema debe validar que la longitud de la contraseña sea un número entero mayor a 0.
- El sistema debe mostrar mensajes claros si no se selecciona ningún tipo de carácter o si la longitud es inválida.
