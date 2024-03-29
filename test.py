# Simple env test.
import json
import select
import time
import logging
import os

import aicrowd_helper
import gym

import coloredlogs
coloredlogs.install(logging.DEBUG)

# All the evaluations will be evaluated on MineRLObtainDiamond-v0 environment
MINERL_GYM_ENV = os.getenv('MINERL_GYM_ENV', 'MineRLObtainDiamond-v0')

def main():
    """
    This function will be called for training phase.
    """
    # Sample code for illustration, add your code below to run in test phase.
    # Load trained model from train/ directory
    env = gym.make(MINERL_GYM_ENV)

    actions = [env.action_space.sample() for _ in range(10)]
    xposes = []
    for _ in range(1):
        obs = env.reset()
        done = False
        netr = 0
        while not done:
            random_act = env.action_space.noop()
            random_act['camera'] = [0, 0.3]
            random_act['back'] = 0
            random_act['forward'] = 1
            random_act['jump'] = 1
            random_act['attack'] = 1
            obs, reward, done, info = env.step(random_act)
            netr += reward
            env.render()

    env.close()

if __name__ == "__main__":
    main()
