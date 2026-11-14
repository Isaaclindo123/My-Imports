"""
# Isa Utilities (or isau)

The Isa Utilities is a import for the python that does you create codes in any language that you want (almost languages):

The languages are:

1. Batch
2. VBS (Visual Basic Script)
3. SQL
4. C (Using MYSYS2 compiler)
5. C++ (Using MYSYS2 compiler)
6. C# (Uning dotnet)
7. Java Script (Node JS)
8. React (Creates the project, you edit the code in the python folder)
9. CSS (to integrate in HTML Script)
10. Html
11. Type Script
12. Ruby
13. Rust
14. PHP (Run in PHP CLI)
15. Lua (raw)
16. R
17. Go
18. Nim
19. Java
20. Assembly (NASM Syntax)

All languages (or part of they) is runned with a file in the Temp folder with the tempfile import

And there was a 2 functions that I had forgotten:
- Terminal Title
- Color Initialize

# That is it!!!
To know more, visit the wiki, and I explain each function
"""

# IsaUtilities (or isau)
# Lazy Imports (modules)
__lazy_modules__ = ["sys", "colorama", "shutil", "os", "subprocess" "tempfile", "webbrownser", "pandas", "sqlalchemy", "pyodbc", "re", "urlib.parse"]

# Imports
import sys
from colorama import init, Fore, Style
import shutil
import os
import subprocess
import tempfile
import webbrowser
import pandas as pd
import sqlalchemy as sa
import pyodbc
import re
import urllib.parse

# To don't create a __cache__ folder
sys.dont_write_bytecode = True

# Author, me :)
__author__ = "Isaac Martins Brito Sousa (IsaacLindo123 GitHub) <isaac.legalzim10@gmail.com>"

# All functions in IsaUtilities (or isau)
__all__ = ["colorinicialize", "terminaltitle", "sqlsender", "sqlconnectunencrypted", "sqlconnectencrypted", "sqlquery", "cmd", "vbs", "c", "cpp", "cs", "nodejs", "react", "css", "html", "ts", "ruby", "rust", "php", "lua", "r", "go", "nim", "java", "asm"]


# Hello
print("Hello form Two Points Community!!! IsaUtilities [1.0] (FIX IN PYPI 1) imported (obs: no run the colorinitialize() & react(appname, appcode) in module (F5))")

# Global variables
_cfgconnect = None

# Defines codes
def colorinicialize():
    try:
        init(autoreset=True)
        sys.stdout.reconfigure(line_buffering=True)
        print(f"{Fore.GREEN}Colors inicialized...")

    except AttributeError:
        print("TBMRCL [Cod 002] Don't run this function in module (F5)")
    

def terminaltitle(title):
    if not terminaltitle:
        print("TBMRCL [Cod 001] Not defined title")
        return
    sys.stdout.write(f"\x1b]2;{title}\x07")
    sys.stdout.flush()

def sqlsender(localdir, filetable):
    try:
        shutil.copy(localdir, filetable)
        
    except Exception as e:
        print(f"TBMRCL [Cod 003] Error in archive copy with details: {e}")

def sqlconnectencrypted(drv, srv, db, tc, tsc):
    global _cfgconnect
    raw_odbc = (
        f"DRIVER={{{drv}}};"
        f"SERVER={srv};"
        f"DATABASE={db};"
        f"Trusted_Connection={tc};"
        f"Encrypt=yes;"
        f"TrustServerCertificate={tsc}"
    )
    params = urllib.parse.quote_plus(raw_odbc)
    _cfgconnect = f"mssql+pyodbc:///?odbc_connect={params}"
    return _cfgconnect


def sqlconnectunencrypted(drv, srv, db, tc):
    global _cfgconnect
    raw_odbc = (
        f"DRIVER={{{drv}}};"
        f"SERVER={srv};"
        f"DATABASE={db};"
        f"Trusted_Connection={tc};"
        f"Encrypt=no;"
        f"TrustServerCertificate=yes"
    )
    params = urllib.parse.quote_plus(raw_odbc)
    _cfgconnect = f"mssql+pyodbc:///?odbc_connect={params}"
    return _cfgconnect

