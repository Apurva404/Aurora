class Capacity:
    def __init__(self):
        self._certified_installer_capcity = 0
        self._pending_cert_installer_capcity = 0
        self._laborer_capcity = 0

    def get_certified_installer_capcity(self) -> int:
        return self._certified_installer_capcity

    def get_pending_cert_installer_capcity(self) -> int:
        return self._pending_cert_installer_capcity

    def get_laborer_capcity(self) -> int:
        return self._laborer_capcity

    def set_certified_installer_capcity(self, n: int):
        self._certified_installer_capcity = n

    def set_pending_cert_installer_capcity(self, n: int):
        self._pending_cert_installer_capcity = n

    def set_laborer_capcity(self, n: int):
        self._laborer_capcity = n

    def increase_certified_installer_capcity_by(self, n: int):
        self._certified_installer_capcity = \
            self._certified_installer_capcity + n

    def increase_pending_cert_installer_capcity_by(self, n: int):
        self._pending_cert_installer_capcity = \
            self._pending_cert_installer_capcity + n

    def increase_laborer_capcity_by(self, n: int):
        self._laborer_capcity = self._laborer_capcity + n

    def decrease_certified_installer_capcity_by(self, n: int):
        self._certified_installer_capcity = \
            self._certified_installer_capcity - n

    def decrease_pending_cert_installer_capcity_by(self, n: int):
        self._pending_cert_installer_capcity = \
            self._pending_cert_installer_capcity - n

    def decrease_laborer_capcity_by(self, n: int):
        self._laborer_capcity = self._laborer_capcity - n
