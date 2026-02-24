from __future__ import annotations
import argparse


class Config:
	def __init__(self, args: argparse.Namespace):
		self.json_file_path: str = args.input
		self.mysql_file_path: str = args.output
		self.database_name: str = args.database
		self.table_name: str = args.table