def sqlquery(qry):
    global _cfgconnect
    if _cfgconnect == None:
        print("TBMRCL [Cod 004] Error in query: You don't defined the sql connect (variable _cfgconnect)")
        return
    try:
        engine = sa.create_engine(_cfgconnect)
        with engine.connect() as conexao:
            df = pd.read_sql(qry, conexao)
        return df
    
    except Exception as e:
        print(f"TBMRCL [Cod 005] Error in query: {e}")

def cmd(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding="cp850")
    print(result.stdout)

    if result.stderr:
        print(f"TBMRCL [Cod: 010] Error in results \n{result.stderr}")


def vbs(vbscommand):
    vbscode = f"""{vbscommand}"""

    with tempfile.NamedTemporaryFile(delete=False, suffix=".vbs", mode="w", encoding="latin1") as f:
        f.write(vbscode)
        vbsdir = f.name

    try:
        subprocess.run(["wscript.exe", vbsdir], check=True)

    except subprocess.CalledProcessError as e:
        print("TBMRCL [Cod 006] Internal Error in VBscript: {e}")

    except FileNotFoundError:
        so = sys.platform
        print(f"TBMRCL [Cod 007] The 'wscript.exe' is not found in your system, (perhaps your system is a Linux, MacOs or other) (SYSTEM:{so})")

    except Exception as e:
        print(f"TBMRCL [Cod UNKNW] Unexcepted error: {e}")
    
    finally:
        if os.path.exists(vbsdir):
            os.remove(vbsdir)
            
def c(ccode):
    ccode_str = f"{ccode}"
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".c", mode="w", encoding="utf-8") as f_c:
        f_c.write(ccode_str)
        c_dir = f_c.name
        
    exe_dir = c_dir.replace(".c", ".exe")

    try:
        compile_result = subprocess.run(["gcc", c_dir, "-o", exe_dir], capture_output=True, text=True)
        
        if compile_result.returncode != 0:
            print("TBMRCL [Cod 045] Compilation Error in C:")
            print(compile_result.stderr)
            return

        run_result = subprocess.run([exe_dir], capture_output=True, text=True)
        
        if run_result.returncode != 0:
            print("TBMRCL [Cod 046] Execution Error in C:")
            print(run_result.stderr)
        else:
            print(run_result.stdout)

    except FileNotFoundError:
        print("TBMRCL [Cod 047] GCC compiler not found. Make sure gcc is installed and added to your PATH.")
        
    except Exception as e:
        print(f"TBMRCL [Cod UNKNW] Unexpected error: {e}")
        
    finally:
        if os.path.exists(c_dir):
            os.remove(c_dir)
        if os.path.exists(exe_dir):
            os.remove(exe_dir)
            
def cpp(cppcode):
    cppcd = f"""{cppcode}"""

    with tempfile.NamedTemporaryFile(delete=False, suffix=".cpp", mode="w", encoding="utf8") as f_cpp:
        f_cpp.write(cppcd)
        cppdir = f_cpp.name

    exedir = cppdir.replace(".cpp", ".exe")

    try:
        compprocess = subprocess.run(
            ["g++", cppdir, "-o", exedir],
            capture_output=True,
            text=True
        )

        if compprocess.returncode != 0:
            print("TBMRCL [Cod 008] Compilation Error in C++:")
            print(compprocess.stderr)

        else:
            result = subprocess.run([exedir], capture_output=True, text=True, check=True)
            print(result.stdout)

    except FileNotFoundError:
        print("TBMRCL [Cod 009] Compilator 'g++' not found, try to install here --> https://www.msys2.org/")

    except Exception as e:
        print(f"[Cod UNKNW] Unexcepted error: {e}")

    finally:
        try:
            if os.path.exists(cppdir):
                os.remove(cppdir)
        except Exception:
            pass

        try:
            if os.path.exists(exedir):
                os.remove(exedir)
        except PermissionError:
            pass

