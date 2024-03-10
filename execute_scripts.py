import subprocess
import os

def execute_scripts(scripts):
    """
    Execute a list of Python scripts using subprocess.

    Args:
    - scripts: List of script filenames to execute.

    Returns:
    - None
    """
    for script in scripts:
        try:
            # Print message indicating the script being executed
            print(f"\nExecuting {script} ...")
            
            # Print estimated execution time for 'Scrapper.py'
            if script == 'Scrapper.py':
                print("Estimated execution time: roughly 10 mins")
                
                # Check if data files exist, if yes, skip execution of Scrapper.py
                if 'user_node_edges.csv' in os.listdir() and 'user_nodes.csv' in os.listdir():
                    print("Skipping execution of Scrapper.py as data files already exist.")
                    continue
            
            # Execute the script using subprocess
            subprocess.run(['python3', script], check=True)
            
            # Print message indicating completion of script execution
            print(f"{script} execution complete.\n")
        except FileNotFoundError:
            print(f"Error: File '{script}' not found.")
        except subprocess.CalledProcessError:
            print(f"Error: Execution of '{script}' failed.")
        except Exception as e:
            print(f"Error: An unexpected error occurred: {e}")

if __name__ == "__main__":
    # List of scripts to execute
    scripts = ['Scrapper.py', 'Analyse.py', 'Visualise.py']

    # Execute scripts
    execute_scripts(scripts)
