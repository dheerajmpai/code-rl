
import subprocess
import platform
import re


def check_c_compiler():
    def get_version(command):
        result = subprocess.run([command, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        version = re.search(r"\d+\.\d+\.\d+", result.stdout)
        return version.group(0) if version else "unknown version"

    try:
        subprocess.run(["gcc", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        gcc_version = get_version("gcc")
        return f"GCC is installed, version: {gcc_version}.", "gcc"
    except FileNotFoundError:
        try:
            subprocess.run(["clang", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            clang_version = get_version("clang")
            return f"Clang is installed, version: {clang_version}.", "clang"
        except FileNotFoundError:
            os_name = platform.system()
            if os_name == "Linux":
                return "Install GCC or Clang using your package manager (e.g., 'sudo apt install gcc').", None
            elif os_name == "Darwin":
                return "Install GCC or Clang using Homebrew (e.g., 'brew install gcc').", None
            elif os_name == "Windows":
                return "Install GCC or Clang via LLVM, MinGW or Cygwin, or consider using Microsoft Visual Studio.", None
            else:
                return f"Operating system '{os_name}' not recognized. Please install a C compiler manually.", None

def check_java_compiler():
    def get_version(command):
        result = subprocess.run([command, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        version = re.search(r"\d+\.\d+\.\d+", result.stdout)
        return version.group(0) if version else "unknown version"
    try:
        subprocess.run(["javac", "-version"], stderr=subprocess.DEVNULL)
        javac_version = get_version("javac")
        return f"Java Compiler (javac) is installed, version: {javac_version}.", "javac"
    except FileNotFoundError:
        os_name = platform.system()
        if os_name == "Linux":
            return "Install Java JDK using your package manager (e.g., 'sudo apt install default-jdk').", None
        elif os_name == "Darwin":
            return "Install Java JDK using Homebrew (e.g., 'brew cask install java').", None
        elif os_name == "Windows":
            return "Download and install Java JDK from the Oracle website or use a package manager like Chocolatey.", None
        else:
            return f"Operating system '{os_name}' not recognized. Please install Java JDK manually.", None

def check_cpp_compiler():
    def get_version(command):
        result = subprocess.run([command, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        version = re.search(r"\d+\.\d+\.\d+", result.stdout)
        return version.group(0) if version else "unknown version"

    try:
        subprocess.run(["g++", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        gpp_version = get_version("g++")
        return f"G++ is installed, version: {gpp_version}.", "g++"
    except FileNotFoundError:
        try:
            subprocess.run(["clang++", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            clangpp_version = get_version("clang++")
            return f"Clang++ is installed, version: {clangpp_version}.", "clang++"
        except FileNotFoundError:
            os_name = platform.system()
            if os_name == "Linux":
                return "Install G++ or Clang++ using your package manager (e.g., 'sudo apt install g++').", None
            elif os_name == "Darwin":
                return "Install G++ or Clang++ using Homebrew (e.g., 'brew install gcc').", None
            elif os_name == "Windows":
                return "Install G++ or Clang++ via LLVM, MinGW or Cygwin, or consider using Microsoft Visual Studio.", None
            else:
                return f"Operating system '{os_name}' not recognized. Please install a C++ compiler manually.", None


def check_go_compiler():
    def get_version(command):
        result = subprocess.run([command, "version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        version = re.search(r"go\d+\.\d+\.\d+", result.stdout)
        return version.group(0) if version else "unknown version"

    try:
        subprocess.run(["go", "version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        go_version = get_version("go")
        return f"Go is installed, version: {go_version}.", "go"
    except FileNotFoundError:
        os_name = platform.system()
        if os_name == "Linux":
            return "Install Go using your package manager (e.g., 'sudo apt install golang').", None
        elif os_name == "Darwin":
            return "Install Go using Homebrew (e.g., 'brew install go').", None
        elif os_name == "Windows":
            return "Download and install Go from the official Golang website or use a package manager like Chocolatey.", None
        else:
            return f"Operating system '{os_name}' not recognized. Please install Go manually.", None


def check_csharp_compiler():
    def get_version(command):
        result = subprocess.run([command, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        version = re.search(r"\d+\.\d+\.\d+", result.stdout)
        return version.group(0) if version else "unknown version"

    try:
        subprocess.run(["csc", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        csc_version = get_version("csc")
        return f"C# Compiler (csc) is installed, version: {csc_version}.", "csc"
    except FileNotFoundError:
        try:
            subprocess.run(["mcs", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            mcs_version = get_version("mcs")
            return f"Mono C# Compiler (mcs) is installed, version: {mcs_version}.", "mcs"
        except FileNotFoundError:
            os_name = platform.system()
            if os_name == "Linux":
                return "Install Mono or .NET SDK using your package manager (e.g., 'sudo apt install mono-complete').", None
            elif os_name == "Darwin":
                return "Install Mono or .NET SDK using Homebrew (e.g., 'brew install mono').", None
            elif os_name == "Windows":
                return "Install .NET SDK from the Microsoft website or use Visual Studio.", None
            else:
                return f"Operating system '{os_name}' not recognized. Please install a C# compiler manually.", None


def check_rust_compiler():
    def get_version(command):
        result = subprocess.run([command, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        version = re.search(r"\d+\.\d+\.\d+", result.stdout)
        return version.group(0) if version else "unknown version"

    try:
        subprocess.run(["rustc", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        rustc_version = get_version("rustc")
        return f"Rust Compiler (rustc) is installed, version: {rustc_version}.", "rustc"
    except FileNotFoundError:
        os_name = platform.system()
        if os_name == "Linux":
            return "Install Rust using rustup (e.g., 'curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh').", None
        elif os_name == "Darwin":
            return "Install Rust using rustup or Homebrew (e.g., 'brew install rust').", None
        elif os_name == "Windows":
            return "Install Rust using rustup (download from https://rustup.rs/).", None
        else:
            return f"Operating system '{os_name}' not recognized. Please install Rust manually.", None


def check_javascript_environment():
    def get_version(command):
        result = subprocess.run([command, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        version = re.search(r"\d+\.\d+\.\d+", result.stdout)
        return version.group(0) if version else "unknown version"

    # Check for Node.js
    try:
        subprocess.run(["node", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        node_version = get_version("node")
        return f"Node.js is installed, version: {node_version}.", "node"
    except FileNotFoundError:
        os_name = platform.system()
        if os_name == "Linux":
            return "Node.js is not installed. Install it using your package manager (e.g., 'sudo apt install nodejs').", None
        elif os_name == "Darwin":
            return "Node.js is not installed. Install it using Homebrew (e.g., 'brew install node').", None
        elif os_name == "Windows":
            return "Node.js is not installed. Download and install it from the Node.js website.", None
        else:
            return f"Operating system '{os_name}' not recognized. Please install Node.js manually.", None


def check_haskell_compiler():
    def get_version(command):
        result = subprocess.run([command, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        version = re.search(r"\d+\.\d+\.\d+", result.stdout)
        return version.group(0) if version else "unknown version"

    try:
        subprocess.run(["ghc", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        ghc_version = get_version("ghc")
        return f"Haskell Compiler (GHC) is installed, version: {ghc_version}.", "ghc"
    except FileNotFoundError:
        os_name = platform.system()
        if os_name == "Linux":
            return "Install Haskell GHC using your package manager (e.g., 'sudo apt install ghc').", None
        elif os_name == "Darwin":
            return "Install Haskell GHC using Homebrew (e.g., 'brew install ghc').", None
        elif os_name == "Windows":
            return "Download and install Haskell GHC from the Haskell website or use a package manager like Chocolatey.", None
        else:
            return f"Operating system '{os_name}' not recognized. Please install Haskell GHC manually.", None

def check_typescript_compiler():
    def get_version(command):
        result = subprocess.run([command, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        version = re.search(r"\d+\.\d+\.\d+", result.stdout)
        return version.group(0) if version else "unknown version"

    try:
        subprocess.run(["tsc", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        tsc_version = get_version("tsc")
        return f"TypeScript Compiler (tsc) is installed, version: {tsc_version}.", "tsc"
    except FileNotFoundError:
        os_name = platform.system()
        if os_name == "Linux" or os_name == "Darwin":
            return "Install Node.js and TypeScript using npm (e.g., 'npm install -g typescript').", None
        elif os_name == "Windows":
            return "Install Node.js from the official website and then TypeScript using npm (e.g., 'npm install -g typescript').", None
        else:
            return f"Operating system '{os_name}' not recognized. Please install Node.js and TypeScript manually.", None

def check_php_compiler():
    def get_version(command):
        result = subprocess.run([command, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        version = re.search(r"\d+\.\d+\.\d+", result.stdout)
        return version.group(0) if version else "unknown version"

    try:
        subprocess.run(["php", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        php_version = get_version("php")
        return f"PHP is installed, version: {php_version}.", "php"
    except FileNotFoundError:
        os_name = platform.system()
        if os_name == "Linux":
            return "Install PHP using your package manager (e.g., 'sudo apt install php').", None
        elif os_name == "Darwin":
            return "Install PHP using Homebrew (e.g., 'brew install php').", None
        elif os_name == "Windows":
            return "Download and install PHP from the PHP website or use a package manager like Chocolatey.", None
        else:
            return f"Operating system '{os_name}' not recognized. Please install PHP manually.", None

def check_kotlin_compiler():
    def get_version(command):
        result = subprocess.run([command, "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        version = re.search(r"\d+\.\d+\.\d+", result.stdout + result.stderr)
        return version.group(0) if version else "unknown version"

    try:
        subprocess.run(["kotlinc", "-version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        kotlinc_version = get_version("kotlinc")
        return f"Kotlin Compiler (kotlinc) is installed, version: {kotlinc_version}.", "kotlinc"
    except FileNotFoundError:
        os_name = platform.system()
        sdkman_instructions = (
            "To install SDKMAN!, open your terminal and run:\n"
            "curl -s \"https://get.sdkman.io\" | bash\n"
            "Then, start a new terminal session or run:\n"
            "source \"$HOME/.sdkman/bin/sdkman-init.sh\"\n"
            "Finally, install Kotlin with:\n"
            "sdk install kotlin\n"
        )
        if os_name == "Linux" or os_name == "Darwin":
            return sdkman_instructions, None
        elif os_name == "Windows":
            return sdkman_instructions + "Note: For Windows, use WSL (Windows Subsystem for Linux) to run SDKMAN!.", None
        else:
            return f"Operating system '{os_name}' not recognized. Please install Kotlin manually.", None

def check_ruby_compiler():
    def get_version(command):
        result = subprocess.run([command, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        version = re.search(r"\d+\.\d+\.\d+", result.stdout)
        return version.group(0) if version else "unknown version"

    try:
        subprocess.run(["ruby", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        ruby_version = get_version("ruby")
        return f"Ruby is installed, version: {ruby_version}.", "ruby"
    except FileNotFoundError:
        os_name = platform.system()
        if os_name == "Linux":
            return "Install Ruby using your package manager (e.g., 'sudo apt install ruby').", None
        elif os_name == "Darwin":
            return "Install Ruby using Homebrew (e.g., 'brew install ruby').", None
        elif os_name == "Windows":
            return "Install Ruby using RubyInstaller for Windows.", None
        else:
            return f"Operating system '{os_name}' not recognized. Please install Ruby manually.", None

def check_swift_compiler():
    def get_version(command):
        result = subprocess.run([command, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        version = re.search(r"\d+\.\d+\.\d+", result.stdout)
        return version.group(0) if version else "unknown version"

    try:
        subprocess.run(["swift", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        swift_version = get_version("swift")
        return f"Swift compiler is installed, version: {swift_version}.", "swift"
    except FileNotFoundError:
        os_name = platform.system()
        if os_name == "Linux":
            return "Install Swift using your package manager or download from Swift.org.", None
        elif os_name == "Darwin":
            return "Install Swift by installing Xcode from the App Store.", None
        elif os_name == "Windows":
            return "Swift is not natively supported on Windows. Consider using a Swift-compatible IDE or WSL.", None
        else:
            return f"Operating system '{os_name}' not recognized. Please install Swift manually.", None

def check_cuda_compiler():
    def get_version(command):
        result = subprocess.run([command, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        version = re.search(r"release (\d+\.\d+)", result.stdout)
        return version.group(1) if version else "unknown version"

    try:
        subprocess.run(["nvcc", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        nvcc_version = get_version("nvcc")
        return f"CUDA Compiler (nvcc) is installed, version: {nvcc_version}.", "nvcc"
    except FileNotFoundError:
        os_name = platform.system()
        if os_name in ["Linux", "Darwin"]:
            return "Install CUDA Toolkit from NVIDIA's website or use your package manager.", None
        elif os_name == "Windows":
            return "Install CUDA Toolkit from NVIDIA's website.", None
        else:
            return f"Operating system '{os_name}' not recognized. Please install CUDA manually.", None

def check_docker():
    def get_version():
        result = subprocess.run(["docker", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        version = re.search(r"\d+\.\d+\.\d+", result.stdout)
        return version.group(0) if version else "unknown version"

    try:
        subprocess.run(["docker", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        docker_version = get_version()
        return f"Docker is installed, version: {docker_version}.", "docker"
    except FileNotFoundError:
        os_name = platform.system()
        if os_name == "Linux":
            return "Install Docker using your package manager (e.g., 'sudo apt install docker').", None
        elif os_name == "Darwin":
            return "Install Docker Desktop from the Docker website.", None
        elif os_name == "Windows":
            return "Install Docker Desktop from the Docker website.", None
        else:
            return f"Operating system '{os_name}' not recognized. Please install Docker manually.", None

def check_aws_cli():
    def get_version():
        try:
            result = subprocess.run(["aws", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            version = re.search(r"aws-cli/(\d+\.\d+\.\d+)", result.stdout)
            return version.group(1) if version else "unknown version"
        except FileNotFoundError:
            return None

    aws_cli_version = get_version()
    if aws_cli_version:
        return f"AWS CLI is installed, version: {aws_cli_version}.", "aws"
    else:
        os_name = platform.system()
        if os_name == "Linux":
            return "Install AWS CLI using your package manager or follow the instructions on the AWS website.", None
        elif os_name == "Darwin":
            return "Install AWS CLI using Homebrew (e.g., 'brew install awscli') or follow the instructions on the AWS website.", None
        elif os_name == "Windows":
            return "Download and install AWS CLI from the AWS website.", None
        else:
            return f"Operating system '{os_name}' not recognized. Please install AWS CLI manually.", None


language_check_functions = {
    "c": check_c_compiler,
    "java": check_java_compiler,
    "cpp": check_cpp_compiler,
    "go": check_go_compiler,
    "cs": check_csharp_compiler,
    "rust": check_rust_compiler,
    "ts": check_typescript_compiler,
    "php": check_php_compiler,
    "haskell": check_haskell_compiler,
    "ruby": check_ruby_compiler,
    "swift": check_swift_compiler,
    "cuda": check_cuda_compiler,
    "kotlin": check_kotlin_compiler,
    "js": check_javascript_environment
}

tool_check_functions = {
    "docker": check_docker,
    "aws": check_aws_cli
    # TODO: Add more tools here if needed
}


if __name__ == "__main__":
    # print(check_c_compiler()[0])
    # print(check_java_compiler()[0])
    # print(check_cpp_compiler()[0])
    # print(check_go_compiler()[0])
    # print(check_csharp_compiler()[0])
    # print(check_rust_compiler()[0])
    # print(check_typescript_compiler()[0])
    # print(check_php_compiler()[0])
    # print(check_haskell_compiler()[0])
    # print(check_ruby_compiler()[0])
    # print(check_swift_compiler()[0])
    # print(check_cuda_compiler()[0])
    # print(check_kotlin_compiler()[0])
    # print(check_javascript_environment()[0])
    # print(check_aws_cli()[0])

    # print(check_docker()[0])

    for language, check_function in language_check_functions.items():
        print(f"{language}: {check_function()[0]}")

    for tool, check_function in tool_check_functions.items():
        print(f"{tool}: {check_function()[0]}")
    pass

