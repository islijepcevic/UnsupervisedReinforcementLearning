"""THIS FILE IS NOT NEEDED
THE SKELETON OF THE ALGORITHM IS IMPLEMENTED IN race.py
"""

class SarsaLambda:

    def __init__(self, agent, environment, gamma, nepisodes):
        
        self.agent = agent
        self.environment = environment

        self.nepisodes = nepisodes

        self.gamma = gamma
    
    def learn(self):

        # init Q(s, a) for every (s, a)

        for episode in xrange(self.nepisodes):

            # init (s, a)

            while True:

                # take action a

                # observe reward and s'

                # calculate Qnext
                delta = reward + self.gamma*Qnext - Q

                eligibility += 1

                for (s, a) in states_and_actions:
                    Q(s, a) += alpha*delta*eligibility(s, a)
                    eligibility(s, a) = gamma * lmbda * eligibility(s, a)
