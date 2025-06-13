# Trabajo académico de Visualización de Datos

- **Alumno**: Adrián Martínez Martínez
- **Asignatura**: Visualización de Datos
- **Titulación**: Máster en Inteligencia Artificial, Reconocimiento de Formas e Imagen Digital (MIARFID)
- **Institudión**: Universidad Politécnica de Valencia (UPV)

El objetivo del proyecto es desrrollar y publicar una página de visualización de datos utilizando la librería `streamlit` y `streamlit cloud`.

## 🏆 Objetivo

La página web debe servir para analizar y visualizar un conjunto de datos elegido por el alumno. El conjunto de datos debe ser susceptible de ser visualizado con mapas, por lo tanto, la información debe ser georreferenciada. En la página web se mostrarán gráficas y mapas utilizando los conocimientos adquiridos a lo largo del curso.

## 📑 Datos utilizados

Los datos utilizados han sido extraidos de la página web [Our World in Data](https://ourworldindata.org/) y, dado la naturaleza del plan de estudios del máster, se han elegido datos sobre Inteligencia Artifical en cuestiones como inversión por páis, número de publicaciones en el campo, etc.

Los mapas se han obtenido de la web [GeoJSON Maps of the globe](https://geojson-maps.kyd.au/).

## 🤓 Extras

Se ha utilizado el componente [timeline](https://github.com/innerdoc/streamlit-timeline), que no se vio en clase, pero explorando los [componentes](https://streamlit.io/components) disponibles de streamlit, esta linea temporal complementaba muy bien la idea de la aplicación.

- **Documentación** del formato del `.json` de datos: https://timeline.knightlab.com/docs/json-format.html

## ✨ Características de la Aplicación

La aplicación web ofrece las siguientes visualizaciones y análisis sobre datos de Inteligencia Artificial:

*   **Plots Interactivos:** Gráficos de barras y de dispersión para explorar publicaciones anuales, y gráficos de líneas para la evolución de la inversión global en IA.
*   **Mapas Detallados:** Visualizaciones coropléticas de publicaciones anuales por país y de inversión privada en IA por regiones.
*   **Análisis Comparativo de Inversión:** Una página dedicada a comparar tendencias entre la inversión global en IA generativa y la inversión privada total en IA.
*   **Línea de Tiempo Histórica:** Un recorrido interactivo por eventos y eras significativas en la historia de la IA.
*   **Mejoras generales:** Se han implementado mejoras en la precisión de los datos en mapas, opciones de visualización (como escalas logarítmicas) y claridad en la presentación de la información.