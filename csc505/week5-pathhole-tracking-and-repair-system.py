# PHTRS – Pothole Tracking and Repair System

class Actor:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.use_cases = []

    def add_use_case(self, use_case):
        self.use_cases.append(use_case)

    def __str__(self):
        output = f"Actor: {self.name}\n  Description: {self.description}\n"
        output += "  Associated Use Cases:\n"
        for uc in self.use_cases:
            output += f"    - {uc.name}({', '.join(uc.arguments)}): {uc.description}\n"
        return output


class UseCase:
    def __init__(self, name, description, arguments):
        self.name = name
        self.description = description
        self.arguments = arguments  # list of required inputs



# Domain Model Classes
class Pothole:
    def __init__(self, pothole_id, street_address, size, location, district, repair_priority):
        self.pothole_id = pothole_id
        self.street_address = street_address
        self.size = size
        self.location = location
        self.district = district
        self.repair_priority = repair_priority

    def __str__(self):
        return (f"Pothole[{self.pothole_id}] at {self.street_address}, "
                f"size={self.size}, location={self.location}, "
                f"district={self.district}, priority={self.repair_priority}")


class WorkOrder:
    def __init__(self, work_order_id, pothole, crew_id, crew_size,
                 equipment_assigned, hours_applied, status,
                 filler_amount, cost):
        self.work_order_id = work_order_id
        self.pothole = pothole
        self.crew_id = crew_id
        self.crew_size = crew_size
        self.equipment_assigned = equipment_assigned
        self.hours_applied = hours_applied
        self.status = status
        self.filler_amount = filler_amount
        self.cost = cost

    def __str__(self):
        return (f"WorkOrder[{self.work_order_id}] for Pothole[{self.pothole.pothole_id}], "
                f"crew={self.crew_id}, status={self.status}, "
                f"hours={self.hours_applied}, cost={self.cost}")


class DamageClaim:
    def __init__(self, claim_id, citizen_name, citizen_address, citizen_phone,
                 damage_type, damage_amount):
        self.claim_id = claim_id
        self.citizen_name = citizen_name
        self.citizen_address = citizen_address
        self.citizen_phone = citizen_phone
        self.damage_type = damage_type
        self.damage_amount = damage_amount

    def __str__(self):
        return (f"DamageClaim[{self.claim_id}] by {self.citizen_name}, "
                f"type={self.damage_type}, amount={self.damage_amount}")


if __name__ == "__main__":

    # Define Use Cases WITH ARGUMENTS
    report_pothole = UseCase(
        "ReportPothole",
        "Citizen submits pothole details.",
        arguments=[
            "street_address",
            "size",
            "location",
            "optional_image"
        ]
    )

    track_pothole_status = UseCase(
        "TrackPotholeStatus",
        "Citizen checks repair progress.",
        arguments=["pothole_id"]
    )

    submit_damage_claim = UseCase(
        "SubmitDamageClaim",
        "Citizen files a damage claim.",
        arguments=[
            "citizen_name",
            "citizen_address",
            "citizen_phone",
            "damage_type",
            "damage_amount",
            "evidence_image"
        ]
    )

    view_potholes = UseCase(
        "ViewReportedPotholes",
        "Admin views and filters pothole reports.",
        arguments=["district_filter", "priority_filter"]
    )

    assign_work_order = UseCase(
        "AssignWorkOrder",
        "Admin assigns a repair crew to a pothole.",
        arguments=[
            "pothole_id",
            "crew_id",
            "crew_size",
            "equipment_assigned"
        ]
    )

    update_repair_status = UseCase(
        "UpdateRepairStatus",
        "Crew updates pothole repair status.",
        arguments=[
            "work_order_id",
            "status",
            "hours_applied",
            "filler_amount"
        ]
    )

    log_repair_details = UseCase(
        "LogRepairDetails",
        "Crew logs materials, labor, and equipment usage.",
        arguments=[
            "work_order_id",
            "equipment_used",
            "hours_applied",
            "filler_amount"
        ]
    )

    process_damage_claims = UseCase(
        "ProcessDamageClaims",
        "Admin reviews and processes damage claims.",
        arguments=["claim_id", "approval_status"]
    )

    # Define Actors
    citizen = Actor("Citizen", "Resident who reports potholes and submits claims.")
    citizen.add_use_case(report_pothole)
    citizen.add_use_case(track_pothole_status)
    citizen.add_use_case(submit_damage_claim)

    admin = Actor("PublicWorksAdmin", "Manages potholes, work orders, and claims.")
    admin.add_use_case(view_potholes)
    admin.add_use_case(assign_work_order)
    admin.add_use_case(process_damage_claims)

    repair_crew = Actor("RepairCrew", "Field crew repairing potholes.")
    repair_crew.add_use_case(update_repair_status)
    repair_crew.add_use_case(log_repair_details)

    actors = [citizen, admin, repair_crew]

    # Print Actor Information
    print("\n# PHTRS Actor & Use Case Overview #\n")
    for actor in actors:
        print(actor)

    # Print Diagram Summary
    print("\n# Diagram Summary #")
    print(
        "The PHTRS system models three actors—Citizens, Public Works Admins, and Repair Crews—"
        "each associated with explicit use cases that define required input arguments. "
        "Domain classes (Pothole, WorkOrder, DamageClaim) represent the core data structures "
        "used throughout the workflow, from pothole reporting to repair execution and claim processing."
    )
