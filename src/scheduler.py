from typing import Dict, List, Tuple, Type

from building_requirement import BUILDING_RESOURCE_REQUIREMENT_MAP
from constants import Weekday
from model.buildings import Building
from model.capacity import Capacity
from model.employees import Employee, CertifiedSolarInstaller, \
    UncertifiedEmployee, PendingCertificationSolarInstaller, Laborer


def get_weekly_worker_availability(
        employees: List[Employee]
        ) -> Dict[Weekday, Dict[Type[Employee], List[Employee]]]:
    """Compute worker availability.

    Arrange the data present in individual employee's availibility into
    a map across which provides easy access to the data, which employees
    are available on a given day. The data is also categorized by employee
    type.
    """
    available_workers = {
        Weekday.Monday: {
            CertifiedSolarInstaller: [],
            PendingCertificationSolarInstaller: [],
            Laborer: []
        },
        Weekday.Tuesday: {
            CertifiedSolarInstaller: [],
            PendingCertificationSolarInstaller: [],
            Laborer: []
        },
        Weekday.Wednesday: {
            CertifiedSolarInstaller: [],
            PendingCertificationSolarInstaller: [],
            Laborer: []
        },
        Weekday.Thursday: {
            CertifiedSolarInstaller: [],
            PendingCertificationSolarInstaller: [],
            Laborer: []
        },
        Weekday.Friday: {
            CertifiedSolarInstaller: [],
            PendingCertificationSolarInstaller: [],
            Laborer: []
        }
    }

    for employee in employees:
        emp_availability = employee.getAvailability()
        for day in Weekday:
            if emp_availability[day]:
                available_workers[day][type(employee)].append(employee)

    return available_workers


def get_weekly_worker_capacity(
        worker_availibility: Dict[Weekday, Dict[Type[Employee], List[Employee]]]  # noqa: E501
        ) -> Dict[Weekday, Capacity]:
    """Compute available worker in a week.

    Transform the worker availibility data into capacity of man power
    available per day of the week
    """
    weekly_capacity = {
        Weekday.Monday: Capacity(),
        Weekday.Tuesday: Capacity(),
        Weekday.Wednesday: Capacity(),
        Weekday.Thursday: Capacity(),
        Weekday.Friday: Capacity()
    }

    for day in Weekday:
        weekly_capacity[day].set_certified_installer_capcity(
            # 1 since assumption is each worker is booked for the entire day
            len(worker_availibility[day][CertifiedSolarInstaller]) * 1
        )
        weekly_capacity[day].set_pending_cert_installer_capcity(
            # 1 since assumption is each worker is booked for the entire day
            len(worker_availibility[day][PendingCertificationSolarInstaller]) * 1  # noqa: E501
        )
        weekly_capacity[day].set_laborer_capcity(
            # 1 since assumption is each worker is booked for the entire day
            len(worker_availibility[day][Laborer]) * 1
        )

    return weekly_capacity