def cs(cscode):
    with tempfile.TemporaryDirectory() as temp_dir:
        csproj_path = os.path.join(temp_dir, "App.csproj")
        program_path = os.path.join(temp_dir, "Program.cs")

        csproj_content = """<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>
</Project>
"""
        with open(csproj_path, "w", encoding="utf-8") as f:
            f.write(csproj_content)
            
        with open(program_path, "w", encoding="utf-8") as f:
            f.write(cscode)

        try:
            run_result = subprocess.run(
                ["dotnet", "run", "--project", csproj_path],
                capture_output=True,
                text=True
            )

            if run_result.returncode != 0:
                print("TBMRCL [Cod 048] Execution Error in C# (.NET):")
                print(run_result.stderr)
                print(run_result.stdout)
            else:
                print(run_result.stdout.strip())

        except FileNotFoundError:
            print("TBMRCL [Cod 049] 'dotnet' command not found. Make sure the .NET SDK is installed and added to your PATH.")
        except Exception as e:
            print(f"TBMRCL [Cod UNKNW] Unexpected error in C# execution: {e}")

        finally:
            if os.path.exists(csproj_path):
                os.remove(csproj_path)

            if os.path.exists(program_path):
                os.remove(program_path)
                
def nodejs(javascriptcode):
    jscd = f"""{javascriptcode}"""

    with tempfile.NamedTemporaryFile(delete=False, suffix=".js", mode="w", encoding="utf-8") as f_js:
        f_js.write(jscd)
        jsdir = f_js.name

    try:
        result = subprocess.run(["node", jsdir], capture_output=True, text=True)

        if result.returncode != 0:
            print("TBMRCL [Cod 013] Execution Error in JavaScript (node.js)")

        else:
            print(result.stdout)


    except FileNotFoundError:
        print("TBMRCL [Cod 014] 'Node.js' not found, install in this link: https://nodejs.org/en")

    except Exception as e:
        print(f"TBMRCL [Cod UNKNW] Unexcepted error: {e}")

    finally:
        if os.path.exists(jsdir):
            os.remove(jsdir)
            
def react(app_name="myreactproject"):
    if app_name is None:
        print("TBMRCL [Cod 016] Define a name to app")
        return
        
    try:
        subprocess.run(["npm.cmd", "--version"], capture_output=True, text=True, check=True)

        prjdir = os.path.join(os.getcwd(), app_name)
        srcdir = os.path.join(prjdir, "src")

        if not os.path.exists(prjdir):
            
            subprocess.run(
                f"npm.cmd create vite@latest {app_name} -- --template react",
                shell=True,
                check=True
            )
            
            if os.path.exists(prjdir):
                subprocess.run(["npm.cmd", "install"], cwd=prjdir, shell=True, check=True)

            else:
                print("TBMRCL [Cod 017] Failed to generate project folder structure...")
                return
        else:
            print(f"Project '{app_name}' is existent, opening the dev server")

        subprocess.run(f'start cmd /k "cd /d {prjdir} && npm run dev"', shell=True)

    except FileNotFoundError:
        print("TBMRCL [Cod 018] Error in 'npm.cmd': Not Found")
        print("To run React codes, install Node.js here --> https://nodejs.org/en")
              
    except subprocess.CalledProcessError as e:
        print(f"TBMRCL [Cod 019] Error during React setup: {e}")

    except Exception as e:
        print(f"TBMRCL [Cod UNKNW] Unexcepted Error: {e}")

def css(csscode):
    if csscode is None:
        print("TBMRCL [Cod 020] Define a css code")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".css", mode="w", encoding="utf8") as f_css:
        f_css.write(csscode)
        cssdir = f_css.name

    return cssdir

def html(htmlcode, stylesheet=None):

    if stylesheet and os.path.exists(stylesheet):
        tag_css = f'href="file:///{stylesheet}"'
        htmlcode = htmlcode.replace("{stylesheet}", tag_css)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".html", mode="w", encoding="utf-8") as f_html:
        f_html.write(htmlcode)
        htmldir = f_html.name

    try:
        webbrowser.open(f"file://{htmldir}")

    except Exception as e:
        print("TBMRCL [Code 021] Error to open brownser with HTML, check if you have internet or if you have a brownser: {e}")

