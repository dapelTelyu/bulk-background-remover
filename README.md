# 🖼️ Automatic Background Remover

A Python script to automatically remove backgrounds from images using [rembg](https://github.com/danielgatis/rembg). Supports `.jpg`, `.jpeg`, `.png`, and `.heic` formats.

---

## 🚀 Features

- Automatically removes image backgrounds
- Supports `.HEIC` files
- Saves the result in the `output/` folder
- Displays progress and final summary
- Automatically creates the output folder if it doesn't exist

---

## 📦 Libraries Used

- [rembg](https://github.com/danielgatis/rembg) - Background remover (MIT)
- [Pillow](https://python-pillow.org/) - Image processing (HPND)
- [pyheif](https://github.com/carsales/pyheif) - Read `.heic` files (MIT)

---

## 📥 Install Dependencies

```bash
pip install rembg pillow pyheif
```
## How to Run the code
```bash
git clone https://github.com/dapelTelyu/bulk-background-remover.git
cd repo-name
```
```bash
python removebg.py
```
