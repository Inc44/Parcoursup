import json


def flatten_dictionary(dictionary, key_prefix=""):
	flattened_dictionary = {}
	for key, value in dictionary.items():
		new_key = f"{key_prefix}{key}"
		if isinstance(value, dict):
			flattened_dictionary.update(flatten_dictionary(value, f"{new_key}_"))
		else:
			flattened_dictionary[new_key] = value
	return flattened_dictionary


def get_optimal_string_type(minimum_length, maximum_length):
	if minimum_length == maximum_length:
		return f"CHAR({maximum_length})"
	"""
	for exponent in range(1, 9):
		optimal_length = (2**exponent) - 1
	"""
	for exponent in range(1, 8):
		optimal_length = 2**exponent
		if maximum_length <= optimal_length:
			return f"VARCHAR({optimal_length})"
	if maximum_length <= 255:
		return f"VARCHAR({255})"
	return "TEXT"


def get_optimal_integer_type(minimum_value, maximum_value):
	if minimum_value >= -128 and maximum_value <= 127:
		return "TINYINT"  # 8 bits
	if minimum_value >= -32768 and maximum_value <= 32767:
		return "SMALLINT"  # 16 bits
	if minimum_value >= -2147483648 and maximum_value <= 2147483647:
		return "INT"  # 32 bits
	return "BIGINT"  # 64 bits


def determine_mysql_type(values):
	valid_values = [value for value in values if value is not None]
	if not valid_values:
		return "NULL"
	data_types = {type(value) for value in valid_values}
	if str in data_types:
		string_lengths = [len(str(value)) for value in valid_values]
		return get_optimal_string_type(min(string_lengths), max(string_lengths))
	if float in data_types:
		return "FLOAT"
	if int in data_types:
		integer_values = [int(value) for value in valid_values]
		return get_optimal_integer_type(min(integer_values), max(integer_values))
	return "ERROR"


def create_insert_statement(table_name, keys, row):
	formatted_values = []
	for key in keys:
		value = row.get(key)
		if value is None:
			formatted_values.append("NULL")
		elif isinstance(value, str):
			escaped_string = value.replace("'", "''")
			formatted_values.append(f"'{escaped_string}'")
		else:
			formatted_values.append(str(value))
	values_string = ", ".join(formatted_values)
	return f"INSERT INTO {table_name} VALUES ({values_string});\n"


def convert_json_to_mysql(json_file_path, mysql_file_path, table_name):
	with open(json_file_path, "r", encoding="utf-8") as file:
		data = json.load(file)
	flattened_data = [flatten_dictionary(row) for row in data]
	keys = []
	for row in flattened_data:
		for key in row.keys():
			if key not in keys:
				keys.append(key)
	valid_keys = []
	column_definitions = []
	for key in keys:
		column_values = [row.get(key) for row in flattened_data]
		mysql_type = determine_mysql_type(column_values)
		if mysql_type == "ERROR":
			raise ValueError(f"Error determining MySQL type for column '{key}'")
		if mysql_type != "NULL":
			valid_keys.append(key)
			column_definitions.append(f"\t{key} {mysql_type}")
	with open(mysql_file_path, "w", encoding="utf-8") as file:
		file.write(f"DROP TABLE IF EXISTS {table_name};\n")
		file.write(f"CREATE TABLE IF NOT EXISTS {table_name} (\n")
		file.write(",\n".join(column_definitions))
		file.write("\n);\n")
		for row in flattened_data:
			insert_statement = create_insert_statement(table_name, valid_keys, row)
			file.write(insert_statement)
		file.write("COMMIT;")


if __name__ == "__main__":
	convert_json_to_mysql("parcoursup.json", "parcoursup.sql", "parcoursup")