def ts(tscode):
    tscd = f"{tscode}"

    with tempfile.NamedTemporaryFile(delete=False, suffix=".ts", mode="w", encoding="utf-8") as f_ts:
        f_ts.write(tscd)
        tsdir = f_ts.name

    try:
        command = f'npx --yes tsx "{tsdir}"'
        result = subprocess.run(command, capture_output=True, text=True, shell=True)

        if result.returncode != 0:
            print("TBMRCL [Cod 022] Execution Error in TypeScript:")
            print(result.stderr)

        else:
            print(result.stdout)

    except FileNotFoundError:
        print("TBMRCL [Cod 023] Node.js or npx not found, to run, install node.js here --> https://nodejs.org/en")

    except Exception as e:
        print(f"TBMRCL [Cod UNKNW] Unexcepted Error: {e}")

    finally:
        if os.path.exists(tsdir):
            os.remove(tsdir)

def ruby(rubycode):
    rbcd = f"{rubycode}"

    with tempfile.NamedTemporaryFile(delete=False, suffix=".rb", mode="w", encoding="utf-8") as f_rb:
        f_rb.write(rbcd)
        rbdir = f_rb.name

    try:
        result = subprocess.run(["ruby", rbdir], capture_output=True, text=True)

        if result.returncode != 0:
            print("TBMRCL [Cod 024] Excecution Error in Ruby:")
            print(result.stderr)

        else:
            print(result.stdout)

    except FileNotFoundError:
        print("TBMRCL [Code 025] Ruby interpreter not found, to run, install here --> https://ruby-lang.org/en")

    except Exception as e:
        print(f"TBMRCL [Code UNKNW] Unexcepted Error: {e}")

    finally:
        if os.path.exists(rbdir):
            os.remove(rbdir)

def rust(rustcode):
    rustcd = f"{rustcode}"

    with tempfile.NamedTemporaryFile(delete=False, suffix=".rs", mode="w", encoding="utf-8") as f_rs:
        f_rs.write(rustcd)
        rustdir = f_rs.name

    exedir = rustdir.replace(".rs", ".exe")

    try:

        compprocess = subprocess.run(
            ["rustc", rustdir, "-o", exedir],
            capture_output=True,
            text=True
        )

        if compprocess.returncode != 0:
            print("TBMRCL [Cod 026] Compilation Error in Rust:")
            print(compprocess.stderr)

        else:
            result = subprocess.run([exedir], capture_output=True, text=True, check=True)
            print(result.stdout)

    except FileNotFoundError:
        print("TBMRCL [Cod 027] Rust compile 'rustc' not found, try to download here: https://rust-lang.org")

    except Exception as e:
        print(f"TBMRCL [Cod UNKNW] Unexcepted Error: {e}")

    finally:
        if os.path.exists(rustdir):
            os.remove(rustdir)

        if os.path.exists(exedir):
            try:
                os.remove(exedir)

            except Exception:
                pass

def php(phpcode):
    phpcd = phpcode.strip()
    if not phpcd.startswith("<?php"):
        phpcd = f"<?php\n{phpcd}"

    with tempfile.NamedTemporaryFile(delete=False, suffix=".php", mode="w", encoding="utf-8") as f_php:
        f_php.write(phpcd)
        phpdir = f_php.name

    try:
        result = subprocess.run(["php", phpdir], capture_output=True, text=True)

        if result.returncode != 0:
            print("TBMRCL [Cod 028] Execution Error in PHP:")
            print(result.stderr)

        else:
            print(result.stdout)

    except FileNotFoundError:
        print("TBMRCL [Cod 029] PHP CLI interpreter not found, try to install php cli and add in your PATH --> https://php.net")

    except Exception as e:
        print(f"TBMRCL [Cod UNKNW] Unexcepted Error: {e}")

    finally:
        if os.path.exists(phpdir):
            os.remove(phpdir)

