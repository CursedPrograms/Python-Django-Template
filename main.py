import os
import subprocess

def main():
    print("Python Project")

    scripts = {
        "1": {
            "name": "Run 'Script00'",
            "description": "This is Script01",
            "file_name": "script00.py"
        },
        "2": {
            "name": "Run 'Script01",
            "description": "This is Script01",
            "file_name": "script01.py"
        },
        "00": {
            "name": "Run 'Install Dependencies'",
            "description": "Install dependencies",
            "file_name": "install_dependencies.py"
        },
    }

    current_script_dir = os.path.dirname(os.path.abspath(__file__))

    while True:
        print("\nAvailable Scripts:")
        for key, script_info in scripts.items():
            print(f"{key}: {script_info['name']} - {script_info['description']}")
        
        user_choice = input("Enter the number of the script you want to run (or 'q' to quit): ").strip()
        
        if user_choice == 'q':
            break
        
        if user_choice in scripts:
            selected_script = scripts[user_choice]
            script_file_name = selected_script["file_name"]
            script_file_path = os.path.join(current_script_dir, script_file_name)
            
            if os.path.exists(script_file_path):
                try:
                    subprocess.run(["python", script_file_path])
                except Exception as e:
                    print(f"An error occurred while running the script: {e}")
            else:
                print(f"Script file '{script_file_name}' does not exist.")
        else:
            print("Invalid choice. Please select a valid script number.")

if __name__ == "__main__":
    main()
