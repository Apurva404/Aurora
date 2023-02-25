from constants import BuildingType
from model.employees import CertifiedSolarInstaller, \
    UncertifiedEmployee, PendingCertificationSolarInstaller, \
    Employee


BUILDING_RESOURCE_REQUIREMENT_MAP = {
    BuildingType.SINGLE_STORY: [
        (CertifiedSolarInstaller, 1)
    ],
    BuildingType.DOUBLE_STORY: [
        (CertifiedSolarInstaller, 1),
        (UncertifiedEmployee, 1)
    ],
    BuildingType.COMMERCIAL: [
        (CertifiedSolarInstaller, 2),
        (PendingCertificationSolarInstaller, 2),
        (Employee, 4)
    ],
}
