# curiosity : The ability to learn new things quickly and effectively
# independent_delivery : The ability to work independently and make decisions without constant supervision
# technical_proficiency : Deep understanding of languages (like Python), frameworks, and underlying computer science principles
# problem_solving : Breaking down complex, ambiguous problems into smaller, manageable, and logical steps to find an efficient solution
# attention_to_quality : Writing clean, readable code and identifying edge cases or potential bugs before they reach the user.
# cross_functional_collaberation : The ability to work effectively within a team (using tools like Git) and across different departments to reach a common goal.
# effective_communication : The ability to explain complex technical concepts clearly to both fellow developers and non-technical stakeholders.
# ownership_and_accountability: : Taking full responsibility for your code from development through to production. It means "owning" the outcome, not just the task.
# system_thinking : The ability to see the big picture and understand how your work fits into the overall goals of the project or organization.
# strategic_alignment : The ability to align your work with the organization's goals and make decisions that contribute to the organization's success.

DEVELOPER_TRAITS = ["curiosity", "independent_delivery", "technical_proficiency", "problem_solving", "attention_to_quality", "cross_functional_collaboration", "effective_communication", "ownership_and_accountability", "system_thinking", "strategic_alignment"]

class DeveloperProfile:
    def __init__(self):
        self.curiosity = False
        self.independent_delivery = False
        self.technical_proficiency = False
        self.problem_solving = False
        self.attention_to_quality = False
        self.cross_functional_collaboration = False
        self.effective_communication = False
        self.ownership_and_accountability = False
        self.system_thinking = False
        self.strategic_alignment = False

    def __str__(self):
        traits = [
            trait.replace("_", " ").title()
            for trait in DEVELOPER_TRAITS
            if getattr(self, trait)
        ]

        developer_traits= "".join([f"\n - {trait}" for trait in traits])

        return f"Developer Profile: {developer_traits}"

class ProfileBuilder:
    def __init__(self):
        self.profile = DeveloperProfile()

    def set_curiosity(self):
        self.profile.curiosity = True
        return self

    def set_independent_delivery(self):
        self.profile.independent_delivery = True
        return self

    def set_technical_proficiency(self):
        self.profile.technical_proficiency = True
        return self

    def set_problem_solving(self):
        self.profile.problem_solving = True
        return self

    def set_attention_to_quality(self):
        self.profile.attention_to_quality = True
        return self

    def set_cross_functional_collaboration(self):
        self.profile.cross_functional_collaboration = True
        return self
    def set_effective_communication(self):
        self.profile.effective_communication = True
        return self

    def set_ownership_and_accountability(self):
        self.profile.ownership_and_accountability = True
        return self

    def set_system_thinking(self):
        self.profile.system_thinking = True
        return self

    def set_strategic_alignment(self):
        self.profile.strategic_alignment = True
        return self

    def build(self):
        return self.profile

if __name__ == "__main__":
    # 1. Initialize the builder
    builder = ProfileBuilder()

    print("\nJr",end=" ")
    print (builder
                .set_curiosity()
                .set_problem_solving()
                .set_technical_proficiency()
                .set_attention_to_quality()
                .build())

    print("\nSr", end=" ")
    print (builder
                .set_independent_delivery()
                .set_effective_communication()
                .set_cross_functional_collaboration()
                .build())

    print("\nLead", end=" ")
    print (builder
               .set_ownership_and_accountability()
               .set_strategic_alignment()
               .set_system_thinking()
               .build())