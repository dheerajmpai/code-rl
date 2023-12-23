

import gym
import subprocess
from gym import spaces

class CodeCompilerEnv(gym.Env):
    def __init__(self):
        super(CodeCompilorEnv, self).__init__()
        # Define the action and observation spaces
        self.action_space = spaces.Box(low=0, high=255, shape=(1000,), dtype='uint8')  # Placeholder
        self.observation_space = spaces.Discrete(2)  # Success or failure

    def step(self, action):
        # Convert action (code) into a file
        with open('temp_code.c', 'w') as file:
            file.write(action)

        # Define the reward levels
        reward_levels = [("", -4), ("-Werror", -3), ("-Werror -Wall", -2), ("-Werror -Wall -Wextra", -1)]
        reward = -4  # Default reward if compilation fails without flags
        errored = False;
        # Compiling with increasing levels of warnings
        for flags, reward_value in reward_levels:
            result = subprocess.run(f"gcc {flags} temp_code.c -o temp_executable", shell=True, capture_output=True, text=True)
            if result.returncode != 0:
                reward = reward_value
                errored = True;
                break
        # Check runtime success
        if not errored:
            result = subprocess.run("./temp_executable", capture_output=True, text=True)
            if result.returncode == 0:
                reward = 1
                # TODO: Further checks for test cases can be implemented here
                # If all test cases pass:
                # reward = 10
        if reward == 1:
            observation = 1 # success
        else:
            observation = 0
        info = {}

        if result.returncode == 0:
            info["stdout"] = result.stdout
        else:
            info["stderr"] = result.stderr

        return observation, reward, True, info  # Sample observation, reward, done, info

    def reset(self):
        # Reset the environment to an initial state
        return self.observation_space.sample()  # Sample observation

    def render(self, mode='human'):
        pass

    def close(self):
        pass
