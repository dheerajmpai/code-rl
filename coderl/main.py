
"""
main.py
====================================
The core module of the 'code-rl' project, this script defines the CodeCompilerEnv class, 
a gym environment for compiling and executing code in various programming languages. 
It also sets up default configurations for different languages such as C, Java, Go, PHP, C#, C++, CUDA, and SystemVerilog.

Classes:

    CodeCompilerEnv: A custom gym environment that handles the compilation and execution 
    of code written in various languages. It supports configurable compiler flags, input 
    and output file handling, and execution commands.

Global Variables:
    defaultConfig: Dictionary containing the default configuration for C language.
    defaultConfigJava: Dictionary containing the default configuration for Java.
    defaultConfigGo: Dictionary containing the default configuration for Go.
    defaultConfigPHP: Dictionary containing the default configuration for PHP.
    defaultConfigCSharp: Dictionary containing the default configuration for C#.
    defaultConfigCPP: Dictionary containing the default configuration for C++.
    defaultConfigCUDA: Dictionary containing the default configuration for CUDA.
    defaultConfigSystemVerilog: Dictionary containing the default configuration for SystemVerilog.
"""

import gym
import subprocess
from gym import spaces
from .utils import check_c_compiler, check_java_compiler, language_check_functions
# from .utils import check_c_compiler

defaultConfig = {
    "lang": "c",
    "reward_levels": [("", -4), ("-Werror", -3), ("-Werror -Wall", -2), ("-Werror -Wall -Wextra", -1)],
    "compiler_path": "gcc", # Currently not supported
    "execute": True,
    "run_command":"./{run_file}",
    "pre_flag":"",
    "post_flag":"",
    "input_filename": "temp_code.c",
    "io_args": "-o",
    
    "output_filename": "temp_executable",
    "post_output_args":"",
    "run_file" : "temp_executable"


}

defaultConfigJava = {
    "lang": "java",
    "reward_levels": [("", -4), ("-Xlint:all -Werror", -3)], # Add more based on javac -help -X
    "compiler_path": "javac", # Currently not supported
    "execute": True,
    "run_command":"java Main",
    "pre_flag":"",
    "post_flag":"",
    "input_filename": "Main.java",
    "io_args": "",
    "output_filename": "",
    "post_output_args":"",
    "run_file": ""
}

defaultConfigGo = {
    "lang": "go",
    "reward_levels": [("build", -1)],  # Simplified, as Go does not use the same flags as gcc or javac
    "compiler_path": "go",  # For compilation
    "execute": True,
    "run_command": "go run {input_file}",  # For execution
    "pre_flag": "",
    "post_flag": "",
    "input_filename": "main.go",  # Go files typically use the .go extension
    "io_args": "",
    "output_filename": "",  # 'go run' does not need an output file specified
    "post_output_args": "",
    "run_file": "main.go"
}

defaultConfigPHP = {
    "lang": "php",
    "reward_levels": [("", -1)],  # PHP doesn't have compiler flags like C++, but you can define different error levels if needed
    "interpreter_path": "php",  # PHP interpreter
    "execute": True,
    "run_command": "php {input_file}",
    "input_filename": "temp_code.php",
    "output_filename": "",  # Not applicable for PHP as it doesn't produce a separate output file
    "post_output_args": "",
    "example": """<?php
echo "Hello, World!";
?>
"""
}



