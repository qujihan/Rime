#!/usr/bin/env python3

import os
import sys
import time
import json
import argparse
import requests

color_reset = "\033[0m"
color_red = "\033[1;31m"
color_green = "\033[1;32m"
color_yellow = "\033[1;33m"
color_blue = "\033[1;34m"

try:
    from tqdm import tqdm

    tqdm_installed = True
except ImportError:
    tqdm_installed = False
    print(f"{color_red}tqdm not installed, will not show progress bar.{color_reset}")
    time.sleep(3)


def parse_config(config_path):
    dicts_map = {}
    try:
        with open(config_path) as file:
            data = json.load(file)
        for dict_dir_name, urls in data.items():
            dicts_map[dict_dir_name] = urls
    except json.JSONDecodeError:
        print(
            f"{color_red}Error: Failed to parse JSON file {config_path}. {color_reset}"
        )
        sys.exit(1)
    except Exception as e:
        print(f"{color_red}Error: {e}{color_reset}")
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
            print("\n")
            print(f"Download {color_blue} {basename} {color_reset}")
            print(f"From {color_green} {url} {color_reset}")
            print(f"Save to {color_yellow} {download_path} {color_reset}")
            download(url, download_path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--proxy", action="store_true", help="Use proxy to download.")
    if parser.parse_args().proxy:
        global download_proxy
        download_proxy = "https://mirror.ghproxy.com/"

    current_dir = os.path.abspath(os.path.dirname(__file__))
    json_path = os.path.join(current_dir, "dicts.json")
    dicts_map = parse_config(json_path)
    print(
        f"{color_red}If you encounter any network issues, try using the --proxy parameter.{color_reset}\n"
    )
    download_from_dicts_map(dicts_map)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nCancelled by user.")
        sys.exit(0)
