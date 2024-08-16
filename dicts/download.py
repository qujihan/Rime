#!/usr/bin/env python3

import os
import sys
import json
import argparse
import requests

try:
    from tqdm import tqdm

    tqdm_installed = True
except ImportError:
    tqdm_installed = False
    print("tqdm not installed, will not show progress bar.")


def parse_config(config_path):
    dicts_map = {}
    try:
        with open(config_path) as file:
            data = json.load(file)
        for dict_dir_name, urls in data.items():
            dicts_map[dict_dir_name] = urls
    except json.JSONDecodeError:
        print(f"Error: Failed to parse JSON file {config_path}. ")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    return dicts_map


def download(url, path):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get("content-length", 0))
    block_size, downloaded_size = 1024, 0

    if tqdm_installed:
        progress_bar = tqdm(total=total_size, unit="iB", unit_scale=True)

    with open(path, "wb") as file:
        for data in response.iter_content(block_size):
            downloaded_size += len(data)
            file.write(data)
            if tqdm_installed:
                progress_bar.update(len(data))
            else:
                progress = downloaded_size / total_size * 100
                print(f"Download {os.path.basename(path)}: {progress:.2f}%")


download_proxy = ""


def download_from_dicts_map(dicts_map):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    for dicts_dir_name, urls in dicts_map.items():
        curr_font_dir = os.path.join(current_dir, dicts_dir_name)
        os.makedirs(curr_font_dir, exist_ok=True)
        for url in urls:
            url = f"{download_proxy}{url}"
            basename = os.path.basename(url)
            download_path = os.path.join(curr_font_dir, basename)
            print(f"Download {basename} from {url}")
            download(url, download_path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--proxy", action="store_true", help="Use proxy to download.")
    if parser.parse_args().proxy:
        global download_proxy
        download_proxy = "https://mirror.ghproxy.com/"
    dicts_map = parse_config("dicts.json")
    download_from_dicts_map(dicts_map)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nCancelled by user.")
        sys.exit(0)