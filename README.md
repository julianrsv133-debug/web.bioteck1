# Bioteck — sitio web

Primera maqueta local del embudo de ventas de Bioteck. Está hecha con HTML, CSS y JavaScript sin framework ni dependencias de construcción, para que sea fácil de abrir, revisar y copiar a GitHub.

## Estructura

- `index.html`: landing del embudo.
- `checkout.html`: resumen del pedido y formulario contraentrega.
- `styles.css`: branding, layouts responsive y animaciones.
- `script.js`: aparición suave de secciones al desplazarse, respetando movimiento reducido.
- `checkout.js`: validación y envío opcional del pedido al webhook configurado.
- `scripts/optimize_images.py`: proceso reproducible de corrección de orientación y exportación WebP.
- `assets/images/`: imágenes optimizadas para el sitio.
- `assets/images/por-cargar/`: originales y mapa de entrega de imágenes.
- `docs/website-audit-checklist.md`: requisitos por confirmar y checklist de revisión.

## Vista local

Abre `index.html` en un navegador. La página también puede publicarse como archivos estáticos una vez que el contenido, las imágenes y el flujo de pedido estén aprobados.

## Secciones construidas

- Presentación del kit, pregunta inicial e historia de la marca.
- Dos conversaciones completas de WhatsApp sin nombres visibles; la captura sobre curación de una lesión queda fuera del sitio.
- Oferta del Kit Natural Care con dos libros digitales de regalo.
- Descripción del kit en el orden indicado: crema dental, desodorante, crema hidratante, cepillo de bambú y los dos libros digitales.
- Checkout adaptado a móviles con resumen del kit, precio, pago contraentrega y datos de entrega.

## Imágenes

Las fotografías optimizadas para la página están en `assets/images/`. Los originales de alta resolución y las capturas que no forman parte del sitio permanecen en `assets/images/por-cargar/` y se excluyen de Git. Consulta `assets/images/README.md` para repetir el proceso de optimización. Revisa el texto alternativo de cada imagen antes de publicar.

## Tipografías

Los títulos usan Georgia y la interfaz usa Inter. Inter se carga desde Google Fonts en esta primera versión; si se necesita que la página no dependa de ese servicio, se puede alojar la fuente localmente.

## Estado

Es una primera dirección visual, no una página lista para producción. El checkout muestra el precio indicado de $119.000 tachado y $77.000 COP; confirma que la oferta sigue vigente antes de conectar pedidos. El formulario no envía información mientras no se configure el webhook. No incluyas secretos en `checkout.js`; para producción conviene interponer un Cloudflare Worker y aplicar controles contra envíos automatizados. Las afirmaciones e ingredientes descritos en los productos requieren cotejo con las etiquetas, fichas oficiales y notificación sanitaria. Las conversaciones de testimonios 5b y 5c se muestran completas y sin nombres; la captura 5a que atribuye curación de una lesión a un producto queda excluida. Confirma permiso de uso y que cualquier afirmación coincide con la notificación sanitaria. Publica el formulario solo después de completar y enlazar la política de tratamiento de datos.

El fondo cálido de veta de madera está hecho en CSS como tratamiento provisional. Puede sustituirse por una fotografía de baño cuando se apruebe esa imagen.
