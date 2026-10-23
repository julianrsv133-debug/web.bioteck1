# Imágenes del sitio Bioteck

Guarda aquí las imágenes aprobadas para la web. Mantén los nombres descriptivos y en minúsculas; usa `.webp` o `.avif` cuando sea posible y conserva los originales fuera del sitio.

Archivos previstos para esta primera sección:

- `fondo-bano-madera.webp` y `fondo-bano-movil.webp`: fondos panorámico y vertical del baño con madera y plantas.
- `kit-natural-care.webp`: foto principal horizontal del kit.
- `historia-bioteck.webp`: imagen lifestyle para presentar la rutina de marca.
- `oferta-kit.webp`: composición del kit para el bloque de oferta.
- `crema-dental-natural.webp`, `desodorante-natural.webp`, `crema-hidratante-natural.webp` y `cepillo-bambu.webp`: fotos de los productos.
- `guia-productos-diarios.webp` y `guia-inflamacion.webp`: portadas de los libros digitales.
- `testimonio-desodorante.webp` y `testimonio-rutina.webp`: recortes 5b y 5c, sin nombres visibles. `5a` se excluye del sitio porque atribuye una curación a un producto.

## Medidas recomendadas

- Fondo del sitio: 2400 × 1600 px (horizontal); opcional móvil, 1080 × 1920 px (vertical).
- Foto principal del kit: 1800 × 1200 px (horizontal, 3:2).
- Foto de oferta: 1400 × 1400 px (cuadrada) o 1600 × 1200 px (horizontal).
- Productos individuales: 1200 × 1200 px (cuadradas), con el producto centrado y aire alrededor.
- Historia de marca: 1200 × 1500 px (vertical) o 1500 × 1200 px (horizontal).
- Testimonios: 1080 × 1350 px (vertical) o video vertical 1080 × 1920 px.
- Portadas de libros digitales: 1000 × 1400 px (vertical).
- Logo: SVG preferido; PNG transparente si no hay SVG.

Para fotografías, WebP es el formato recomendado para la web. Puedes enviarme los originales en JPG, PNG o WebP; si todavía no los tienes optimizados, puedo preparar las copias web al integrarlos. Evita enviar capturas de pantalla cuando exista el archivo original. Mantén el producto o sujeto principal cerca del centro para que el recorte adaptable no lo corte.

## Optimización repetible

Los originales se conservan localmente en `por-cargar/Imagenes Funnel Web 2.0/` y se excluyen de GitHub para no exponer capturas ni datos de clientes. Las copias WebP optimizadas sí forman parte del sitio. Para repetir la conversión en otro equipo, copia allí los originales, instala Pillow para Python y ejecuta `python scripts/optimize_images.py` desde la raíz del proyecto. El proceso corrige la orientación EXIF, mantiene la relación de aspecto y genera las exportaciones WebP.

No subas datos personales de clientes ni testimonios sin autorización. Cada imagen debe tener texto alternativo descriptivo en `index.html`.
