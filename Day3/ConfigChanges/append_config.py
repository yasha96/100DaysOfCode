import re
import json

def append_to_config_file(config_file_path, new_section):
    # Read the existing Config file
    with open(config_file_path, 'r') as file:
        config_data = file.read()

    # Extract the 'resolves-conflict-dependencies' and 'targets' sections using regex
    resolves_conflict_pattern = r'resolves-conflict-dependencies\s*=\s*({[^}]+});'
    targets_pattern = r'targets\s*=\s*{[^}]+};'

    resolves_conflict_match = re.search(resolves_conflict_pattern, config_data)
    targets_match = re.search(targets_pattern, config_data)

    if not resolves_conflict_match or not targets_match:
        raise ValueError("Could not find 'resolves-conflict-dependencies' or 'targets' section in the Config file.")

    resolves_conflict_str = resolves_conflict_match.group(1)
    targets_str = targets_match.group(0)

    # Convert the existing resolves-conflict-dependencies section to a dictionary
    resolves_conflict_dict = json.loads(resolves_conflict_str)

    # Append the new_section to the resolves-conflict-dependencies dictionary
    new_section_version = list(new_section.keys())[0]
    resolves_conflict_dict[new_section_version] = new_section[new_section_version]

    # Convert the dictionary back to a string
    updated_resolves_conflict_str = json.dumps(resolves_conflict_dict, indent=4)

    # Append the updated_resolves_conflict_str and targets_str to the existing Config data
    updated_config_data = config_data.replace(resolves_conflict_str, updated_resolves_conflict_str + ";")
    updated_config_data = updated_config_data.replace(targets_str, "\n\n" + targets_str)

    # Write the updated Config back to the file
    with open(config_file_path, 'w') as file:
        file.write(updated_config_data)

# Example usage
config_file_path = '/Users/mrajyash/100DaysOfCode/Day3/ConfigChanges/append_config.py'
new_section = {
    "2.0": {
        "Testool": "3.x",
        "MySelfTest": "30.x"
    }
}

append_to_config_file(config_file_path, new_section)