def generate_building_workday_assignment(
        buildings: List[Building],
        weekly_capacity: Dict[Weekday, Capacity]
        ) -> Tuple[Dict[Weekday, Dict[Building, Capacity]], List[Building]]:  # noqa: E501
    """Assign buildings to workday and compute their requirement.

    Process each building and assign it a workday, as well as record
    the type of employees required to complete the job.
    """
    scheduled_buildings = {
        Weekday.Monday: {},
        Weekday.Tuesday: {},
        Weekday.Wednesday: {},
        Weekday.Thursday: {},
        Weekday.Friday: {},
    }

    unschedulable_buildings = []

    for building in buildings:
        requirements = BUILDING_RESOURCE_REQUIREMENT_MAP.get(
            building.get_building_type()
        )
        for day in Weekday:
            schedulable = True
            booked_capacity = Capacity()
            for requirement in requirements:
                requirement_type = requirement[0]
                required_quantity = requirement[1]
                if requirement_type == CertifiedSolarInstaller:
                    # If possible satisfy requirement
                    if required_quantity <= weekly_capacity[day].get_certified_installer_capcity():  # noqa: E501
                        booked_capacity.increase_certified_installer_capcity_by(required_quantity)  # noqa: E501
                        weekly_capacity[day].decrease_certified_installer_capcity_by(required_quantity)  # noqa: E501
                        continue
                    # else can't meet requirement, try next day
                    schedulable = False
                    break
                elif requirement_type == PendingCertificationSolarInstaller:
                    # If possible satisfy requirement
                    if required_quantity <= weekly_capacity[day].get_pending_cert_installer_capcity():  # noqa: E501
                        booked_capacity.increase_pending_cert_installer_capcity_by(required_quantity)  # noqa: E501
                        weekly_capacity[day].decrease_pending_cert_installer_capcity_by(required_quantity)  # noqa: E501
                        continue
                    # else can't meet requirement, try next day
                    schedulable = False
                    break
                elif requirement_type == UncertifiedEmployee:
                    # Choose first the resource which is more flexible
                    # if possible satisfy requirement with only laborers
                    if required_quantity <= weekly_capacity[day].get_laborer_capcity():  # noqa: E501
                        booked_capacity.increase_laborer_capcity_by(required_quantity)  # noqa: E501
                        weekly_capacity[day].decrease_laborer_capcity_by(required_quantity)  # noqa: E501
                        continue
                    # otherwise pick as many laborer as possible
                    booked_capacity.increase_laborer_capcity_by(
                        weekly_capacity[day].get_laborer_capcity()
                    )
                    required_quantity = required_quantity - weekly_capacity[day].get_laborer_capcity()  # noqa: E501
                    weekly_capacity[day].set_laborer_capcity(0)

                    # fill the rest with pending certs
                    if required_quantity <= weekly_capacity[day].get_pending_cert_installer_capcity():  # noqa: E501
                        booked_capacity.increase_pending_cert_installer_capcity_by(required_quantity)  # noqa: E501
                        weekly_capacity[day].decrease_pending_cert_installer_capcity_by(required_quantity)  # noqa: E501
                        continue
                    # else can't meet requirement, try next day
                    schedulable = False
                    break
                elif requirement_type == Employee:
                    # Choose first the resource which is more flexible
                    # if possible satisfy requirement with only laborers
                    if required_quantity <= weekly_capacity[day].get_laborer_capcity():  # noqa: E501
                        booked_capacity.increase_laborer_capcity_by(required_quantity)  # noqa: E501
                        weekly_capacity[day].decrease_laborer_capcity_by(required_quantity)  # noqa: E501
                        continue
                    # otherwise pick as many laborer as possible
                    remaining_laborer = \
                        weekly_capacity[day].get_laborer_capcity()
                    booked_capacity.increase_laborer_capcity_by(
                        remaining_laborer
                    )
                    required_quantity = required_quantity - remaining_laborer
                    weekly_capacity[day].set_laborer_capcity(0)

                    # if possible satisfy remaining requirement with only
                    # pending certification installers
                    if required_quantity <= weekly_capacity[day].get_pending_cert_installer_capcity():  # noqa: E501
                        booked_capacity.increase_pending_cert_installer_capcity_by(required_quantity)  # noqa: E501
                        weekly_capacity[day].decrease_pending_cert_installer_capcity_by(required_quantity)  # noqa: E501
                        continue
                    # otherwise pick as many pending certs as possible
                    remaining_pending_certs = weekly_capacity[day].get_pending_cert_installer_capcity()  # noqa: E501
                    booked_capacity.increase_pending_cert_installer_capcity_by(remaining_pending_certs)  # noqa: E501
                    required_quantity = required_quantity - remaining_pending_certs  # noqa: E501
                    weekly_capacity[day].set_pending_cert_installer_capcity(0)

                    # fill the rest with certs
                    if required_quantity <= weekly_capacity[day].get_certified_installer_capcity():  # noqa: E501
                        booked_capacity.increase_certified_installer_capcity_by(required_quantity)  # noqa: E501
                        weekly_capacity[day].decrease_certified_installer_capcity_by(required_quantity)  # noqa: E501
                        continue

                    # else can't meet requirement, try next day
                    schedulable = False
                    break

            if schedulable:
                # assign buiding to current day and record required
                # employee distribution
                scheduled_buildings[day][building] = booked_capacity
                # process next building
                break 
            else:
                # return all booked resources and try the next available day
                weekly_capacity[day].increase_certified_installer_capcity_by(
                    booked_capacity.get_certified_installer_capcity()
                )
                weekly_capacity[day].increase_pending_cert_installer_capcity_by(  # noqa: E501
                    booked_capacity.get_pending_cert_installer_capcity()
                )
                weekly_capacity[day].increase_laborer_capcity_by(
                    booked_capacity.get_laborer_capcity()
                )

        if not schedulable:
            unschedulable_buildings.append(building)

    return scheduled_buildings, unschedulable_buildings


