#!/usr/bin/env python3
"""Render a PDF's first two pages as a straight (unrotated) stack, PNG w/ transparent bg.

Page 2 sits in front (it usually has a figure), offset down/right just far enough
that page 1's title + authors still peek out above it. Page 2 itself is cropped
shortly after its first figure (a bit of body text shows below it) rather than
shown in full, and the freed vertical space is used to enlarge the whole stack.

Usage:
    python3 scripts/make_paper_preview.py <input.pdf> <output.png> \\
        [--dpi 300] [--width 1600] [--height 900] [--reveal 0.32] [--offset-x 0.10] \\
        [--page2-crop 0.52] [--fill 0.92]
"""

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter


def rasterize_pages(pdf_path, num_pages, dpi, tmp_dir):
    prefix = str(Path(tmp_dir) / "page")
    subprocess.run(
        ["pdftoppm", "-png", "-r", str(dpi), "-f", "1", "-l", str(num_pages), str(pdf_path), prefix],
        check=True,
    )
    return sorted(Path(tmp_dir).glob("page-*.png"))


def add_border(page_rgba, width=3, color=(210, 210, 210, 255)):
    """A thin keyline around the page so overlapping pages read as distinct
    sheets even where the drop shadow between them is subtle."""
    bordered = page_rgba.copy()
    draw = ImageDraw.Draw(bordered)
    w, h = bordered.size
    draw.rectangle([0, 0, w - 1, h - 1], outline=color, width=width)
    return bordered


def make_shadow(page_rgba, blur_radius, opacity):
    alpha = page_rgba.split()[-1]
    shadow = Image.new("RGBA", page_rgba.size, (0, 0, 0, 0))
    shadow.paste((0, 0, 0, opacity), mask=alpha)
    return shadow.filter(ImageFilter.GaussianBlur(blur_radius))


def build_stack(page_files, canvas_w, canvas_h, reveal_frac, offset_x_frac, page2_crop_frac, fill_frac):
    canvas = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))

    # Shadow falls down/right of whichever page is on top, like light from the upper left.
    # Soft and wide rather than tight/dark, for a more elegant "resting on top" look.
    shadow_offset = (10, 14)
    shadow_blur = 40
    shadow_opacity = 90

    raw_back = Image.open(page_files[0]).convert("RGBA")
    raw_front = Image.open(page_files[1]).convert("RGBA")

    # Solve for the scale that makes (revealed sliver of page 1) + (cropped page 2)
    # fill `fill_frac` of the canvas height, so cropping page 2 shorter lets everything
    # else scale up rather than leaving empty space.
    orig_h = raw_back.height
    stack_h_frac = reveal_frac + page2_crop_frac
    scale = (canvas_h * fill_frac) / (orig_h * stack_h_frac)

    def scaled(img):
        return img.resize((int(img.width * scale), int(img.height * scale)), Image.LANCZOS)

    back_page_full = scaled(raw_back)
    front_page_full = scaled(raw_front)
    front_page = front_page_full.crop((0, 0, front_page_full.width, int(front_page_full.height * page2_crop_frac)))

    reveal_px = int(back_page_full.height * reveal_frac)
    offset_x = int(back_page_full.width * offset_x_frac)
    front_w, front_h = front_page.size

    # Crop page 1 to align with page 2's bottom edge, instead of letting its
    # untouched remainder hang far below/off the canvas.
    total_h = reveal_px + front_h
    back_page = add_border(back_page_full.crop((0, 0, back_page_full.width, total_h)))
    front_page = add_border(front_page)
    back_w, back_h = back_page.size
    total_w = max(back_w, front_w + offset_x)
    group_x = (canvas_w - total_w) // 2
    back_x = group_x
    back_y = (canvas_h - total_h) // 2
    front_x = group_x + offset_x
    front_y = back_y + reveal_px

    back_shadow = make_shadow(back_page, shadow_blur, shadow_opacity)
    canvas.alpha_composite(back_shadow, (back_x + shadow_offset[0], back_y + shadow_offset[1]))
    canvas.alpha_composite(back_page, (back_x, back_y))

    front_shadow = make_shadow(front_page, shadow_blur, shadow_opacity)
    canvas.alpha_composite(front_shadow, (front_x + shadow_offset[0], front_y + shadow_offset[1]))
    canvas.alpha_composite(front_page, (front_x, front_y))

    return canvas


def fit_to_aspect(img, aspect_w, aspect_h, margin_frac=0.035):
    """Trim to the content's bounding box (plus a small margin) and re-pad to the
    target aspect ratio, so a fixed-aspect CSS box isn't mostly empty margin."""
    bbox = img.getbbox()
    if not bbox:
        return img
    x0, y0, x1, y1 = bbox
    w, h = x1 - x0, y1 - y0
    mx, my = int(w * margin_frac), int(h * margin_frac)
    x0, y0 = max(0, x0 - mx), max(0, y0 - my)
    x1, y1 = min(img.width, x1 + mx), min(img.height, y1 + my)
    content = img.crop((x0, y0, x1, y1))

    cw, ch = content.size
    target_ratio = aspect_w / aspect_h
    if cw / ch > target_ratio:
        canvas_w, canvas_h = cw, int(cw / target_ratio)
    else:
        canvas_h, canvas_w = ch, int(ch * target_ratio)

    fitted = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))
    fitted.paste(content, ((canvas_w - cw) // 2, (canvas_h - ch) // 2), content)
    return fitted


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--dpi", type=int, default=300)
    parser.add_argument("--width", type=int, default=1600)
    parser.add_argument("--height", type=int, default=900)
    parser.add_argument("--reveal", type=float, default=0.32, help="fraction of page 1's height left visible above page 2 (title + authors)")
    parser.add_argument("--offset-x", type=float, default=0.10, dest="offset_x", help="horizontal shift of page 2, as a fraction of page 1's width")
    parser.add_argument("--page2-crop", type=float, default=0.52, dest="page2_crop", help="fraction of page 2's height to keep, cropped from the top (just past its first figure)")
    parser.add_argument("--fill", type=float, default=0.92, help="target fraction of canvas height the stack should fill")
    args = parser.parse_args()

    if not args.pdf.exists():
        sys.exit(f"No such file: {args.pdf}")

    with tempfile.TemporaryDirectory() as tmp_dir:
        page_files = rasterize_pages(args.pdf, 2, args.dpi, tmp_dir)
        if len(page_files) < 2:
            sys.exit("pdftoppm produced fewer than 2 pages")
        canvas = build_stack(page_files, args.width, args.height, args.reveal, args.offset_x, args.page2_crop, args.fill)
        canvas = fit_to_aspect(canvas, args.width, args.height)
        canvas = canvas.resize((args.width, args.height), Image.LANCZOS)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(args.output)
    print(f"Wrote {args.output} ({args.width}x{args.height})")


if __name__ == "__main__":
    main()
