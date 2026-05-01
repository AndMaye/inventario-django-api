# 🧾 Inventario API con Django REST Framework

Este proyecto es una API REST desarrollada con Django y Django REST Framework para la gestión de un sistema de inventario.

Permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre productos.

---

## 🚀 Funcionalidades

- 📦 Crear productos
- 📋 Listar productos
- 🔍 Ver detalle de un producto
- ✏️ Actualizar productos
- 🗑️ Eliminar productos

---

## 🔗 Endpoints de la API

### 📦 Productos

- `GET /api/productos/` → Listar todos los productos  
- `POST /api/productos/` → Crear nuevo producto  
- `GET /api/productos/{id}/` → Ver producto por ID  
- `PUT /api/productos/{id}/` → Actualizar producto  
- `DELETE /api/productos/{id}/` → Eliminar producto  

---

## 🧪 Ejemplo de JSON (POST / PUT)

```json id="readme2"
{
  "nombre": "Teclado gamer",
  "descripcion": "Teclado mecánico RGB",
  "precio": "120000",
  "stock": 15
}
🛠️ Tecnologías usadas
Python
Django
Django REST Framework
SQLite
🎯 Objetivo del proyecto

Este proyecto fue desarrollado como práctica de backend para fortalecer habilidades en:

Desarrollo de APIs REST
Manejo de bases de datos
Arquitectura backend con Django

En CMD:

```bash id="git1"
git add .
git commit -m "README profesional para portafolio"
git push
