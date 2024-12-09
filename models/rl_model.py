import numpy as np
import random
import gym

class RouletteEnv(gym.Env):
    def __init__(self):
        self.action_space = gym.spaces.Discrete(37)
        self.state_space = gym.spaces.Discrete(1)

    def step(self, action):
        result = random.randint(0, 36)
        reward = 1 if action == result else 0
        done = True
        return np.array([0]), reward, done, {}

    def reset(self):
        return np.array([0])

def train_rl_model():
    env = RouletteEnv()
    Q = np.zeros([env.action_space.n, env.state_space.n])
    alpha = 0.1
    gamma = 0.95
    epsilon = 1.0

    for episode in range(10000):
        state = env.reset()
        done = False
        while not done:
            if random.uniform(0, 1) < epsilon:
                action = env.action_space.sample()
            else:
                action = np.argmax(Q[:, state[0]])
            next_state, reward, done, _ = env.step(action)
            Q[action, state[0]] = Q[action, state[0]] + alpha * (reward + gamma * np.max(Q[:, next_state[0]]) - Q[action, state[0]])
            state = next_state

    return Q

# Usage example
if __name__ == "__main__":
    Q = train_rl_model()
    print("Trained Q-table:", Q)
