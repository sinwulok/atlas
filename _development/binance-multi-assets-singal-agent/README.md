# binance-multi-assets-singal-agent

Binance multi-asset signal agent prototype extracted from a research notebook into a small Python project with a layered `src/` application layout.

## Overview

This project now has two implementation surfaces:

- Application code under `src/`, split by responsibility into `app/`, `config/`, `data/`, `execution/`, `signals/`, and `market/`.
- `binance_testnet_crpyto_v4.ipynb`: the original exploratory notebook retained for reference.

The strategy matches the notebook prototype: fetch recent 1-minute klines, calculate MACD plus 30-minute percentage change, then produce buy or sell signals per asset. The command-line runner defaults to dry-run mode so the extracted code can be exercised without placing orders.

## Structure

```text
binance-multi-assets-singal-agent/
├── run.py                   # Thin CLI wrapper
├── config/                  # Optional config files / future YAML defaults
├── public/                  # Static charts and exported assets
├── src/
│   ├── app/
│   │   ├── main.py          # Main CLI implementation
│   │   └── runner.py        # Trading loop orchestration
│   ├── config/
│   │   └── defaults.py      # Default runtime settings
│   ├── data/
│   │   ├── asset_loader.py  # Asset-state assembly
│   │   ├── asset_sources.py # CSV/TXT asset-source readers
│   │   └── default_assets.py # Built-in fallback asset basket
│   ├── execution/
│   │   ├── binance_client.py # Binance client factory and credential checks
│   │   └── order_service.py # Live/dry-run order submission
│   ├── models.py            # Runtime and strategy data models
│   ├── types.py             # Binance client protocol typing
│   ├── signals/
│   │   ├── indicators.py    # MACD and indicator calculation
│   │   └── macd_strategy.py # Latest-signal evaluation
│   └── market/
│       ├── constants.py     # Raw kline schema
│       ├── klines.py        # Binance kline fetching
│       └── transformers.py  # DataFrame normalization
├── binance_testnet_crpyto_v4.ipynb
├── requirements.txt
└── setup.py
```

## How To Run

1. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

2. Create a `.env` file if you want authenticated requests or live orders:

   ```env
   BINANCE_API_KEY=your_api_key
   BINANCE_API_SECRET=your_api_secret
   ```

3. Run one dry-run iteration against testnet data:

   ```sh
   python run.py --iterations 1
   ```

4. Or run the application module directly:

   ```sh
   python -m src.app.main --iterations 1
   ```

5. Only enable order placement when you explicitly want it:

   ```sh
   python -m src.app.main --live --iterations 0
   ```

## Asset Inputs

If `src/data/assets.csv` or `src/data/assets.txt` is empty, the runner falls back to the notebook's default basket:

- BTC
- LTC
- TRX
- ETH
- BNB
- XRP

CSV supports `asset`, `order_size`, and `is_long` columns. TXT supports lines like:

```text
BTC,0.0025,false
ETH,0.03,true
```

## Architecture Notes

- `src/config/` holds runtime defaults.
- `src/data/` handles asset definitions and input parsing, plus the default asset lists.
- `src/execution/` isolates exchange client creation and order submission.
- `src/signals/` holds indicator calculation and signal evaluation.
- `src/app/` coordinates the CLI and trading loop.
- `public/` stores exported charts and notebook-generated static assets.
- Typical public-safe files include `favicon`, `robots.txt`, `site.webmanifest`, preview images, downloadable example files, and other intentionally public static assets.

## Notes

- Dry-run is the default. Without `--live`, the runner logs intended orders instead of submitting them.
- `numpy<2` is pinned because the notebook workflow already showed compatibility issues around the indicator stack.
- The notebook remains useful for charts and exploratory work, but the extracted project structure is the intended execution path.
- `setup.py` is for packaging and installation metadata, not for launching the app.
- `run.py` is the conventional lightweight entrypoint if you prefer a repo-local launcher.

## Related Links

- [Binance API (python-binance)](https://github.com/sammchardy/python-binance)
- [Project Catalog](../../catalog/index.md)
- [Repository Root](../../README.md)
