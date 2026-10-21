---
title: Coolita TVstream
emoji: 🐠
colorFrom: gray
colorTo: purple
sdk: static
pinned: false
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

## TVStream

A remote-first Stremio-compatible catalog/stream browser for Coolita TV. Open
`index.html` with a static server; the Hugging Face Space workflow deploys the
repository as-is.

### Deployment

- Ship `hls.min.js` beside `index.html`. It is vendored in this repo, so there
  is no CDN race at startup. If it is missing, direct MP4 and native HLS still
  work, but HLS.js playback is unavailable.
- Optional `config.json` beside `index.html` seeds addons after a cache wipe:
  `{"addons":["https://example.com/manifest.json"]}`.
- Add `?addon=MANIFEST_URL` to install a manifest on first load.
- HTTP addons/streams/subtitles are blocked when the Space is served over HTTPS.
  The operator whitelist (if any) must cover addon, stream, poster, subtitle and
  CDN hosts.

### Controls

Arrows move focus, OK/Enter activates, Back/Escape/Backspace leaves the current
view. Player controls auto-hide; Up/Down brings them back. Media play/pause,
rewind and fast-forward key codes are mapped when the browser reports them.
Back while a text field is focused closes the field before leaving the page.

### Diagnostics

Addons → Diagnostics reports engine version, native HLS, MSE codecs, Widevine/
PlayReady availability, screen size, CPU/memory hints and the last remote key
code. Use those probes to confirm behaviour on the actual Coolita build.

### Known limits

- No MPEG-DASH or DRM license playback yet; unsupported sources now fail over to
  the next source instead of stranding the player.
- Torrent/infoHash sources are listed but cannot play in a browser.
- Subtitle conversion supports SRT; ASS/SSA and non-UTF-8 files need conversion.
- CORS, mixed content, codec support and the exact remote key map are controlled
  by the TV firmware and the operator's network policy.
