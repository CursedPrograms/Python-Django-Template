from django.shortcuts import render
from django.http import HttpResponse
import os
import subprocess

def run_script(request, script_number):
    current_script_dir = os.path.dirname(os.path.abspath(__file__))

    scripts = {
        "1": {"file_name": "script00.py"},
        "2": {"file_name": "script01.py"},
        "00": {"file_name": "install_dependencies.py"},
    }

    script_info = scripts.get(script_number)

    if not script_info:
        return HttpResponse("Invalid script number")

    script_file_name = script_info["file_name"]
    script_file_path = os.path.join(current_script_dir, script_file_name)

    if os.path.exists(script_file_path):
        try:
            subprocess.run(["python", script_file_path], capture_output=True, text=True)
            return HttpResponse("Script executed successfully")
        except Exception as e:
            return HttpResponse(f"An error occurred while running the script: {e}")
    else:
        return HttpResponse(f"Script file '{script_file_name}' does not exist.")

def show_run_script_form(request):
    scripts = {
        "1": {"name": "Run 'Script00'", "description": "This is Script00"},
        "2": {"name": "Run 'Script01'", "description": "This is Script01"},
        "00": {"name": "Run 'Install Dependencies'", "description": "Install dependencies"},
    }

    return render(request, 'run_script_form.html', {'scripts': scripts})
