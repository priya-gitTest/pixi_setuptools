import yaml
from importlib.resources import files
from pathlib import Path

# 1. Define the package path to the resource
PACKAGE_NAME = 'pixi_setuptools'
RESOURCE_NAME = 'employees.yaml'

def process_employee_data():
    """
    Reads the bundled employees.yaml file, processes the data,
    adds a new employee, and saves the updated list to the working directory.
    """
    # 2. Use importlib.resources.files to find the path of the packaged file
    # This is the correct way to access bundled files after pip install.
    try:
        # Resolve path to the packaged resource
        resource_path: Path = files(PACKAGE_NAME).joinpath(RESOURCE_NAME)
        
        # Read the packaged YAML file
        with resource_path.open('r') as file:
            employees_data = yaml.safe_load(file)

    except FileNotFoundError:
        print(f"Error: The packaged file {RESOURCE_NAME} was not found.")
        return

    print("--- Current Employee Data ---")
    for employee in employees_data['employees']:
        # Note: The employee data will be read-only from the package,
        # but we can modify the Python dictionary copy.
        print(f"Employee: {employee['name']}, Skills: {', '.join(employee['skills'])}")

    # 3. Modify the data (in memory)
    new_employee = {
        'name': 'Alice Green',
        'age': 30,
        'skills': ['Flask', 'SQLAlchemy']
    }
    employees_data['employees'].append(new_employee)

    # 4. Write the modified data to a NEW file in the current working directory
    output_filename = 'updated_employees_output.yaml'
    with open(output_filename, 'w') as file:
        yaml.dump(employees_data, file)
    
    print(f"\n--- Update Complete ---")
    print(f"Updated YAML saved to '{output_filename}' in the current working directory.")

if __name__ == '__main__':
    process_employee_data()