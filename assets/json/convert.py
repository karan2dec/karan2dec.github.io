import argparse
import json

import yaml


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser("YAML to JSON")
    parser.add_argument(
        "-i",
        "--path-file",
        help="Path to the YAML file",
        default="resume.yaml",
        required=False,
    )
    return parser.parse_args()


def main():
    args = parse_args()

    with open(args.path_file) as f:
        data = yaml.safe_load(f)

    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
