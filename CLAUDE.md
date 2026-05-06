# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Comandos de desarrollo

El entorno virtual está en `.venv/` (raíz del repositorio). El proyecto Django vive en `proyecto_portafolio/`. Todos los comandos de Django se ejecutan desde esa subcarpeta.

```bash
# Activar el entorno virtual (PowerShell en Windows)
.\.venv\Scripts\Activate.ps1

# Servidor de desarrollo
cd proyecto_portafolio
python manage.py runserver

# Migraciones
python manage.py makemigrations
python manage.py migrate

# Recolectar archivos estáticos (necesario antes del despliegue)
python manage.py collectstatic --noinput

# Crear superusuario para el admin de Django
python manage.py createsuperuser

# Ejecutar tests
python manage.py test

# Ejecutar tests de una sola app
python manage.py test portfolio
python manage.py test dashboard
```

## Variables de entorno

| Variable | Por defecto | Uso |
|---|---|---|
| `DJANGO_SECRET_KEY` | clave insegura para dev | Clave secreta de Django |
| `DEBUG` | `False` | Activar modo debug (`true`/`1`/`yes`) |
| `ALLOWED_HOSTS` | `*` | Hosts permitidos separados por comas |
| `DATABASE_URL` | SQLite local | URL de conexión a base de datos (PostgreSQL en producción) |

Para desarrollo local: crear un archivo `.env` en `proyecto_portafolio/` con `DEBUG=true`.

## Arquitectura

El repositorio contiene un solo proyecto Django (`proyecto_portafolio/`) con dos apps:

### `portfolio` — Portafolio público
- **`/`** → `views.home` → `templates/portfolio/home.html`
- **`/projects/`** → `views.ProjectListView` → `templates/portfolio/projects.html`
- Modelo `Project`: título, descripción, imagen (`ImageField`, sube a `media/projects/`), URL del proyecto, URL de GitHub.

### `dashboard` — Sección de datos/análisis
- **`/dashboard/`** → `views.dashboard_home` → `templates/dashboard/dashboard.html`
- Actualmente sin modelos propios; la app está pensada para visualizaciones de datos.

### Plantillas y estáticos
- `templates/base.html` — plantilla base con navbar, Font Awesome 5, Particles.js y Google Fonts (Playfair Display).
- `static/css/style.css` — hoja de estilos global única.
- `static/img/` y `static/js/` — activos estáticos del proyecto.
- Las URLs del navbar usan namespaces: `portfolio:home`, `portfolio:projects`, `dashboard:dashboard_home`.

### Base de datos
- Desarrollo: SQLite (`db.sqlite3`, excluido del repositorio).
- Producción: PostgreSQL vía variable de entorno `DATABASE_URL` (configurado con `dj-database-url`).

### Despliegue (Heroku-style)
- `Procfile` ejecuta `collectstatic` + Gunicorn en el arranque.
- WhiteNoise sirve los archivos estáticos en producción (middleware configurado).
- Python 3.12.8 especificado en `runtime.txt`.

## Dependencias importantes

- `Pillow` **no está en `requirements.txt`** pero el modelo `Project` usa `ImageField`. Si se trabaja con imágenes en local, instalar manualmente: `pip install Pillow`.
- `psycopg[binary]` está incluido para PostgreSQL, aunque en local se usa SQLite.
