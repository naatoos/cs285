import abc
import numpy as np


class BasePolicy(object, metaclass=abc.ABCMeta):
    def get_action(self, obs: np.ndarray) -> np.ndarray:
        raise NotImplementedError

    def update(self, observations: np.ndarray, actions: np.ndarray, **kwargs) -> dict:
        """Return a dictionary of logging information."""
        raise NotImplementedError

    def save(self, filepath: str):
        raise NotImplementedError