class CodeCompilerEnv(gym.Env):
    """
    A gym environment for compiling and executing code in various programming languages.
    It allows the user to define custom configurations for different languages, handling
    compiler flags, file inputs/outputs, and execution commands.

    Attributes:
        reward_levels (list): A list of tuples containing compiler flags and corresponding rewards.
        config (dict): Configuration dictionary for the selected language.
        execute (bool): Flag to determine whether to execute the compiled code.
        input_filename (str): Name of the file where the input code will be written.
        io_args (str): Additional arguments for input/output processing.
        output_filename (str): Name of the output file generated after compilation.
        post_output_args (str): Additional arguments after output file is generated.
        pre_flag (str): Additional flags before the main compiler command.
        post_flag (str): Additional flags after the main compiler command.
        run_file (str): Name of the file to run after compilation.
        action_space (gym.spaces): Gym space representing the action space.
        observation_space (gym.spaces): Gym space representing the observation space.

    Methods:
        step(action): Executes one step of the environment's dynamics.
        reset(): Resets the environment to an initial state.
        render(mode='human'): Renders one frame of the environment. (Not implemented)
        close(): Performs any necessary cleanup. (Not implemented)
    """

    def __init__(self, config= defaultConfig):
        """
        Initializes the CodeCompilerEnv environment with a given configuration.

        Args:
            config (dict): A dictionary containing configuration parameters. Defaults to defaultConfig.
        """
        super(CodeCompilerEnv, self).__init__()
        self.reward_levels = config["reward_levels"]
        self.config = config
        self.execute = config["execute"]
        self.input_filename = config["input_filename"]
        self.io_args = config["io_args"]
        self.output_filename = config["output_filename"]
        self.post_output_args = config["post_output_args"]
        self.pre_flag = config ["pre_flag"]
        self.post_flag = config ["post_flag"]
        self.run_file = config ["run_file"]
        # Define the action and observation spaces
        repr_out, self.command = language_check_functions[config['lang']]()
        print(repr_out)
        self.action_space = spaces.Box(low=0, high=255, shape=(1000,), dtype='uint8')  # Placeholder
        self.observation_space = spaces.Discrete(2)  # Success or failure

    def step(self, action):
        """
        Executes one step of the environment's dynamics. It involves writing the action (code) 
        to a file, compiling it with increasing levels of warnings, and optionally executing it.

        Args:
            action (str): The source code to be compiled and executed.

        Returns:
            tuple: A tuple containing the observation, reward, done status, and additional info.
        """

        # Convert action (code) into a file
        with open(self.input_filename, 'w') as file:
            file.write(action)

        # Define the reward levels
        reward_levels = self.reward_levels
        reward = reward_levels[0][1]  # Default reward if compilation fails without flags
        errored = False;
        # Compiling with increasing levels of warnings
        for flags, reward_value in reward_levels:
            result = subprocess.run(f"{self.command} {self.pre_flag} {flags} {self.post_flag} {self.input_filename} {self.io_args} {self.output_filename} {self.post_output_args}", shell=True, capture_output=True, text=True)
            print("compile result", result)

            if result.returncode != 0:
                reward = reward_value
                errored = True;
                break
        # Check runtime success
        if (not errored) and (self.execute == True):
            run_command = self.config["run_command"].format(
                run_file=f"{self.run_file}"
            )

            result = subprocess.run(run_command, shell=True, capture_output=True, text=True)
            print("run result", result)
            if result.returncode == 0:
                reward = 1
                # TODO: Further checks for test cases can be implemented here
                # If all test cases pass:
                # reward = 10
        if reward == 1:
            observation = 1 # success
        else:
            if (self.execute == False) and (errored == False):
                observation = 1 # Success
            else:
                observation = 0 # Failed

        info = {}

        if result.returncode == 0:
            info["stdout"] = result.stdout
        else:
            info["stderr"] = result.stderr

        return observation, reward, True, info  # Sample observation, reward, done, info

    def reset(self):
        """
        Resets the environment to an initial state. Generates a new sample observation. MUST be redefined for custom environments.

        Returns:
            int: A sample observation from the observation space.
        """

        # Reset the environment to an initial state
        return self.observation_space.sample()  # Sample observation

    def render(self, mode='human'):
        """
        Renders one frame of the environment. (Currently not implemented)

        Args:
            mode (str): The mode to render with. Defaults to 'human'.
        """
        pass

    def close(self):
        """
        Performs any necessary cleanup. (Currently not implemented)
        """
        pass

defaultConfigCSharp = {
    "lang": "cs",
    "reward_levels": [("", -1)],  # Simplified, as mcs doesn't have equivalent warning flags
    "compiler_path": "mcs",
    "execute": True,
    "run_command": "mono {run_file}.exe",
    "pre_flag": "",
    "post_flag": "",
    "input_filename": "MainClass.cs",  # Name of the C# source file
    "io_args": "-out:MainClass.exe",
    "output_filename": "",    # Name of the compiled executable
    "post_output_args": "",
    "run_file":"MainClass"
}

defaultConfigCPP = {
    "lang": "cpp",
    "reward_levels": [("", -4), ("-Werror", -3), ("-Werror -Wall", -2), ("-Werror -Wall -Wextra", -1)],
    "compiler_path": "g++",  # g++ is typically used for compiling C++ code
    "execute": True,
    "run_command":"./{run_file}",
    "pre_flag":"",
    "post_flag":"",
    "input_filename": "temp_code.cpp",
    "io_args": "-o",
    "output_filename": "temp_executable",
    "post_output_args":"",
    "run_file": "temp_executable"
}
defaultConfigCUDA = {
    "lang": "cuda",
    "reward_levels": [("", -4)],  # Customize as needed
    "compiler_path": "nvcc",  # NVIDIA CUDA Compiler
    "execute": True,
    "run_command":"./{run_file}",
    "pre_flag":"",
    "post_flag":"",
    "input_filename": "temp_code.cu",  # CUDA files typically have a .cu extension
    "io_args": "-o",
    "output_filename": "temp_executable",
    "post_output_args":"",
    "run_file": "temp_executable"
}

defaultConfigSystemVerilog = {
    "lang": "systemverilog",
    "reward_levels": [("", -1)],  # Adjust based on the simulator's warning/error system
    "compiler_path": "iverilog",  # Icarus Verilog for SystemVerilog
    "execute": True,
    "run_command": "vvp {run_file}",
    "pre_flag": "",
    "post_flag": "",
    "input_filename": "temp_code.sv",
    "io_args": "-o",
    "output_filename": "temp_output",
    "post_output_args": "",
    "run_file": "temp_output"
}


if __name__ == "__main__":
    env = CodeCompilerEnv(defaultConfigCUDA)

    pass
