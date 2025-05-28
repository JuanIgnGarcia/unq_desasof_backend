import os
import pytest
import ast


# Function to check for circular imports
def test_check_circular_imports():
    files = []
    # Walk through the project directory to analyze files
    for root, dirs, files_list in os.walk("src"):
        for file in files_list:
            if file.endswith(".py") and file != "test_*.py":
                files.append(os.path.join(root, file))

    # Analyze the files to look for circular imports
    for file in files:
        with open(file, "r") as f:
            tree = ast.parse(f.read())
            for node in ast.walk(tree):
                if isinstance(node, ast.ImportFrom):
                    module = node.module
                    if "controller" in module and "service" in module:
                        pytest.fail(f"Importación cíclica detectada: {file}")


# Function to check the dependencies of modules
def test_check_dependencies():
    controllers_dir = "src/controllers"
    services_dir = "src/service"

    # Check that controllers do not import from the 'controllers' folder
    for root, dirs, files_list in os.walk(controllers_dir):
        for file in files_list:
            if file.endswith(".py"):
                with open(os.path.join(root, file), "r") as f:
                    content = f.read()
                    assert "from src.service" in content, f"{file} no importa desde 'service' como debería"

    # Check that services do not import from 'controllers'
    for root, dirs, files_list in os.walk(services_dir):
        for file in files_list:
            if file.endswith(".py"):
                with open(os.path.join(root, file), "r") as f:
                    content = f.read()
                    assert "from src.controller" not in content, f"{file} no debería importar desde 'controller'"






