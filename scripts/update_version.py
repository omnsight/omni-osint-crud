import argparse
import json
import re
from pathlib import Path


def increment_version(version_str, release_type):
    """Increments a version string based on the release type."""
    try:
        major, minor, patch = map(int, version_str.split("."))
    except ValueError:
        print(f"Error: Invalid version format '{version_str}'. Expected 'major.minor.patch'.")
        return None

    if release_type == 1:
        major += 1
        minor = 0
        patch = 0
    elif release_type == 2:
        minor += 1
        patch = 0
    elif release_type == 3:
        patch += 1

    return f"{major}.{minor}.{patch}"


def update_pyproject_version(file_path, release_type):
    """Updates the version in a pyproject.toml file."""
    content = file_path.read_text()
    match = re.search(r'version = "(\d+\.\d+\.\d+)"', content)
    if not match:
        print(f"Error: Version not found in {file_path}")
        return

    current_version = match.group(1)
    new_version = increment_version(current_version, release_type)
    if new_version is None:
        return

    print(f"Updating {file_path}: {current_version} -> {new_version}")
    updated_content = content.replace(f'version = "{current_version}"', f'version = "{new_version}"')
    file_path.write_text(updated_content)


def update_package_json_version(file_path, release_type):
    """Updates the version in a package.json file."""
    with file_path.open("r") as f:
        data = json.load(f)

    current_version = data.get("version")
    if not current_version:
        print(f"Error: Version not found in {file_path}")
        return

    new_version = increment_version(current_version, release_type)
    if new_version is None:
        return

    print(f"Updating {file_path}: {current_version} -> {new_version}")
    data["version"] = new_version

    with file_path.open("w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")


def main():
    parser = argparse.ArgumentParser(description="Update project version in pyproject.toml and package.json.")
    parser.add_argument(
        "-r",
        "--release-type",
        type=int,
        choices=[1, 2, 3],
        required=True,
        help="Release type: 1 for major, 2 for minor, 3 for patch.",
    )
    args = parser.parse_args()

    project_root = Path(__file__).parent.parent
    pyproject_path = project_root / "pyproject.toml"
    package_json_path = project_root / "client" / "package.json"

    update_pyproject_version(pyproject_path, args.release_type)
    update_package_json_version(package_json_path, args.release_type)


if __name__ == "__main__":
    main()
