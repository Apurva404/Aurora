from constants import Weekday
import data_reader

from scheduler import schedule


if __name__ == "__main__":
    test_cases = [
        "src/testcase/test1.json",
        "src/testcase/test2.json",
        "src/testcase/test3.json",
        "src/testcase/test4.json",
        "src/testcase/test5.json",
        "src/testcase/test6.json",
        "src/testcase/test7.json",
    ]

    for test_case in test_cases:
        print(f"Testcase : {test_case}\n")

        test_description, test_buildings, test_employees = \
            data_reader.read_data(test_case)

        print(f"Scenario : {test_description}\n")
        work_schedule, unschedulable_buildings = \
            schedule(test_buildings, test_employees)

        print("Unschedulable buildings :")
        for building in unschedulable_buildings:
            print(f"Building {building.id} {building.get_building_type()}")

        print("\n")

        for day in Weekday:
            print(f"On {day} : ")
            if not work_schedule[day]:
                print("No work.", end='')
            for building, workers in work_schedule[day].items():
                print(f"Building {building.id} of type \
                      {building.get_building_type()} will be \
                      serviced by ", end='')
                for worker in workers:
                    print(
                        f"Employee {worker.id} ({worker.__class__.__name__})",
                        end=','
                    )
                print("\n")
            print("\n")
        print("\n")