def lua(luacode):
    luacd = f"{luacode}"

    with tempfile.NamedTemporaryFile(delete=False, suffix=".lua", mode="w", encoding="utf-8") as f_lua:
        f_lua.write(luacd)
        luadir = f_lua.name

    try:
        result = subprocess.run(["lua", luadir], capture_output=True, text=True)
        
        if result.returncode != 0:
            print("TBMRCL [Cod 030] Execution Error in Lua:")
            print(result.stderr)
        else:
            print(result.stdout)

    except FileNotFoundError:
        print("TBMRCL [Cod 031] Lua interpreter not found, try to install and add in your PATH here --> https://lua.org")
        
    except Exception as e:
        print(f"TBMRCL [Cod UNKNW] Unexcepted error: {e}")
        
    finally:
        if os.path.exists(luadir):
            os.remove(luadir)

def r(rcode):
    rcd = f"{rcode}"

    with tempfile.NamedTemporaryFile(delete=False, suffix=".R", mode="w", encoding="utf-8") as f_r:
        f_r.write(rcd)
        rdir = f_r.name

    rscript_exec = shutil.which("Rscript")
    
    if not rscript_exec and sys.platform == "win32":
        r_base_dir = r"C:\Program Files\R"
        if os.path.exists(r_base_dir):
            subdirs = os.listdir(r_base_dir)
            for sub in subdirs:
                potential_path = os.path.join(r_base_dir, sub, "bin", "x64", "Rscript.exe")
                if os.path.exists(potential_path):
                    rscript_exec = potential_path
                    break

    if not rscript_exec:
        rscript_exec = "Rscript"

    try:
        result = subprocess.run([rscript_exec, rdir], capture_output=True, text=True)

        if result.returncode != 0:
            print("TBMRCL [Cod 032] Execution Error in R:")
            print(result.stderr)
        else:
            print(result.stdout)

    except FileNotFoundError:
        print("TBMRCL [Cod 033] R interpreter / 'Rscript' not found, install R and add to your PATH --> https://www.r-project.org/")
        
    except Exception as e:
        print(f"TBMRCL [Cod UNKNW] Unexcepted error: {e}")
        
    finally:
        if os.path.exists(rdir):
            os.remove(rdir)

def go(gocode):
    gocd = f"{gocode}"

    with tempfile.NamedTemporaryFile(delete=False, suffix=".go", mode="w", encoding="utf-8") as f_go:
        f_go.write(gocd)
        godir = f_go.name

    go_exec = shutil.which("go")
    
    if not go_exec and sys.platform == "win32":
        default_go_path = r"C:\Program Files\Go\bin\go.exe"
        if os.path.exists(default_go_path):
            go_exec = default_go_path

    if not go_exec:
        go_exec = "go"

    try:
        result = subprocess.run([go_exec, "run", godir], capture_output=True, text=True)

        if result.returncode != 0:
            print("TBMRCL [Cod 034] Execution Error in Go:")
            print(result.stderr)

        else:
            print(result.stdout)

    except FileNotFoundError:
        print("TBMRCL [Cod 035] Go compiler not found, try to install here --> https://golang.org/dl/")

    except Exception as e:
        print(f"TBMRCL [Cod UNKNW] Unexcepted Error: {e}")

    finally:
        if os.path.exists(godir):
            os.remove(godir)

def nim(nimcode):
    nimcd = f"{nimcode}"

    with tempfile.NamedTemporaryFile(delete=False, suffix=".nim", mode="w", encoding="utf-8") as f_nim:
        f_nim.write(nimcd)
        nimdir = f_nim.name

    exedir = nimdir.replace(".nim", ".exe" if sys.platform == "win32" else "")

    try:
        comp_result = subprocess.run(["nim", "c", "-d:release", "--verbosity:0", "--hints:off", nimdir], capture_output=True, text=True)

        if comp_result.returncode != 0:
            print("TBMRCL [Cod 053] Compilation Error in Nim:")
            print(comp_result.stderr)
        else:
            run_result = subprocess.run([exedir], capture_output=True, text=True)
            print(run_result.stdout)
            if run_result.stderr:
                print(run_result.stderr)

    except FileNotFoundError:
        print("TBMRCL [Cod 054] Nim compiler not found, install Nim and add to your PATH --> https://nim-lang.org/")

    except Exception as e:
        print(f"TBMRCL [Cod UNKNW] Unexpected Error: {e}")

    finally:
        for path in [nimdir, exedir]:
            if path and os.path.exists(path):
                try:
                    os.remove(path)
                except:
                    pass

