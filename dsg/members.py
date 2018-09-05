class Dan:
    """Represents a member of DSG. Specifically represents Dan."""

    def __init__(self):
        pass

    @property
    def github(self):
        """Returns the github address of the member"""

        return f"https://github.com/RainbowLegend"

    @property
    def bhsSchedule(self):
        """Returns the BHS schedule of the member"""

        return "1 - Honors Lit\n2 - PhysEd/HealthEd/Study\n3 - Honors Spanish II\n4 - Honors Bio\n" \
               "5 - Honors Comp Sci 1\n6 - Honors USH 1\n7 - Honors Geometry"
