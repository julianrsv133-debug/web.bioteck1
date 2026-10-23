"""Create responsive, web-ready Bioteck images from the numbered originals."""

from pathlib import Path

from PIL import Image, ImageOps


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "images" / "por-cargar" / "Imagenes Funnel Web 2.0"
DESTINATION = ROOT / "assets" / "images"


def load_image(filename: str) -> Image.Image:
    image = Image.open(SOURCE / filename)
    return ImageOps.exif_transpose(image).convert("RGB")


def export(image: Image.Image, filename: str, max_edge: int = 1800) -> None:
    image.thumbnail((max_edge, max_edge), Image.Resampling.LANCZOS)
    image.save(DESTINATION / filename, "WEBP", quality=82, method=6)
    print(f"{filename}: {image.width}x{image.height}")


def main() -> None:
    if not SOURCE.is_dir():
        raise SystemExit(f"No encuentro la carpeta de originales: {SOURCE}")

    DESTINATION.mkdir(parents=True, exist_ok=True)
    exports = [
        ("1.jpg", "fondo-bano-madera.webp", 2200),
        ("1.1 para movil.jpg", "fondo-bano-movil.webp", 1800),
        ("3 Foto principal kit.jpg", "kit-natural-care.webp", 1800),
        ("3 imagen de oferta.jpg", "oferta-kit.webp", 1600),
        ("imagen oferta funnel.png", "oferta-principal.webp", 1600),
        ("end.png", "cierre-oportunidad.webp", 1600),
        ("4.jpg", "historia-bioteck.webp", 1600),
        ("6a.png", "crema-dental-natural.webp", 1200),
        ("6b.png", "desodorante-natural.webp", 1200),
        ("6c.png", "crema-hidratante-natural.webp", 1200),
        ("7a.jpg", "guia-productos-diarios.webp", 1400),
        ("7b.jpg", "guia-inflamacion.webp", 1400),
    ]

    for source, output, max_edge in exports:
        if not (SOURCE / source).is_file():
            print(f"Se conserva {output}: no está el original {source}")
            continue
        export(load_image(source), output, max_edge)

    export(load_image("foto cepillo.png"), "cepillo-bambu.webp", 1200)

    # Preserve the full anonymized conversations. 5a remains excluded because it
    # attributes healing a child's mouth lesion to a product.
    export(load_image("5b.jpg"), "testimonio-desodorante.webp", 2000)
    export(load_image("5c.jpg"), "testimonio-rutina.webp", 2000)


if __name__ == "__main__":
    main()
