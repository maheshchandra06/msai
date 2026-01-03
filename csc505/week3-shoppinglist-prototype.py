# Defines the screen names
# Prints the total number of screens
# Prints the navigation flow (e.g., "Home → Add Item → Save → View List")
# Optionally includes descriptions of what each screen doe

SCREENS = ["Home", "View Lists", "Create List", "Edit List", "Edit Share Settings", "Edit Reminder Settings"]

NAVIGATION_FLOWS = [
    "Home → Create List",
    "Home → Create List → Edit List",
    "Home → View Lists",
    "Home → View Lists → Edit List → Edit Share Settings",
    "Home → View Lists → Edit List → Edit Reminder Settings"
]


def display_shopping_list_prototype():
    """Prints the prototype summary including screen count and navigation flow."""
    header = "----------- Shopping List Prototype -----------"
    print(f"{header.center(50)}")
    screen_names="".join([f"{name}, " for name in SCREENS]).removesuffix(", ")
    print(f"Screens: {screen_names}")
    print(f"Total number of screens: {len(SCREENS)}")

    print("\nNavigation Flow:")
    for path in NAVIGATION_FLOWS:
        print(path)

if __name__ == "__main__":
    display_shopping_list_prototype()