def java(javacode):
    if "public class" not in javacode:
        javacode = f"""
public class Main {{
    public static void main(String[] args) {{
        {javacode}
    }}
}}
"""

    match_var = re.search(r"public\s+class\s+(\w+)", javacode)
    class_name = match_var.group(1) if match_var else "Main"

    tmp_dir = tempfile.mkdtemp()
    javadir = os.path.join(tmp_dir, f"{class_name}.java")

    try:
        with open(javadir, "w", encoding="utf-8") as f_java:
            f_java.write(javacode)

        compprocess = subprocess.run(["javac", "-d", tmp_dir, javadir], capture_output=True, text=True)

        if compprocess.returncode != 0:
            print("TBMRCL [Cod 038] Compilation Error in Java:")
            print(compprocess.stderr)

        else:
            runprocess = subprocess.run(
                ["java", "-cp", tmp_dir, class_name],
                capture_output=True, text=True
            )
            
            if runprocess.returncode != 0:
                print("TBMRCL [Cod 039] Execution Error in Java:")
                print(runprocess.stderr)
                
            else:
                print(runprocess.stdout)

    except FileNotFoundError:
        print("TBMRCL [Cod 040] Java JDK ('javac' / 'java') not found, install Java JDK and add to your PATH --> https://adoptium.net/")

    except Exception as e:
        print(f"TBMRCL [Cod UNKNW] Unexcepted Error {e}")

    finally:
        if os.path.exists(tmp_dir):
            shutil.rmtree(tmp_dir, ignore_errors=True)

def asm(asmcode):
    asmcd = f"{asmcode}"

    with tempfile.NamedTemporaryFile(delete=False, suffix=".asm", mode="w", encoding="utf-8") as f_asm:
        f_asm.write(asmcd)
        asmdir = f_asm.name

    objdir = asmdir.replace(".asm", ".obj" if sys.platform == "win32" else ".o")
    exedir = asmdir.replace(".asm", ".exe" if sys.platform == "win32" else "")

    try:
        format_flag = "win64" if sys.platform == "win32" else "elf64"
        
        nasm_process = subprocess.run(
            ["nasm", "-f", format_flag, asmdir, "-o", objdir],
            capture_output=True,
            text=True
        )

        if nasm_process.returncode != 0:
            print("TBMRCL [Cod 041] Assembly Error (NASM):")
            print(nasm_process.stderr)
        else:
            link_process = subprocess.run(
                ["gcc", objdir, "-o", exedir],
                capture_output=True,
                text=True
            )

            if link_process.returncode != 0:
                print("TBMRCL [Cod 042] Linking Error in Assembly:")
                print(link_process.stderr)
            else:
                run_cmd = [exedir] if sys.platform == "win32" else [f"./{os.path.basename(exedir)}"]
                result = subprocess.run(run_cmd, capture_output=True, text=True, check=True, cwd=os.path.dirname(asmdir))
                print(result.stdout)

    except FileNotFoundError:
        print("TBMRCL [Cod 043] Assembler 'nasm' or linker 'gcc' not found. Install NASM and GCC/MinGW -> https://www.nasm.us/")

    except Exception as e:
        print(f"TBMRCL [Cod UNKNW] Unexpected error: {e}")

    finally:
        for path in [asmdir, objdir, exedir]:
            if path and os.path.exists(path):
                try:
                    os.remove(path)
                except:
                    pass




    


        

        

        
        
            


        


            
    




 


        
        
        
        
        
        


    

    

            
            
    
        
        
    
                  
            
    
    
    
    
    
    


    
    
    
    
    







































# By IsaacLindo123 (github)
