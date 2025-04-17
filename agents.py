import random

class BaseAgent:
    def __init__(self, agent_id, position, agent_type):
        self.agent_id = agent_id
        self.position = position
        self.target = None 
        self.path = []
        self.agent_type = agent_type 
        self.is_busy = False

    def assign_task(self, target, path):
        self.target = target
        self.path = path
        self.is_busy = True

    def move_step(self):
        if self.path:
            self.position = self.path.pop(0)
            if not self.path:
                self.is_busy = False
                self.target = None

    def __repr__(self):
        return f"{self.agent_type.capitalize()}Agent#{self.agent_id} at {self.position}"


class RobotAgent(BaseAgent):
    def __init__(self, agent_id, position):
        super().__init__(agent_id, position, "robot")


class HumanAgent(BaseAgent):
    def __init__(self, agent_id, position):
        super().__init__(agent_id, position, "human")