def assign_workers_to_building(
        scheduled_buildings: Dict[Weekday, Dict[Building, Capacity]],  # noqa: E501
        weekly_employee_availability: Dict[Weekday, Dict[Type[Employee], List[Employee]]]  # noqa: E501
        ) -> Dict[Weekday, Dict[Building, List[Employee]]]:  # noqa: E501
    """Assign individual employee to a building.

    Since buildings have already been assigned to workdays and it is
    guaranteed that the company has enough resources to handle the
    building on that day, we can safely assign the right class of employee
    in a first come first serve basis to the buildings without the fear of
    overbooking.
    """
    work_schedule = {
        Weekday.Monday: {},
        Weekday.Tuesday: {},
        Weekday.Wednesday: {},
        Weekday.Thursday: {},
        Weekday.Friday: {}
    }

    for day in Weekday:
        day_schedule = scheduled_buildings[day]
        for building, requirement in day_schedule.items():
            num_certs = requirement.get_certified_installer_capcity()
            num_pending_certs = \
                requirement.get_pending_cert_installer_capcity()
            num_laborer = requirement.get_laborer_capcity()

            if building not in work_schedule[day]:
                work_schedule[day][building] = []

            # since the building capacity has already been planned,
            # we can safely assign the correct type of installer to this
            # building and remove them from the availibility map
            certs_to_assign = weekly_employee_availability[day][CertifiedSolarInstaller][0:num_certs]  # noqa: E501
            weekly_employee_availability[day][CertifiedSolarInstaller] = \
                weekly_employee_availability[day][CertifiedSolarInstaller][num_certs:]  # noqa: E501
            work_schedule[day][building] = \
                work_schedule[day][building] + certs_to_assign

            pending_certs_to_assign = \
                weekly_employee_availability[day][PendingCertificationSolarInstaller][0:num_pending_certs]  # noqa: E501
            weekly_employee_availability[day][PendingCertificationSolarInstaller] = \
                weekly_employee_availability[day][PendingCertificationSolarInstaller][num_pending_certs:]  # noqa: E501
            work_schedule[day][building] = \
                work_schedule[day][building] + pending_certs_to_assign

            laborers_to_assign = weekly_employee_availability[day][Laborer][0:num_laborer]  # noqa: E501
            weekly_employee_availability[day][Laborer] = \
                weekly_employee_availability[day][Laborer][num_laborer:]
            work_schedule[day][building] = \
                work_schedule[day][building] + laborers_to_assign

    return work_schedule


def schedule(
        buildings: List[Building],
        employees: List[Employee]
        ) -> Tuple[Dict[Weekday, Dict[Building, List[Employee]]], List[Building]]:  # noqa: E501
    # Compute which employee is available on which day
    weekly_employee_availability = \
        get_weekly_worker_availability(employees)

    # Compute how much categorized man power is available each day
    weekly_capacity = \
        get_weekly_worker_capacity(weekly_employee_availability)

    # assign buildings to a day and determine the worker requirement for them
    scheduled_buildings, unschedulable_buildings = \
        generate_building_workday_assignment(buildings, weekly_capacity)

    # now we need to assign employees to building on a given day to complete
    # the work schedule
    work_schedule = assign_workers_to_building(
        scheduled_buildings,
        weekly_employee_availability
    )

    return work_schedule, unschedulable_buildings
