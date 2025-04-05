import json
import toml

def convert_json_to_toml(json_file, toml_file):
    """
    Convert a JSON file to a TOML file.
    """
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    with open(toml_file, "w", encoding="utf-8") as f:
        toml.dump(data, f)

    print(f"Converted JSON to TOML: {toml_file}")


def read_toml_as_elements(toml_file):
    """
    Read a TOML file and return it as a dictionary.
    """
    with open(toml_file, "r", encoding="utf-8") as f:
        data = toml.load(f)

    return data


# Example usage
if __name__ == "__main__":
    # File paths
    json_file = "data/graph_data.json"
    toml_file = "data/graph_data.toml"

    # Convert JSON to TOML
    convert_json_to_toml(json_file, toml_file)

    # Read TOML back as elements
    elements = read_toml_as_elements(toml_file)

    # Print the loaded elements
    print("Nodes:")
    for node in elements["nodes"]:
        print(node)

    print("\nEdges:")
    for edge in elements["edges"]:
        print(edge)
