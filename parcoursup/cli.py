from __future__ import annotations
import argparse

from .config import Config
from .converter import convert_json_to_mysql


def run(config: Config) -> None:
	convert_json_to_mysql(
		config.json_file_path,
		config.mysql_file_path,
		config.database_name,
		config.table_name,
	)


def main() -> None:
	arg_parser = argparse.ArgumentParser(description="Converts JSON to MySQL.")
	arg_parser.add_argument(
		"-i",
		"--input",
		default="parcoursup.json",
		help="Path to the input `.json` file. Default: `parcoursup.json`.",
	)
	arg_parser.add_argument(
		"-o",
		"--output",
		default="parcoursup.sql",
		help="Path to the output `.sql` file. Default: `parcoursup.sql`.",
	)
	arg_parser.add_argument(
		"-d",
		"--database",
		default="parcoursup",
		help="Name of the MySQL database. Default: `parcoursup`.",
	)
	arg_parser.add_argument(
		"-t",
		"--table",
		default="parcoursup",
		help="Name of the MySQL table. Default: `parcoursup`.",
	)
	args = arg_parser.parse_args()
	config = Config(args)
	run(config)


if __name__ == "__main__":
	main()
