from __future__ import annotations

import argparse
import logging
import os
from pathlib import Path

from dotenv import load_dotenv

from ..config import DEFAULT_ASSETS_FILE, DEFAULT_INTERVAL, DEFAULT_LOOKBACK, DEFAULT_POLL_SECONDS
from ..execution import create_client, validate_credentials
from ..models import RuntimeConfig
from ..resources import load_assets
from .runner import run_bot


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Binance multi-asset signal agent")
    parser.add_argument("--assets-file", type=Path, default=DEFAULT_ASSETS_FILE)
    parser.add_argument("--iterations", type=int, default=1, help="Set 0 to run indefinitely.")
    parser.add_argument("--poll-seconds", type=int, default=DEFAULT_POLL_SECONDS)
    parser.add_argument("--quote-asset", default="USDT")
    parser.add_argument("--lookback", default=DEFAULT_LOOKBACK)
    parser.add_argument("--interval", default=DEFAULT_INTERVAL)
    parser.add_argument("--live", action="store_true", help="Place live orders instead of dry-run logging.")
    parser.add_argument("--mainnet", action="store_true", help="Use Binance mainnet instead of testnet.")
    parser.add_argument("--log-level", default="INFO")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    logging.basicConfig(
        level=getattr(logging, str(args.log_level).upper(), logging.INFO),
        format="%(asctime)s | %(levelname)s | %(message)s",
    )

    load_dotenv()
    api_key = os.getenv("BINANCE_API_KEY", "")
    api_secret = os.getenv("BINANCE_API_SECRET", "")
    live_trading = bool(args.live)
    testnet = not bool(args.mainnet)

    validate_credentials(api_key, api_secret, live_trading=live_trading)

    config = RuntimeConfig(
        api_key=api_key,
        api_secret=api_secret,
        testnet=testnet,
        live_trading=live_trading,
        quote_asset=args.quote_asset,
        interval=args.interval,
        lookback=args.lookback,
        poll_seconds=args.poll_seconds,
        iterations=args.iterations,
    )
    client = create_client(config.api_key, config.api_secret, testnet=config.testnet)
    assets = load_assets(args.assets_file)
    run_bot(client, assets, config)


if __name__ == "__main__":
    main()