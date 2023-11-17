from .cisco import CiscoBusinessSwitch, CiscoCatalyst


class AutomationFactory:
    _automations = {}

    @classmethod
    def get_obj(cls, automation_type):
        if automation_type not in cls._automations:
            if automation_type == "cisco_business":
                cls._automations[automation_type] = CiscoBusinessSwitch()
            elif automation_type == "cisco_catalyst":
                cls._automations[automation_type] = CiscoCatalyst()
            else:
                raise ValueError("Device functionality not found!!")
        return cls._automations[automation_type]
