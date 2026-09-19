# Enterprise Lead Routing & Scoring Module
# Engineered for High-Throughput Service Ingestion

class LeadScorer:
    def __init__(self):
        self.weights = {'budget': 0.4, 'urgency': 0.3, 'fit': 0.3}

    def score(self, lead):
        return sum(lead.get(k, 0) * w for k, w in self.weights.items())
