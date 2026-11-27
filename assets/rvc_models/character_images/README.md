# Character images

Drop a character image here to show it above the "Select Your Models"
dropdown in the Inference tab while that model is selected.

Naming rule: the file name must match the model (directory) name, e.g.
`ayaka-jp.png` for the `ayaka-jp` model.

Supported formats: `.png`, `.jpg`, `.jpeg`, `.webp`, `.gif`.

Alternatively, add an `"image"` field (URL or path) to the model entry in
`assets/rvc_models/public_models.json`:

```json
{
    "name": "ayaka-jp",
    "description": "...",
    "credit": "...",
    "url": "...",
    "tags": ["..."],
    "image": "https://example.com/ayaka-jp.png"
}
```

When both exist, the local file in this folder takes priority.
