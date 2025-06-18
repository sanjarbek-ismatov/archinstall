from typing import override

from archinstall.default_profiles.profile import GreeterType, ProfileType
from archinstall.default_profiles.xorg import XorgProfile


class PlasmaProfile(XorgProfile):
	def __init__(self) -> None:
		super().__init__('KDE Plasma', ProfileType.DesktopEnv)

	@property
	@override
	def packages(self) -> list[str]:
		return [
			'plasma-desktop',
			'konsole',
			'kate',
			'dolphin',
			'ark',
            'plasma-nm',
            'plasma-pa',
            'kscreen',
            'kinfocenter',
            'powerdevil',
            'xdg-desktop-portal-kde',
            'kde-gtk-config',
            'kwallet-pam',
            'kwrited',
            'sddm-kcm',
			'breeze-gtk',
			'plasma-browser-integration',
			'plasma-disks',
			'plasma-systemmonitor',
			'breeze5',
			'spectacle',
		]

	@property
	@override
	def default_greeter_type(self) -> GreeterType:
		return GreeterType.Sddm
