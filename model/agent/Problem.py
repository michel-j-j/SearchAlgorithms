class Problem:
    def __init__(self, states, initial, goal, actions, transition_model, cost):
        self.states = states
        if initial not in states:
            self.states.append(initial)
        self.initial = initial
        if goal not in states:
          self.states.append(goal)
        self.goal = goal
        self.actions = actions
        self.transition_model = transition_model
        self.cost = cost

    def get_actions(self, state):
        return self.actions [state]
    
    def result(self, state, action):
     return self.transition_model [state][action]
    
    def goal_test(self, state):
     return state== self.goal
    
    def action_cost (self, state1, action, state2):
        if action in self.actions [state1] and state2== self.result(state1, action):
           return self.cost [state1][state2]
        else:
            return -1