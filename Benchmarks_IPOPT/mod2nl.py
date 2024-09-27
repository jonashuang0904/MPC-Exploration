import os
import subprocess

# Set the path to the directory containing the .mod files
mod_dir = "D:\AMPL_new\IPOPT\model_file\model file"
os.chdir(mod_dir)

# AMPL executable path
ampl_path = "D:/AMPL_new/ampl.exe"
print(os.listdir(mod_dir))
# Go through all the .mod files in the directory
for filename in os.listdir(mod_dir):
    print(filename)
    if filename.endswith(".mod"):
        # Extract the model name
        model_name = os.path.splitext(filename)[0]   
        
        ampl_command = f"""
        reset;
        model {filename};
        write g_{model_name}.nl;
        """
        # Using subprocess to run AMPL commands
        try:
            result = subprocess.run([ampl_path], input=ampl_command, text=True, capture_output=True)
            if result.returncode == 0:
                print(f"NL file generated successfully for {filename} to {model_name}.nl")
            else:
                print(f"Error generating NL file for {filename}")
                print(result.stdout)
                print(result.stderr)
        except Exception as e:        
            print(f"Error NL file for {filename}")

print("\nDiagnostic process completed.")