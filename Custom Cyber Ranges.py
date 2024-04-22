import random

class CyberRange:
    def __init__(self, num_hosts, num_attackers):
        self.num_hosts = num_hosts
        self.num_attackers = num_attackers
        self.hosts = [f"Host_{i}" for i in range(num_hosts)]
        self.attackers = [f"Attacker_{i}" for i in range(num_attackers)]
    
    def simulate_attack(self):
        attacker = random.choice(self.attackers)
        target = random.choice(self.hosts)
        print(f"{attacker} is attacking {target}")
    
    def simulate_defense(self):
        defender = random.choice(self.hosts)
        target = random.choice(self.attackers)
        print(f"{defender} is defending against {target}")
    
    def simulate_scenario(self):
        print("Starting cyber range simulation...")
        for _ in range(5):  # Replace with appropriate number of rounds
            self.simulate_attack()
            self.simulate_defense()
        print("Cyber range simulation completed.")

if __name__ == "__main__":
    num_hosts = 10  # Number of hosts in the cyber range
    num_attackers = 3  # Number of attackers in the cyber range
    cyber_range = CyberRange(num_hosts, num_attackers)
    cyber_range.simulate_scenario()
