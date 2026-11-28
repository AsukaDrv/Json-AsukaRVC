"""Aggregates every tab builder of the AsukaRVC WebUI.

app.py imports the tab builders from this module only:

    from tabs_main import inference_tab, downloader_tab, upload_tab

Each builder opens its own gr.Tab context and must be called inside a
gr.Blocks context.
"""

from ui.tabs.inference.inference_tab import inference_tab

__all__ = ['inference_tab']
