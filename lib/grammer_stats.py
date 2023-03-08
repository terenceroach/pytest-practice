class GrammerStats:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def check(self, text):
        valid_endings = ['.', '?', '!']

        if text[0].isupper() and text[-1] in valid_endings:
            self.passed += 1
            return True
        else:
            self.failed += 1
            return False
        
    def percentage_good(self):
        print("Passed: " + str(self.passed))
        print("Failed: " + str(self.failed))
        total_checks = self.passed + self.failed
        percent_passed = (self.passed / total_checks) * 100
        return int(percent_passed)