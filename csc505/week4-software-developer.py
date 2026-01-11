TRAIT_DESCRIPTIONS = {
    "curiosity": "The ability to learn new things quickly and effectively",
    "independent_delivery": "The ability to work independently and make decisions without constant supervision",
    "technical_proficiency": "Deep understanding of languages (Java / Python), frameworks, and underlying computer science principles",
    "problem_solving": "Breaking down complex, ambiguous problems into smaller, manageable, and logical steps to find an efficient solution",
    "attention_to_quality": "Writing clean, readable code and identifying edge cases or potential bugs before they reach the user.",
    "cross_functional_collaboration": "The ability to work effectively within a team (using tools like Git) and across different departments to reach a common goal.",
    "effective_communication": "The ability to explain complex technical concepts clearly to both fellow developers and non-technical stakeholders.",
    "ownership_and_accountability": "Taking full responsibility for your code from development through to production. It means 'owning' the outcome, not just the task.",
    "system_thinking": "The ability to see the big picture and understand how your work fits into the overall goals of the project or organization.",
    "strategic_alignment": "The ability to align your work with the organization's goals and make decisions that contribute to the organization's success."
}

DEVELOPER_TRAITS = list(TRAIT_DESCRIPTIONS.keys())

class DeveloperProfile:
    def __init__(self):
        self.traits = {
            trait: False for trait in DEVELOPER_TRAITS
        }

    def __str__(self):
        active_traits = [
            trait
            for trait in DEVELOPER_TRAITS
            if self.traits[trait]
        ]
        developer_traits= "".join([f"\n - {trait.title().replace('_'," ")} : {TRAIT_DESCRIPTIONS[trait].casefold().capitalize()}" for trait in active_traits])
        return f"Developer Profile: {developer_traits}"

class ProfileBuilder:
    def __init__(self):
        self.profile = DeveloperProfile()

    def set_trait(self,trait_name):
        if trait_name in self.profile.traits:
            self.profile.traits[trait_name] = True
        return self

    def build(self):
        return self.profile

class ProfileDirector:
    def __init__(self):
        self.director = ProfileBuilder()

    def build_junior_dev_profile(self):
        return (f"\nJunior {self.director
                .set_trait("curiosity")
                .set_trait("problem_solving")
                .set_trait("technical_proficiency")
                .set_trait("attention_to_quality")
                .build()}")

    def build_senior_dev_profile(self):
        return (f"\nSenior {self.director
                .set_trait("independent_delivery")
                .set_trait("effective_communication")
                .set_trait("cross_functional_collaboration")
                .build()}")

    def build_lead_dev_profile(self):
        return (f"\nLead {self.director
               .set_trait("ownership_and_accountability")
               .set_trait("strategic_alignment")
               .set_trait("system_thinking")
                .build()}")

if __name__ == "__main__":
    director = ProfileDirector()
    jr_dev_profile = director.build_junior_dev_profile()
    senior_dev_profile = director.build_senior_dev_profile()
    lead_dev_profile = director.build_lead_dev_profile()
    print(jr_dev_profile)
    print(senior_dev_profile)
    print(lead_dev_profile)