class InvalidVoterException(Exception):
    def __init__(self, message="Age is less than 18, cannot vote!"):
        self.message = message
        super().__init__(self.message)

def check_voter_age(age):
    if age < 18:
        raise InvalidVoterException(f"Invalid age: {age}. You must be at least 18 to vote.")
    else:
        print("You are eligible to vote.")

# Example usage
try:
    age = int(input("Enter your age: "))
    check_voter_age(age)
except InvalidVoterException as e:
    print(f"Error: {e}")
